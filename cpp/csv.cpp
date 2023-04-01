#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

int main() {
    std::string filename{"csv_file.txt"};
    std::ifstream input{filename};

    if (!input.is_open()) {
        std::cerr << "Couldn't read file: " << filename << "\n";
        return EXIT_FAILURE;
    }

    std::vector<std::vector<std::string>> csv_rows;
    for (std::string line; std::getline(input, line);) {
        std::istringstream ss(std::move(line));
        std::vector<std::string> row;
        if (!csv_rows.empty()) {
            // We expect each row to be as big as the first row
            row.reserve(csv_rows.front().size());
        }
        // std::getline can split on other characters, here we use ','
        for (std::string value; std::getline(ss, value, ',');) {
            row.push_back(std::move(value));
        }
        csv_rows.push_back(std::move(row));
    }

    // Print out our table
    for (const std::vector<std::string>& row : csv_rows) {
        for (const std::string& value : row) {
            std::cout << std::setw(10) << value;
        }
        std::cout << "\n";
    }
}