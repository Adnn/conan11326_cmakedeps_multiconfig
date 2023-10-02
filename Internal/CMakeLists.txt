cmake_minimum_required(VERSION 3.15)

# set the project name and version
project(Internal VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(TARGET_NAME "internallib")

add_library(${TARGET_NAME} Add.cpp)

# list public headers
set_target_properties(${TARGET_NAME} PROPERTIES PUBLIC_HEADER Add.h)

# make cache variables for install destinations
include(GNUInstallDirs)

# add the build tree or install tree to the include directories
target_include_directories(
    ${TARGET_NAME}
    PUBLIC
        "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>"
        "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>")


# add the install targets
install(
    TARGETS ${TARGET_NAME}
    EXPORT ${PROJECT_NAME}Targets
    PUBLIC_HEADER
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${TARGET_NAME})

# install the exported targets
install(
    EXPORT ${PROJECT_NAME}Targets
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
    NAMESPACE ad::)

include(CMakePackageConfigHelpers)

# TODO Generate version file for the config file
#write_basic_package_version_file(
#  "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfigVersion.cmake"
#  VERSION "${Tutorial_VERSION_MAJOR}.${Tutorial_VERSION_MINOR}"
#  COMPATIBILITY AnyNewerVersion

# generate the config file that includes the exports
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME})

# install the config and version files
install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
        #"${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME})

# TODO Generate the export targets from the build tree
## needs to be after the install(TARGETS) command
#export(EXPORT MathFunctionsTargets
#  FILE "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsTargets.cmake"
#)
#
