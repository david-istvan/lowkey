#!/usr/bin/env python
import unittest

from lowkey.lww.LWWEdge import LWWEdge
from lowkey.lww.LWWVertex import LWWVertex
from lowkey.lww.LWWMap import LWWMap
from lowkey.lww.tests.LWWMapTests import LWWMapTests

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWGraphPartsTests(LWWMapTests):
    
    def testLWWVertexCompatibility(self):
        self.lwwMap = LWWVertex()
        self.assertTrue(issubclass(type(self.lwwMap), LWWMap))
        
    def testLWWEdgeCompatibility(self):
        self.lwwMap = LWWEdge()
        self.assertTrue(issubclass(type(self.lwwMap), LWWMap))


if __name__ == "__main__":
    unittest.main()
