#include <utility>  // std::exchange

template<typename T>
class UniquePointer {
  public:
    /// Default constructor.
    UniquePointer() : ptr_(nullptr) {}
    /// Constructs a unique pointer from a raw pointer.
    explicit UniquePointer(T* ptr) : ptr_(ptr) {}

    /// Delete copy constructor and assignment operator.
    UniquePointer(const UniquePointer& other) = delete;
    UniquePointer& operator=(const UniquePointer& other) = delete;

    /// Move constructor.
    UniquePointer(UniquePointer&& other) : ptr_(other.release()) {}

    /// Move assignment operator.
    UniquePointer& operator=(UniquePointer&& other) {
        if (this != &other) {
            reset(other.release());
        }
        return *this;
    }

    /// Release the ownership of the pointer.
    T* release() {
        return std::exchange(ptr_, nullptr);
    }

    /// Reset the pointer to a new value. Swaps out the thing we own.
    void reset(T* ptr) {
        T* old_ptr = std::exchange(ptr_, ptr);
        delete old_ptr;
    }

    ~UniquePointer() {
        delete ptr_;
    }

    /// Dereference operator.
    T& operator*() const {
        return *ptr_;
    }
    /// Arrow operator.
    T* operator->() const {
        return ptr_;
    }

  private:
    T* ptr_;
};

template<typename T, typename... Args>
UniquePointer<T> make_unique(Args&&... args) {
    return UniquePointer<T>(new T(std::forward<Args>(args)...));
}