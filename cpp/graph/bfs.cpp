#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <string>

template <typename T>
std::vector<T> breadth_first_search(std::unordered_map<T, std::vector<T> > map, T start) {
    std::unordered_set<T> visited;
    std::vector<T> result;
    std::vector<T> queue = {start};

    while (!queue.empty()) {
        T current = queue.front();
        queue.erase(queue.begin());
        if (visited.find(current) == visited.end()) {
            visited.insert(current);
            result.push_back(current);
            for (T next : map[current]) {
                queue.push_back(next);
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

    auto result = breadth_first_search(map, 'a');
    std::vector<char> expected = {'a', 'b', 'c', 'd', 'e', 'f'};
    assert(result == expected);
}