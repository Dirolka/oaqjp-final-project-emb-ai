"""Offline contract tests; these do not claim to test Watson classification."""
import unittest
from unittest.mock import patch, Mock
import requests
from EmotionDetection import emotion_detector
from server import app

class OfflineTests(unittest.TestCase):
    def test_http_400(self):
        with patch('EmotionDetection.emotion_detection.requests.post', return_value=Mock(status_code=400)):
            self.assertEqual(emotion_detector(''), dict.fromkeys(('anger','disgust','fear','joy','sadness','dominant_emotion')))
    def test_format(self):
        response=Mock(status_code=200,text='{"emotionPredictions":[{"emotion":{"anger":0.1,"disgust":0.2,"fear":0.3,"joy":0.9,"sadness":0.1}}]}')
        with patch('EmotionDetection.emotion_detection.requests.post',return_value=response):
            self.assertEqual(emotion_detector('test')['dominant_emotion'],'joy')
    def test_blank_route(self):
        with patch('server.emotion_detector') as detector:
            self.assertEqual(app.test_client().get('/emotionDetector?textToAnalyze=%20').text,'Invalid text! Please try again!')
            detector.assert_not_called()
    def test_service_failure(self):
        with patch('server.emotion_detector', side_effect=requests.Timeout()):
            self.assertIn('service unavailable',app.test_client().get('/emotionDetector?textToAnalyze=hello').text)

if __name__=='__main__':
    unittest.main()
