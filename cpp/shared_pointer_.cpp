#include <iostream>

template<typename T>
class SmartPointer {
public:
    T* ptr;
    int *ref_count;
    SmartPointer(T* p) : ptr(p), ref_count(new int(1)) {}
    SmartPointer(const SmartPointer& other) : ptr(other.ptr), ref_count(other.ref_count) {
        ++(*ref_count);
    }
    SmartPointer& operator=(const SmartPointer& other) {
        if (this != &other) {
            --(*this->ref_count);
            if (*this->ref_count == 0) {
                delete this->ptr;
                delete this->ref_count;
            }
            this->ptr = other.ptr;
            this->ref_count = other.ref_count;
            ++(*this->ref_count);
        }
        return *this;
    }
    ~SmartPointer() {
        --(*ref_count);
        if (*ref_count == 0) {
            delete ptr;
            delete ref_count;
        }
    }
};

int main() {
    SmartPointer<int> p(new int(1));
    SmartPointer<int> q(p);
    SmartPointer<int> r(q);
    
    std::cout << *p.ref_count << std::endl;

    return 0;
}