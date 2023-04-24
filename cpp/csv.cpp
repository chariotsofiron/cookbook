#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>
#include "string_.cpp"

int main() {
    std::string filename{"csv_file.txt"};
    std::ifstream input{filename};

    if (!input.is_open()) {
        std::cerr << "Couldn't read file: " << filename << "\n";
        return EXIT_FAILURE;
    }

    std::vector<std::vector<std::string>> csv_rows;
    for (std::string line; std::getline(input, line);) {
        csv_rows.push_back(split_string(line, ','));
    }

    // Print out our table
    for (const std::vector<std::string>& row : csv_rows) {
        for (const std::string& value : row) {
            std::cout << std::setw(10) << value;
        }
        std::cout << "\n";
    }
}