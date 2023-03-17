#include <iostream>  // cout, endl
#include <string>    // std::string

// convert string to integer
auto convert_string_to_int(std::string_view str) -> int {
    try {
        return std::stoi(std::string(str));
    } catch (std::invalid_argument const& e) {
        std::cerr << "Invalid argument: " << e.what() << '\n';
    } catch (std::out_of_range const& e) {
        std::cerr << "Out of Range error: " << e.what() << '\n';
    }
}