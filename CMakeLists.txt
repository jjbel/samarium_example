cmake_minimum_required(VERSION 3.16) # At least CMake-3.16 is required

# Install deps using Conan
execute_process(
    COMMAND conan install . -b missing -if ${CMAKE_BINARY_DIR} -pr default -pr:b default
            -s build_type=${CMAKE_BUILD_TYPE}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_BINARY_DIR}/conan_toolchain.cmake)

project(SamariumExample CXX) # Create Project

find_package(samarium CONFIG REQUIRED)

add_executable(example example.cpp) # create an example executable

target_compile_features(example PUBLIC cxx_std_20) # set C++ standard
target_link_libraries(example samarium::samarium) # use project

add_custom_target(
    run ALL
    COMMAND example
    DEPENDS example
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    USES_TERMINAL
)
