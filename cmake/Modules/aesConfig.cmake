INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_AES aes)

FIND_PATH(
    AES_INCLUDE_DIRS
    NAMES aes/api.h
    HINTS $ENV{AES_DIR}/include
        ${PC_AES_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    AES_LIBRARIES
    NAMES gnuradio-aes
    HINTS $ENV{AES_DIR}/lib
        ${PC_AES_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(AES DEFAULT_MSG AES_LIBRARIES AES_INCLUDE_DIRS)
MARK_AS_ADVANCED(AES_LIBRARIES AES_INCLUDE_DIRS)

