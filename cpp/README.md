# C++ cookbook

## Install

```shell
brew install cmake, llvm

# symlink clang-format and clang-tidy to /usr/local/bin
ln -s "$(brew --prefix llvm)/bin/clang-format" "/usr/local/bin/clang-format"
ln -s "$(brew --prefix llvm)/bin/clang-tidy" "/usr/local/bin/clang-tidy"
```


## Build

```shell
cmake -S . -B build
cmake --build build
```

## Run

```shell
./build/main
```

## Lint + format

