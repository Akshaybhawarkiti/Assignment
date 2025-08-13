cmake_minimum_required(VERSION 3.20)
project(bt_demo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(behaviortree_cpp_DIR "C:/vcpkg/installed/x64-windows/share/behaviortree_cpp")
# This will find the BehaviorTree.CPP installed via vcpkg
find_package(behaviortree_cpp CONFIG REQUIRED)

add_executable(bt_main main.cpp)
target_link_libraries(bt_main PRIVATE BT::behaviortree_cpp)
