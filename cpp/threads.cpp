#include <iostream>
#include <thread>
#include <atomic>
#include <vector>

const int N_THREADS = 10;

void count(std::atomic<int>& counter) {
    for (int i = 0; i < 1'000'000; ++i) {
        counter++;
    }
}


int main() {
    std::atomic<int> counter(0);
    
    std::vector<std::thread> threads;
    // spawn n threads:
    for (int i = 0; i < N_THREADS; ++i) {
        threads.emplace_back(std::thread(count, std::ref(counter)));
    }

    // Wait for all threads to finish
    for (auto& thread : threads) {
        thread.join();
    }

    std::cout << "Counter value: " << counter << std::endl;
}