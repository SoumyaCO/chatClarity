'''
Contains models, inferencing.
'''
import requests
import os 
from dotenv import load_dotenv
load_dotenv()

# there will be two routes
# 1. for the user search [data processing ..]
# 2. for the similar message search

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"}

sentences = ["That is a happy dog",
			"That is a very happy person",
			"Today is a sunny day"]

def similarity_search(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = similarity_search({
	"inputs": {
		"source_sentence": "happy",
		"sentences": [
			"That is a happy dog",
			"That is a very happy person",
			"Today is a sunny day"
		]
	},
})
print(output)