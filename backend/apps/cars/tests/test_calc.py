from unittest import TestCase
from unittest.mock import MagicMock, patch

from apps.cars.services import calc, math


class CalcTestCase(TestCase):
    @patch.object(math, 'cos')
    def test_add(self, mock_math: MagicMock):
        mock_math.return_value = 15
        res = calc(3, 2, '+')
        self.assertEqual(res, 20)
        self.assertEqual(mock_math.call_count, 1)

    @patch('apps.cars.services.sqrt')
    def test_mul(self, mock_sqrt: MagicMock):
        mock_sqrt.return_value = 1
        res = calc(3, 2, '*')
        self.assertEqual(res, 7)
        self.assertEqual(mock_sqrt.call_count, 1)

    def test_sub(self):
        res = calc(3, 2, '-')
        self.assertEqual(res, 1)