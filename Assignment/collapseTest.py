import unittest
import Assignment.collapse as collapse

class CollapseTest(unittest.TestCase):

# Happy path:  nominal value within bounds
    def test100_010_ShouldCollapseOneGoodDigit(self):
        value = '5'
        expectedResult = '5'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)

    def test_ShouldCollapseOneGoodDigit(self):
        value = '0'
        expectedResult = '0'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldCollapseTwoGoodDigits(self):
        value = '10'
        expectedResult = '1'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldCollapseThreeGoodDigits(self):
        value = '123'
        expectedResult = '6'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldCollapseTwoSameGoodDigits(self):
        value = '99'
        expectedResult = '9'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldCollapseFiveGoodDigits(self):
        value = '98769'
        expectedResult = '3'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldNotCollapseZeroGoodDigits(self):
        value = ''
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldNotCollapseOneBadDigits(self):
        value = 'a'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldNotCollapseValueBelowZero(self):
        value = '-1'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test_ShouldNotCollapseWithoutParentheses(self):
        value = 1
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)