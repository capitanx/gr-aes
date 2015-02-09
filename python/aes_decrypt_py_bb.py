#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

# GNURadio
import numpy
from gnuradio import gr

# AES
from Crypto.Cipher import AES
from Crypto import Random

# SHA-256 and MD5
import hashlib


class aes_decrypt_py_bb(gr.sync_block):
    """
    AES Decrypt block
    """
    def __init__(self, key, iv, mode):
        self.key  = key
        self.iv   = iv
        self.mode = mode
        gr.sync_block.__init__(self,
            name="aes_decrypt_py_bb",
            in_sig=[numpy.uint8],
            out_sig=[numpy.uint8])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        cipher = AES.new(self.key, self.mode, self.iv)
        out[:] = map( ord, cipher.decrypt(in0) )

        return len(output_items[0])

