import unittest
import avg

class averageTestCase(unittest.TestCase):

    def test_average(self):
        answer = avg.compute_average([1, 2, 3, 4, 5])
        self.assertEqual(answer, 3.0)
    
    def test_empty_input_average(self):
        answer = avg.compute_average([])
        self.assertEqual(answer, 0)

    def test_float_input_number(self):
        self.assertEqual(avg.compute_average([2.7, 2.8, 4.8, 4.9]), 3)

if __name__ == "__main__":
    unittest.main()

