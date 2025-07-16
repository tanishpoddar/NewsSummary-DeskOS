"""
Utility functions for fetching and summarizing news articles using NewsAPI and Gemini API.
"""
import os
import requests
import json

NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

NEWSAPI_BASE_URL = 'https://newsapi.org/v2/'

def fetch_latest_news():
    """
    Fetch the latest top headlines from NewsAPI.
    Returns a list of article dicts.
    """
    url = f'{NEWSAPI_BASE_URL}top-headlines'
    params = {'country': 'us', 'apiKey': NEWSAPI_KEY, 'pageSize': 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get('articles', [])

def fetch_news_by_query(query):
    """
    Fetch news articles from NewsAPI matching the given query.
    Returns a list of article dicts.
    """
    url = f'{NEWSAPI_BASE_URL}everything'
    params = {'q': query, 'apiKey': NEWSAPI_KEY, 'pageSize': 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get('articles', [])

def summarize_text(text):
    """
    Summarize the given text using the Gemini API.
    Returns a summary string, or a fallback message on error.
    """
    prompt = f"Summarize the following news article in 2-3 sentences:\n{text}"
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": GEMINI_API_KEY
        }
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        # Extract summary from Gemini response
        summary = result["candidates"][0]["content"]["parts"][0]["text"].strip()
        return summary
    except Exception as e:
        print(e)
        return "Summary not available." 