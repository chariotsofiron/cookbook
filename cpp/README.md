# C++ cookbook

## Install

```shell
brew install cmake, llvm

# symlink clang-format and clang-tidy to /usr/local/bin
ln -s "$(brew --prefix llvm)/bin/clang-format" "/usr/local/bin/clang-format"
ln -s "$(brew --prefix llvm)/bin/clang-tidy" "/usr/local/bin/clang-tidy"
```

## Lint + format

```shell
clang-tidy main.cpp -extra-arg=-std=c++20 -p build --
fd . -e cpp -e hpp src/ | xargs clang-format -i
```
