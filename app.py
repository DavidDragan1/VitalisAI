from flask import Flask, request, render_template

import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext"
headers = {"Authorization": "Bearer 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"}


app = Flask(__name__)


@app.route('/')  # default render route
def index():
    return render_template('index.html', output=" ") #  sets empty output box


@app.route('/diagnosis', methods=['POST'])
def diagnosis():

    top3_list = []  # declares empty list/clears list on next turn

    # Get user input from the form
    symptoms = request.form['symptoms']

    output = query({
        "inputs": f"{symptoms.title()} are symptoms of [MASK]."
    })                                                           # passes inference & assigns output to mask token value

    for n in range(3):
        top3_list.append(output[n]["token_str"])  # append top 3 token strings from query result to list

    #  removing [' '] from output
    top3_list_f = str(top3_list).strip('[]').replace("'", '')

    return render_template('index.html', output=top3_list_f)
    # Send the result back to the HTML page


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

