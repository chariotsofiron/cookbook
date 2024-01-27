
/// https://en.wikipedia.org/wiki/Reservoir_sampling
#include <fmt/core.h>  // fmt::println
#include <fmt/ranges.h>
#include <fmt/ostream.h>  // fmt::join

#include <random>  // std::uniform_int_distribution

template<typename T>
class Reservoir {
  private:
    // Random number generator
    std::mt19937 rng_;
    /// Reservoir to hold the current sample
    std::vector<T> reservoir_;
    /// The size of the sample
    const size_t size_;
    /// The number of observations so far
    size_t count_ = 0;

    size_t get_rand_index() {
        // Generate a random integer uniformly between min and max
        std::uniform_int_distribution<size_t> dist(0, count_);
        return dist(rng_);
    }

  public:
    Reservoir(size_t size) : rng_(), reservoir_(), size_(size) {
        reservoir_.reserve(size);
        // Initialize the random number generator
        std::random_device device;
        rng_ = std::mt19937(device());
    }
    void add(T observation) {
        count_++;
        // If we have space for the new element, just add it
        if (reservoir_.size() < size_) {
            reservoir_.push_back(observation);
        } else {
            // Otherwise, replace a random element with the new one
            size_t rand_index = get_rand_index();
            if (rand_index < reservoir_.size()) {
                reservoir_[rand_index] = observation;
            }
        }
    }
    void print_sample() {
        fmt::println("{}", fmt::join(reservoir_, ", "));
    }
};

int main() {
    fmt::println("Hello, world!");

    auto res = Reservoir<int>(4);
    res.add(10);
    res.add(7);
    res.add(3);
    res.add(6);
    res.add(2);
    res.add(8);
    res.add(9);
    res.add(1);
    res.add(4);
    res.add(5);
    res.add(11);
    res.print_sample();
}
