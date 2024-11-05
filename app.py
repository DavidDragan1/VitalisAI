from flask import Flask, request, render_template
from api_inference import query
import re


app = Flask(__name__)


@app.route('/')  # default render route
def index():
    return render_template('index.html', output=" ") #  sets empty output box


@app.route('/response', methods=['POST'])
def diagnosis():
    # Get form data
    age = request.form.get('age')
    sex = request.form.get('sex')
    conditions = request.form.get('conditions')
    occupation = request.form.get('occupation')
    symptoms = request.form.get('symptoms')
    
    output = query(f"Patient Profile: {age}, sex: {sex}, conditions: {conditions}, occupation: {occupation}. Chief Complaint: {symptoms}. What is your diagnosis and recommendation?").content

    # Process the output
    formatted_output = process_output(output)

    # Render the result in the template
    return render_template('response.html', output=formatted_output)

def process_output(output):
    # Remove unwanted parts using regex
    cleaned_output = re.sub(r"content='- |refusal=None|role='assistant'|audio=None|function_call=None|tool_calls=None", "", output)

    # Replace '**text**' with '<h2>text</h2>'
    formatted_output = re.sub(r'\*\*(.*?)\*\*', r'<h2>\1</h2>', cleaned_output)

    return formatted_output





