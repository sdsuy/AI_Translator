import unittest

from translator import englishtofrench, englishtogerman

class TestEnglishToFrench(unittest.TestCase):
    def testNull(self): 
        self.assertEqual(englishtofrench(None), 'text must be provided') # test when None is given as input the output is 'text must be provided'.
    def testHello(self): 
        self.assertEqual(englishtofrench('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
    def testFrench(self): 
        self.assertEqual(englishtofrench('French'), 'Français') # test when 'French' is given as input the output is 'Français'.

class TestEnglishToGerman(unittest.TestCase):
    def testNull(self): 
        self.assertEqual(englishtogerman(None), 'text must be provided') # test when None is given as input the output is 'text must be provided'.
    def testHello(self): 
        self.assertEqual(englishtogerman('Hello'), 'Hallo') # test when 'Hello' is given as input the output is 'Hallo'.
    def testGerman(self): 
        self.assertEqual(englishtogerman('German'), 'Deutsch') # test when 'German' is given as input the output is 'Deutsch'.
