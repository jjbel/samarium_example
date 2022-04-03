cmake_minimum_required(VERSION 3.16) # At least CMake-3.16 is required
project(SamariumExample CXX) # Create Project

# Get deps using Conan
execute_process(
    COMMAND conan install . -b missing -if build
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    OUTPUT_QUIET
)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) # include Conan
conan_basic_setup(TARGETS) # setup Conan

add_executable(example example.cpp) # create an example executable

target_compile_features(example PUBLIC cxx_std_20) # set C++ standard
target_link_libraries(example CONAN_PKG::samarium) # use project

# GCC requires libTBB for std::execution
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    find_package(TBB REQUIRED)
    target_link_libraries(example TBB::tbb)
endif()

# enable running the example with ctest
include(CTest)
enable_testing()
add_test(NAME example COMMAND example)
