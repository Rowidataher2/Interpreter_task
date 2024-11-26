import unittest
from processing.processing_engine import ProcessingEngine

class Testprocessing(unittest.TestCase):
    def test_basic_arithmetic(self):
        message = {"value": 100}

        engine = ProcessingEngine("ATTR + 50 * (ATTR / 10)")
        result = engine.process_message(message)
        self.assertEqual(result, 600.0)

    def test_matching_regex_equation(self):
        message = {"value": "dog1"}
        engine = ProcessingEngine("Regex(ATTR, '^dog')")
        result = engine.process_message(message)
        self.assertTrue(result)

    def test_non_matching_regex(self):
        message = {"value": "cat"}
        engine = ProcessingEngine("Regex(ATTR, '^dog')")
        result = engine.process_message(message)
        self.assertFalse(result)


