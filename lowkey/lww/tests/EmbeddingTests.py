#!/usr/bin/env python
import unittest

from lww.LWWRegister import LWWRegister
from lww.LWWPlainValueSet import LWWPlainValueSet

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class EmbeddingTests(unittest.TestCase):

    def testEmbedRegisterInRegister(self):
        base = LWWRegister()
        embedded = LWWRegister()
        
        value = "hello"
        
        embedded.update(value, 10)
        base.update(embedded, 20)
        
        retrievedEmbedded = base.query()    
        self.assertTrue(retrievedEmbedded)
        self.assertTrue(isinstance(retrievedEmbedded, LWWRegister))
        
        self.assertTrue(retrievedEmbedded.query())
        self.assertEqual(retrievedEmbedded.query(), value)
        self.assertTrue(isinstance(retrievedEmbedded.query(), str))
        
    def testEmbedSetInRegister(self):
        base = LWWRegister()
        embedded = LWWPlainValueSet()
                
        value = "element1"
        
        embedded.add(value, 10)
        base.update(embedded, 20)
        
        retrievedEmbedded = base.query()
        self.assertTrue(retrievedEmbedded)
        self.assertTrue(isinstance(retrievedEmbedded, LWWPlainValueSet))        
        self.assertTrue(retrievedEmbedded.lookup(value))
        
    def testEmbedRegisterInSet(self):
        base = LWWPlainValueSet()
        embedded = LWWRegister()
                
        value = "element1"
        embedded.update(value, 10)
        base.add(embedded, 20)
        
        self.assertTrue(base.lookup(embedded))
        
    def testEmbedSetInSet(self):
        base = LWWPlainValueSet()
        embedded = LWWPlainValueSet()
                
        value = "element1"
        
        embedded.add(value, 10)
        base.add(embedded, 20)
        
        self.assertTrue(base.lookup(embedded))
        
        newValue = "element2"
        embedded.add(newValue, 30)
        
        self.assertTrue(base.lookup(embedded))
        self.assertTrue(embedded.lookup(value))
        self.assertTrue(embedded.lookup(newValue))


if __name__ == "__main__":
    unittest.main()
