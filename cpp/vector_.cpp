#include <fmt/core.h>

template <typename T>
class Vector {
   private:
    /// The number of elements in the vector.
    size_t size_;
    /// The maximum number of elements that can be stored in the vector.
    size_t capacity_;
    /// The pointer to the first element in the vector.
    T* data_;

    /// Resizes the vector to the given capacity.
    void resize(size_t new_capacity) {
        T* new_data = new T[new_capacity];
        if (data_ == nullptr) {
            throw std::bad_alloc();
        }
        std::copy(data_, data_ + size_, new_data);
        delete[] data_;
        data_ = new_data;
        capacity_ = new_capacity;
    }

   public:
    Vector() : size_(0), capacity_(0), data_(nullptr) {}

    /// Constructs a vector with the given elements.
    Vector(std::initializer_list<T> list)
        : size_(list.size()),
          capacity_(list.size()),
          data_(new T[list.size()]) {
        std::copy(list.begin(), list.end(), data_);
    }
    /// Constructs a vector with the given capacity.
    Vector<T>(std::size_t capacity) {
        data_ = new T[capacity];
        size_ = 0;
        capacity_ = capacity;
    }

    // Support for enhanced for loops
    T* begin() { return data_; }
    T* end() { return data_ + size_; }
    const T* begin() const { return data_; }
    const T* end() const { return data_ + size_; }

    /// Destructor.
    ~Vector() { delete[] data_; }

    /// Appends a new element to the end of the vector.
    void push_back(const T& value) {
        if (size_ == capacity_) {
            resize(size_ == 0 ? 1 : size_ * 2);
        }
        data_[size_++] = value;
    }

    /// Returns the number of elements in the vector.
    size_t size() const { return size_; }

    /// Index operator
    T& operator[](size_t index) { return data_[index]; }
    /// Index operator.
    const T& operator[](size_t index) const { return data_[index]; }

    /// Assignment operator overload
    Vector& operator=(const Vector& other) {
        if (this != &other) {
            T* new_data = new T[other.capacity_];
            std::copy(other.data_, other.data_ + other.size_, new_data);
            delete[] data_;
            data_ = new_data;
            size_ = other.size_;
            capacity_ = other.capacity_;
        }
        return *this;
    }
};

int main() {
    auto nums = Vector<int>(10);

    for (int i = 0; i < 10; i++) {
        nums.push_back(i);
    }

    nums = {1, 2, 3, 4, 5};

    for (auto num : nums) {
        fmt::print("{}\n", num);
    }

    return 0;
}