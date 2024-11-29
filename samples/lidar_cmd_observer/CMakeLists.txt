cmake_minimum_required(VERSION 3.21 FATAL_ERROR)

set(DEMO_NAME lidar_cmd_observer)
add_executable(${DEMO_NAME} main.cpp)

target_include_directories(
        ${DEMO_NAME}
        PRIVATE
        ../../3rdparty/
        )

target_link_libraries(${DEMO_NAME}
        PUBLIC
        livox_lidar_sdk_static
				)

target_compile_options(${DEMO_NAME} PRIVATE ${SDK_EXAMPLE_COMPILE_OPTIONS})
target_link_options(${DEMO_NAME} PRIVATE ${SDK_EXAMPLE_COMPILE_OPTIONS})