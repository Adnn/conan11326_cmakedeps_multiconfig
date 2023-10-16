cmake_minimum_required(VERSION 3.15)

# set the project name and version
project(Downstream VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(TARGET_NAME "myapp")

add_executable(${TARGET_NAME} main.cpp)

find_package(Internal REQUIRED)

target_link_libraries(${TARGET_NAME} PRIVATE ad::internal)

# make cache variables for install destinations
include(GNUInstallDirs)

# add the install targets
install(TARGETS ${TARGET_NAME})
