"""
Module inside of Sentiment Analysis package which analyzes text
for positive or negative or neutral feelings
"""
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """Function which takes in text and uses the Watson Sentiment
    Analyzer to analyze given input for positive or negative feelings"""
    url = '''https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'''
    header =  {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj  = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {"label": label, "score": score}
