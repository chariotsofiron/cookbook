#include <vector>

bool valid_rows(const std::vector<std::vector<char>>& board) {
    for (const auto& row : board) {
        for (auto x : row) {
            if (x != '.') {
                continue;
            }
            for (auto y : row) {
                if (y != '.' && x == y) {
                    return false;
                }
            }
        }
    }
    return true;
}

bool valid_cols(const std::vector<std::vector<char>>& board) {
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (board[i][j] != '.') {
                continue;
            }
            for (int k = 0; k < 9; ++k) {
                if (board[k][j] != '.' && board[i][j] == board[k][j]) {
                    return false;
                }
            }
        }
    }
    return true;
}


bool is_valid_sudoku(std::vector<std::vector<char>>) {
    return true;
}

int main() {
    std::vector<std::vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
}