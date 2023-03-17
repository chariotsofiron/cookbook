"""Functions for interfacing with I/O."""
import fcntl
import os
import select
import subprocess
import sys
import termios


def get_key(blocking: bool = True) -> str:
    """Get currently pressed key.
    - https://stackoverflow.com/a/13207724/9518712
    - http://effbot.org/pyfaq/how-do-i-get-a-single-keypress-at-a-time.htm

    :param blocking: whether to wait for a key press
    :return: The currently pressed key
    """
    file_descriptor = sys.stdin.fileno()
    oldterm = termios.tcgetattr(file_descriptor)
    newattr = oldterm[:]
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    # turns off stdin’s echoing and disables canonical mode
    termios.tcsetattr(file_descriptor, termios.TCSANOW, newattr)
    oldflags = fcntl.fcntl(file_descriptor, fcntl.F_GETFL)
    # obtain stdin’s file descriptor flags and modify them for non-blocking mode
    fcntl.fcntl(file_descriptor, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    if blocking:
        # wait for incoming characters
        select.select([file_descriptor], [], [])
    key = sys.stdin.read(1)

    # close
    termios.tcsetattr(file_descriptor, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(file_descriptor, fcntl.F_SETFL, oldflags)
    return key


def read_clipboard() -> str:
    """Get the contents of the system clipboard.

    :return: The system clipboard as a string
    """
    with subprocess.Popen(["pbpaste"], stdout=subprocess.PIPE) as process:
        process.wait()
        if process.stdout:
            clipboard = process.stdout.read().decode("utf-8")
            return clipboard
    return ""
