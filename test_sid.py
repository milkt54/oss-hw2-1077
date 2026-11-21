import unittest
from sid import digit_sum, lucky_number

MY_SID4 = 1234  # 본인 SID4 (앞자리 0이면 제거, 예: 0705 -> 705)

class TestSid(unittest.TestCase):
    def test_digit_sum(self):
        self.assertEqual(digit_sum(1234), 10)

    def test_lucky_number(self):
        self.assertEqual(lucky_number(1234), 1)

    def test_my_sid(self):
        self.assertEqual(lucky_number(1077), 6)  # 본인 학번 끝 4자리의 한 자리 반복 합으로 수정
