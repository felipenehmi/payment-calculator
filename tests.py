import sys
import unittest
from contextlib import contextmanager
from main import main
from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class CalculatorTest(unittest.TestCase):

    def test_success(self):
        with captured_output() as (out, err):
            main(["", "entries/entry_valid.txt"])

        output = out.getvalue().strip()
        self.assertTrue(
            "The amount to pay to ASTRID is: 85\n" +
            "The amount to pay to RENE is: 215\n" +
            "The amount to pay to FELIPE is: 315\n" +
            "The amount to pay to JOHN is: 360\n" +
            "The amount to pay to LUCAS is: 330" in output
        )

    def test_invalid_input(self):
        with captured_output() as (out, err):
            main(["", "entries/entry_invalid_format.txt"])

        output = out.getvalue().strip()
        self.assertTrue(
            "Invalid Input: LUCAS=MO08:00-14:00,TH01:00-05:00,TU08:00-16:XX" in output
        )

    def test_invalid_hour_range(self):
        with captured_output() as (out, err):
            main(["", "entries/entry_invalid_range.txt"])

        output = out.getvalue().strip()
        self.assertTrue(
            "Invalid hour range: MO10:00-10:00,TH12:00-14:00,SU20:00-21:00" in output
        )


if __name__ == '__main__':
    unittest.main()
