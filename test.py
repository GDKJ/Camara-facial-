import unittest


class Test_test_1(unittest.TestCase):
    def test_usuario(self):
        long=len('estuardo')
        self.assertTrue(long>5 and long<13 )
        #self.fail("Not implemented")

class Test_test_2(unittest.TestCase):
    def test_usuario(self):
        long=len('ana')
        self.assertFalse(long>5 and long<13 )
        #self.fail("Not implemented")

class Test_test_3(unittest.TestCase):
    def test_usuario(self):
        y='gary89-'.isalnum()   
        self.assertFalse(y== True)
        #self.fail("Not implemented")

class Test_test_4(unittest.TestCase):
    def test_passw(self):
        long=len('Flor12-a')
        self.assertTrue(long >=8)
        #self.fail("Not implemented")

class Test_test_5(unittest.TestCase):
    def test_passw(self):
        y='Flor12a'.isalnum()   
        self.assertTrue(y==False)
        #self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
