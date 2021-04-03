#!/usr/bin/env python
import unittest

from lww.LWWPlainValueMap import LWWPlainValueMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWPlainValueMapTests(unittest.TestCase):

    def testAddAndQueryEntries(self):
        lwwMap = LWWPlainValueMap()
        
        key1 = "name"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        
        self.assertTrue(lwwMap.lookup(key1))
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.size(), 1)
        
        key2 = "profession"
        value2 = "researcher"
        lwwMap.add(key2, value2, 20)
        
        self.assertEqual(lwwMap.query(key2), value2)
        self.assertEqual(lwwMap.size(), 2)
    
    def testAddingWithExistingKeyIsProcessedButNotExistsImmediately(self):
        lwwMap = LWWPlainValueMap()
        
        key1 = "name"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.size(), 1)
        
        value2 = "David"
        lwwMap.add(key1, value2, 20)
        self.assertEqual(lwwMap.query(key1), value2)
        self.assertEqual(lwwMap.size(), 1)
        
    def testRemoveAndQueryEntry(self):
        lwwMap = LWWPlainValueMap()
        
        key1 = "name"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.size(), 1)
        
        lwwMap.remove(key1, 30)
        self.assertFalse(lwwMap.lookup(key1), value1)
        self.assertEqual(lwwMap.size(), 0)

    def testIterateOverEntries(self):
        lwwMap = LWWPlainValueMap()
        
        key1 = "firstName"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        key2 = "lastName"
        value2 = "David"
        lwwMap.add(key2, value2, 20)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.query(key2), value2)
        self.assertEqual(lwwMap.size(), 2)
        
        entrySet = lwwMap.entrySet()
        
        entriesVisited = 0
        for (key, value), _ in entrySet:
            if(key == key1):
                self.assertEqual(value, value1)
                entriesVisited += 1
            elif(key == key2):
                self.assertEqual(value, value2)
                entriesVisited += 1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 2)
                
        key3 = "profession"
        value3 = "researcher"
        lwwMap.add(key3, value3, 30)
        
        entriesVisited = 0
        for (key, value), _ in entrySet:
            if(key == key1):
                self.assertEqual(value, value1)
                entriesVisited += 1
            elif(key == key2):
                self.assertEqual(value, value2)
                entriesVisited += 1
            elif(key == key3):
                self.assertEqual(value, value3)
                entriesVisited += 1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 3)
        
    def testIterateOverKeys(self):
        lwwMap = LWWPlainValueMap()
        
        key1 = "firstName"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        key2 = "lastName"
        value2 = "David"
        lwwMap.add(key2, value2, 20)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.query(key2), value2)
        self.assertEqual(lwwMap.size(), 2)
        
        keySet = lwwMap.keySet()
        
        entriesVisited = 0
        for key in keySet:
            if(key == key1):
                self.assertEqual(lwwMap.query(key), value1)
                entriesVisited += 1
            elif(key == key2):
                self.assertEqual(lwwMap.query(key), value2)
                entriesVisited += 1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 2)

    """
    def testRemoveNotexisting(self):
        lwwMap = LWWPlainValueMap()
        
        self.assertRaises(KeyError, lwwMap.remove, "key", 10)
    """


if __name__ == "__main__":
    unittest.main()