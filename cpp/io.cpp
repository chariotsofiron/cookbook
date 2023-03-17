#include <fstream>   // std::ifstream
#include <iostream>  // cout, endl
#include <sstream>   // std::stringstream
#include <string>    // std::string

auto read_file_to_string(std::string_view path) -> std::string {
    std::ifstream file(path);
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}


auto get_input_from_stdin() -> std::string {
    std::string input;
    // uses newline as delimiter (cin uses any whitespace)
    std::getline(std::cin, input);
    return input;
}

auto main() -> int {
    // std::string text = read_file_to_string();
    // std::cout << text;
    std::cout << "Hello, World!" << std::endl;
}