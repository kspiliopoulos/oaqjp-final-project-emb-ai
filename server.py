"""
Flask application for Emotion Detection
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to handle emotion detection requests
    """
    # Get the text to analyze from request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)
    
    # Check if response is valid
    if response['dominant_emotion'] is None:
        return "Invalid input! Please try again."
        
    # Format the response string
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Create formatted response string
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return response_text

@app.route("/")
def render_index_page():
    """
    Route to render the main index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
