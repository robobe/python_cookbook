```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv/opencv_contrib/modules \
    -D BUILD_EXAMPLES=OFF \
    -D WITH_TIFF=OFF \
    -D BUILD_JAVA=OFF \
    -D BUILD_opencv_java_bindings_generator=OFF \
    -D BUILD_opencv_xfeatures2d=ON \
    -D CPACK_BINARY_DEB=ON \
    -D CPACK_SOURCE_ZIP=ON \
    -D BUILD_opencv_python=OFF \
    -D WITH_V4L=OFF \
    -D WITH_LIBV4L=ON \
    ..
```