from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase(TestCase):
    def test_empty(self):
        self.assertEqual(solution("din"),"(((")
    def test_basic(self):
        self.assertEqual(solution("recede"),"()()()")
    def test_single(self):
        self.assertEqual(solution("Success"),")())())","should ignore case")
    def test_multi(self):
        self.assertEqual(solution("(( @"),"))((")



if __name__ == '__main__':
    main()