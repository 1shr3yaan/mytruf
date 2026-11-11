
import unittest
from analyze import analyze_password


class TestPasswordAnalyzer(unittest.TestCase):

    def test_empty_password(self):
        result = analyze_password("")
        self.assertIsInstance(result, dict)

    def test_common_password(self):
        result = analyze_password("password123")
        self.assertLess(result["score"], 50)

    def test_long_password(self):
        result = analyze_password("Tr0ub4dor&Example!92")
        self.assertGreaterEqual(result["score"], 80)

    def test_result_contains_required_fields(self):
        result = analyze_password("Hello1234!Example")
        self.assertIn("score", result)
        self.assertIn("rating", result)
        self.assertIn("entropy", result)
        self.assertIn("findings", result)
        self.assertIn("recommendations", result)


if __name__ == "__main__":
    unittest.main()
