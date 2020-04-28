

## CMake에서 라이브러리 링크하는 방법

### 1. `find_package()`로 라이브러리 찾기

`find_package()`가 특정 경로에 있는 라이브러리 패키지를 찾도록 경로를 알려주는 방법은 두 가지 방법이 있다. 여기서 알려줘야 할 경로는 `<package_name>Config.cmake` 파일이 있는 경로다.

1. `CMAKE_PREFIX_PATH` 에 경로 추가

   ```cmake
   set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} some/path/to/lib)
   ```

2. `<package_name>_DIR` 변수 추가

   ```cmake
   set(<package_name>_DIR some/path/to/lib)
   ```



### 2. 라이브러리 경로 추가하기

```cmake
include_directories(${<package_name>_INCLUDE_DIRS})
link_directories(${<package_name>_LIBRARY_DIRS})
```



### 3. 라이브러리 링크하기

```cmake
target_link_libraries(<target_name> 
    ${<package_name>_LIBRARIES} 
)
```







