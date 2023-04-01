#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <string>

template <typename T>
std::vector<T> depth_first_search(std::unordered_map<T, std::vector<T> > map, T start) {
    std::unordered_set<T> visited;
    std::vector<T> result;
    std::vector<T> stack = {start};

    while (!stack.empty()) {
        T current = stack.back();
        stack.pop_back();
        if (visited.find(current) == visited.end()) {
            visited.insert(current);
            result.push_back(current);
            for (T next : map[current]) {
                stack.push_back(next);
            }
        }
    }
    return result;
}

int main() {
    auto map = std::unordered_map<char, std::vector<char> >() = {
        {'a', {'b', 'c'}},
        {'b', {'a', 'd', 'e'}},
        {'c', {'a', 'f'}},
        {'d', {'b'}},
        {'e', {'b', 'f'}},
        {'f', {'c', 'e'}}
    };

    auto result = depth_first_search(map, 'a');
    std::vector<char> expected = {'a', 'c', 'f', 'e', 'b', 'd'};
    assert(result == expected);

    for (auto c : result) {
        std::cout << c << " ";
    }
    std::cout << std::endl;
}