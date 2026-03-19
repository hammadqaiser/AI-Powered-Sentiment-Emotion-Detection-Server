"""
server.py - Flask application for detecting emotions from text input using emotion_detector.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Flask route to process emotion detection from user input.
    Returns a formatted string with emotion scores or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def index():
    """
    Renders the homepage of the emotion detection app.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5054)
