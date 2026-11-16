"""Live-service tests of the five emotion examples required by the lab."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify dominant emotions returned by the real Watson NLP service."""

    def test_joy(self):
        """Recognize joy."""
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    def test_anger(self):
        """Recognize anger."""
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

    def test_disgust(self):
        """Recognize disgust."""
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Recognize sadness."""
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

    def test_fear(self):
        """Recognize fear."""
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
