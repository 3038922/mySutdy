#设置最低的编译版本
cmake_minimum_required(VERSION 3.10)
#项目名称
project(clangStuady)
#设置c/c++标准
set(CMAKE_C_STANDARD 11)#C11
set(CMAKE_CXX_STANDARD 17)#C17
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_compile_options(-Wno-unused-variable -Wno-unused-function)
#是谁就改成谁
set(name "cow")
#头文件路径
INCLUDE_DIRECTORIES("./include/")
#枚举头文件
file(GLOB_RECURSE INCLUDES "./include/*.h" "./include/*.hpp" "./userSrc/${name}/*.h" "./userSrc/${name}/*.hpp")
#枚举源文件
file(GLOB_RECURSE SOURCES "./userSrc/${name}/*.c" "./userSrc/${name}/*.cpp" "./include/lv_examples/*.c")
#加入一些-D
#ADD_DEFINITIONS () 

#PROJECT_SOURCE_DIR 这是项目路径
#PROJECT_BINARY_DIR 这是build里面的文件夹
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin) #设置二进制文件存放路径 
SET(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/firmware) #设置各种库存放路径

#要建立的静态库
#file(GLOB_RECURSE LIBLVGL "./include/lvgl/*.c")
#file(GLOB_RECURSE LIBDRIVERS "./include/lv_drivers/*.c")
#file(GLOB_RECURSE LIBRESOURCES "./src/system/ncr_font10.c" "./src/system/logo.c" "./src/system/field.c")
# add_library(linuxlvgl STATIC ${LIBLVGL})
# add_library(linuxdrivers STATIC ${LIBDRIVERS})
#add_library(resources STATIC ${LIBRESOURCES})

# #添加需要链接的库文件目录 新建好了 链接的时候用
LINK_DIRECTORIES(${LIBRARY_OUTPUT_PATH})

IF(WIN32)
    message("the system is windows")
    include_directories(${SDL2_INCLUDE_DIRS})
    #生成可执行文件
    add_executable(main ${SOURCES} ${INCLUDES})
    #链接SDL2的静态库
    target_link_libraries(main  SDL2 SDL2main lvgl drivers)#不链接pthread easylog编译报错
ELSEIF(UNIX)
    message("the system is linux")
    #寻找sdl2
    find_package(SDL2 REQUIRED SDL2)
    include_directories(${SDL2_INCLUDE_DIRS})
    #生成可执行文件
    add_executable(main ${SOURCES} ${INCLUDES})
    target_link_libraries(main PRIVATE SDL2 liblinuxlvgl.a liblinuxdrivers.a  pthread)#不链接pthread easylog编译报错
ENDIF(WIN32)
#添加一个run命令
add_custom_target (run COMMAND ninja all  COMMAND ${EXECUTABLE_OUTPUT_PATH}/main)

