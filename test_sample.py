
import unittest

class MyTest(unittest.TestCase):

    #defind result variable to store the test results
    result = None


    def setUp(self):
        pass

    def tearDown(self):

        passed = self.result.wasSuccessful()
        err = self.result.errors
        failed = self.result.failures
        print (' Test passed' if passed else \
                ' %d errors and %d failures' % \
                (len(err), len(failed)))

    def run(self, result=None):
        self.result = result # save the result
        unittest.TestCase.run(self, result)


    def testEquals(self):
        self.assertEqual(10, 10) # pass

    def testNotEqualNum(self):
        self.assertEqual(1, 0) #fail

    def testTrue(self):
        self.assertTrue(10 * 7 == 70) #pass



if __name__ == '__main__':
    unittest.main()
