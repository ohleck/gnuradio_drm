#!/usr/bin/env python
# 
# Copyright 2012 Communications Engineering Lab (CEL) / KIT (Karlsruhe Institute of Technology) 
# Author: Felix Wunsch
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
#

from gnuradio import gr, gr_unittest
#import drm_swig
import drm

class qa_interleaver_vbvb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()
        self.src = gr.vector_source_b((0,1,2,3,4,5,6,7,8,9), True, 10)
        self.head = gr.head(10,2)
        seq = (3,7,5,8,6,1,9,4,2,0)
        self.interleaver = drm.interleaver_vbvb(seq)
        self.snk = gr.vector_sink_b(10)
        
        self.tb.connect(self.src, self.head, self.interleaver, self.snk)

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        res = self.snk.data()
        # check data
        ref = (3,7,5,8,6,1,9,4,2,0,3,7,5,8,6,1,9,4,2,0)
        print "res:", res
        print "ref:", ref
        self.assertTupleEqual(res, ref)


if __name__ == '__main__':
    gr_unittest.main ()
