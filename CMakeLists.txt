cmake_minimum_required(VERSION 3.16) # At least CMake-3.16 is required
project(SamariumExample CXX) # Create Project

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # include Conan
conan_basic_setup(TARGETS) # setup Conan

add_executable(example example.cpp)

target_compile_features(example PUBLIC cxx_std_20) # set C++ standard
target_link_libraries(example CONAN_PKG::samarium) # use project
