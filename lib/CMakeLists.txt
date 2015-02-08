# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND aes_sources
)

set(aes_sources "${aes_sources}" PARENT_SCOPE)
if(NOT aes_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT aes_sources)

add_library(gnuradio-aes SHARED ${aes_sources})
target_link_libraries(gnuradio-aes ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-aes PROPERTIES DEFINE_SYMBOL "gnuradio_aes_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-aes PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-aes
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_aes_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_aes.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_aes.cc
)

add_executable(test-aes ${test_aes_sources})

target_link_libraries(
  test-aes
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-aes
)

GR_ADD_TEST(test_aes test-aes)
