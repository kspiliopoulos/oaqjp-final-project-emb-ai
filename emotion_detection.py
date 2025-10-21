import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP Emotion Predict function.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: The text attribute from the response object
    """
    # Define the URL for the Watson NLP Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers with the required model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the input JSON with the text to analyze
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make the POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        response_json = response.json()
        print("Full Response:")
        print(json.dumps(response_json, indent=2))
        return response_json
    else:
        print(f"Error: Status code {response.status_code}")
        print(f"Response: {response.text}")
        return None
