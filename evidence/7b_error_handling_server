"""Flask web application for Watson NLP emotion detection."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the input and format the result for the provided web interface."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"
    try:
        result = emotion_detector(text_to_analyze)
    except (RequestException, ValueError, KeyError, IndexError):
        return "Emotion detection service unavailable. Please try again later."
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )


@app.route("/")
def index():
    """Render the original project interface."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
