import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Watson NLP Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers with the required model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the input JSON with the text to analyze
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make the POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
     
    # Check if status code is 400 (bad request - blank entry)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # Convert the response text into a dictionary using json library
    response_dict = json.loads(response.text)
    
    # Extract the required set of emotions with their scores
    # Navigate through the response structure to get emotion predictions
    if response.status_code == 200:
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Extract individual emotion scores
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Find the dominant emotion (emotion with the highest score)
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        # Get the dominant emotion name
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return the formatted output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return None
