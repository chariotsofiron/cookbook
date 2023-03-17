
# Install

```shell
brew install cmake, llvm

# symlink clang-format and clang-tidy to /usr/local/bin
ln -s "$(brew --prefix llvm)/bin/clang-format" "/usr/local/bin/clang-format"
ln -s "$(brew --prefix llvm)/bin/clang-tidy" "/usr/local/bin/clang-tidy"
```


# Build

```shell
clang++ main.cpp -std=c++17 -Wall -Wextra -Wpedantic
```

# Run

# Lint + format



# Debug