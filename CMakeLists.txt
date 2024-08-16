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

file(GLOB_RECURSE files "*.cpp")
foreach(file ${files})
    get_filename_component(EXAMPLE_NAME ${file} NAME_WE)
    add_executable(${EXAMPLE_NAME} ${file})
    target_compile_features(${EXAMPLE_NAME} PUBLIC cxx_std_20) # set C++ standard
    target_link_libraries(${EXAMPLE_NAME} samarium::samarium)
endforeach()

# TODO for now not using this, just running it thru python
if(CURRENT_EXAMPLE)
    add_custom_target(
        run ALL
        COMMAND example
        DEPENDS example
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        USES_TERMINAL
    )
endif()

# conan creates its own preset...but cmake gives error deuplicate preset: default
file(REMOVE CMakeUserPresets.json)