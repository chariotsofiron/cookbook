/// [linux socket manpages](https://man7.org/linux/man-pages/man2/socket.2.html)
/// Not sure if I'll ever have to reference this again
/// This was a repo for testing getting nic timestamps for TCP Streams
/// I used posix-socket-rs as reference.
use std::io::{Read, Write, IoSliceMut};
use std::net::{Shutdown, TcpListener, TcpStream, SocketAddr, Ipv4Addr};
use std::os::unix::prelude::AsRawFd;
use std::time::Duration;

fn main() {
    std::thread::spawn(|| {
        let listener = TcpListener::bind("127.0.0.1:3334").unwrap();
        println!("Server listening on port 3334");
        for stream in listener.incoming() {
            match stream {
                Ok(mut stream) => {
                    println!("New connection: {}", stream.peer_addr().unwrap());
                    std::thread::spawn(move || {
                        // connection succeeded
                        let mut data = [0 as u8; 50]; // using 50 byte buffer
                        stream.write(b"Hello").unwrap();
                        while match stream.read(&mut data) {
                            Ok(size) => {
                                // echo everything!
                                stream.write(&data[0..size]).unwrap();
                                true
                            }
                            Err(_) => {
                                println!(
                                    "An error occurred, terminating connection with {}",
                                    stream.peer_addr().unwrap()
                                );
                                stream.shutdown(Shutdown::Both).unwrap();
                                false
                            }
                        } {}
                    });
                }
                Err(e) => println!("Error connection failed: {}", e)
            }
        }
        // close the socket server
        drop(listener);
    });
    std::thread::sleep(Duration::from_millis(1000)); // wait for server to start
    

    let mut socket = TcpStream::connect("127.0.0.1:3334").unwrap();
    // let mut buffer = vec![0u8; 40];
    // socket.read(&mut buffer).unwrap();
    // println!("buffer={:?}", buffer);


    // let ip = "127.0.0.1".parse::<Ipv4Addr>().unwrap();
    // let port = 3334u16;

    // // create the address
    // let inner;
    // unsafe {
    //     let ip : u32 = std::mem::transmute(ip.octets());
    //     inner = libc::sockaddr_in {
    //         sin_family: libc::AF_INET  as libc::sa_family_t,
    //         sin_addr: libc::in_addr { s_addr: ip },
    //         sin_port: port.to_be(),
    //         ..std::mem::zeroed()
    //     };
    // }


    // // create the socket
    // let socket_fd;
    // unsafe {
    //     socket_fd = libc::socket(libc::AF_INET, libc::SOCK_STREAM | libc::SOCK_CLOEXEC, libc::IPPROTO_TCP);
    //     let err = libc::connect(socket_fd, &inner as *const _ as *const _, std::mem::size_of::<libc::sockaddr_in>() as libc::socklen_t);    
    //     println!("err={}", err);
    // }



    // Set timestamping socket option
    let optval: libc::c_uint = 0xf;
    unsafe {
        libc::setsockopt(
            socket.as_raw_fd(),
            libc::SOL_SOCKET,
            libc::SO_TIMESTAMPNS,
            &optval as *const _ as *const libc::c_void,
            std::mem::size_of_val(&optval) as libc::socklen_t,
        );
    }


    let mut buf = vec![0u8; 40];
    let mut cdata_buf = [0; 40];


    
    
    let flags = 2;
    
    // unsafe {
        //     libc::recv(socket.as_raw_fd(), buf.as_mut_ptr() as *mut libc::c_void, buf.len(), flags);
        // }
        // println!("{:?}", buf);
        // return;
        
    let mut data = [IoSliceMut::new(&mut buf)];
    unsafe {
        let mut header = std::mem::zeroed::<libc::msghdr>();
        header.msg_iov = data.as_ptr() as *mut libc::iovec;
        header.msg_iovlen = data.len();
        header.msg_control = cdata_buf.as_mut_ptr() as *mut libc::c_void;
        header.msg_controllen = cdata_buf.len();
        let ret = libc::recvmsg(socket.as_raw_fd(), &mut header, flags | libc::MSG_CMSG_CLOEXEC);
        println!("ret={}, {}, {}", ret, data.len(), cdata_buf.len());

        // cdata.length = header.msg_controllen as usize;
        // cdata.truncated = header.msg_flags & libc::MSG_CTRUNC != 0;
        // Ok((ret as usize, header.msg_flags))
    }

    println!("{:?}", buf);
    println!("{:?}", cdata_buf);


    let timestamp = u64::from_le_bytes(cdata_buf[16..24].try_into().unwrap());
    let nanos = u64::from_le_bytes(cdata_buf[24..32].try_into().unwrap());
    println!("timestamp: {}", timestamp * 1_000_000_000 + nanos);

}