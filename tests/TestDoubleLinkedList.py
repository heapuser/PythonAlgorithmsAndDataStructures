import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from PythonAlgorithmsAndDataStructures.DoubleLinkedList import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):  
    def testInit(self):
        self.dll=DoubleLinkedList()
        self.assertEqual(self.dll.head,None)
        self.assertEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),0)
        
    def testAppendAndRemove(self):
        self.dll=DoubleLinkedList()
        
        self.dll.append(1)
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),1)  
        self.dll.append('Hello')
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),2)        
        self.dll.append((10,11))
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),3)
        self.dll.append({1:'a',2:'b'})
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),4)
        self.dll.append(1)
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),5)
        self.dll.append([1,2,3,4,5])
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),6)
        self.dll.append(1)
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),7)
        
        self.dll.remove(1)
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),4)        
        self.dll.remove('Hello')
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),3)
        self.dll.remove({1:'a',2:'b'})
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),2)
        self.dll.remove([1,2,3,4,5])
        self.assertNotEqual(self.dll.head,None)
        self.assertNotEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),1)

        self.dll.remove((10,11))
        self.assertEqual(self.dll.head,None)
        self.assertEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),0)
        self.dll.remove((10,11))

        self.assertEqual(self.dll.head,None)
        self.assertEqual(self.dll.tail,None)
        self.assertEqual(self.dll.length(),0)

    def testPrint(self):
        self.dll=DoubleLinkedList()
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.show(),'1 <-> 2 <-> 3')
        
    def testPerf(self):
        self.dll=DoubleLinkedList()
        for i in range(1000):
            self.dll.append(i)
        for i in range(1000):
            self.dll.remove(i)
        self.assertEqual(self.dll.length(),0)
        
if __name__=='__main__':
    unittest.main()
    
