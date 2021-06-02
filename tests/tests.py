import unittest

from translator import englishtofrench

class TestEnglishToFrench(unittest.TestCase):
    def testNull(self): 
        self.assertEqual(englishtofrench(None), 'text must be provided') # test when None is given as input the output is 'text must be provided'.
    def testHello(self): 
        self.assertEqual(englishtofrench('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
    def testFrench(self): 
        self.assertEqual(englishtofrench('French'), 'Français') # test when 'French' is given as input the output is 'Français'.
