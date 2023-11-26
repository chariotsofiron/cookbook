### Frontmatter
cmake_minimum_required(VERSION 3.25.0)
project(main)
set(CMAKE_CXX_STANDARD 17)


## Compiler options
add_compile_options(
    # Reasonable and standard
    -Wall
    -Wextra
    # Others
    -Wpedantic
    -Wshadow
    -Wold-style-cast
    -Weffc++
    -Wformat
    -Wconversion
    -Wuninitialized
    # # Debug
    # -g
    # -fsanitize=address,undefined,integer
)


## Executable
add_executable(${PROJECT_NAME} randomized/reservoir_sampling.cpp)


## Dependencies
include(FetchContent)
FetchContent_Declare(fmt
  GIT_REPOSITORY https://github.com/fmtlib/fmt.git
  GIT_TAG master
)
FetchContent_MakeAvailable(fmt)
target_link_libraries(${PROJECT_NAME} PRIVATE fmt::fmt)
