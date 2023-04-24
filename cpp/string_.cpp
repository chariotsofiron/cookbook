#include <string>
#include <vector>
#include <string_view>

std::vector<std::string> split_string(std::string_view str, char delimiter) {
    std::vector<std::string> tokens;
    std::size_t start = 0;
    std::size_t end = str.find(delimiter);

    while (end != std::string_view::npos) {
        tokens.push_back(std::string(str.substr(start, end - start)));
        start = end + 1;
        end = str.find(delimiter, start);
    }

    tokens.push_back(std::string(str.substr(start)));

    return tokens;
}