from firebase_functions import https_fn
from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key = os.getenv("OPEN_AI")

@app.route('/')
def hello_world():
    return 'Hello, Firebase Cloud Functions with Python'

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data['prompt']
        
        response = generate(prompt)

        result = {
            "response": response
        }

        return jsonify(result)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        return jsonify({"error": error_message}), 500


def generate(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"{prompt}",
        max_tokens=1024
        )
    return response

@https_fn.on_request(max_instances=1)
def articles(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()