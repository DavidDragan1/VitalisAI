from flask import Flask, request, render_template
from api_inference import query
import re


app = Flask(__name__)


@app.route('/')  # default render route
def index():
    return render_template('index.html', output=" ") #  sets empty output box


@app.route('/response', methods=['POST'])
def diagnosis():
    global body_area # declare global variable 
    # Get form data
    age = request.form.get('age')
    sex = request.form.get('sex')
    weight = int(request.form.get('weight'))
    height = int(request.form.get('height'))
    conditions = request.form.get('conditions')
    occupation = request.form.get('occupation')
    symptoms = request.form.get('symptoms')

    bmi = str(getBmi(weight, height)) # calc bmi

    # inference model via query method from api_inference.py script, passing relevant values
    output = query(f"Patient Profile: {age}, sex: {sex}, conditions: {conditions}, Body-Mass-Index: {bmi}, occupation: {occupation}. Chief Complaint: {symptoms}. What is your diagnosis and recommendation?").content

    # Process the output and save body_area
    formatted_output, body_area = format_output(output)
    selected_img = returnImage()
    bmi_status = evalBmi(float(bmi))

    # Render the result in the template
    return render_template('response.html', output=formatted_output, anat_img=selected_img, bmi=bmi, bmi_status=bmi_status)


def format_output(output):
    # Extract the value inside $(...) and save it as body_area
    body_area_match = re.search(r'\$(.*?)\$', output)
    body_area = body_area_match.group(1) if body_area_match else None

    # Remove the $(...) from the output
    cleaned_output = re.sub(r'\$(.*?)\$', '', output)

    # Remove other unwanted parts using regex
    cleaned_output = re.sub(r"content='- |refusal=None|role='assistant'|audio=None|function_call=None|tool_calls=None", "", cleaned_output)

    # Replace '**text**' with '<h2>text</h2>'
    formatted_output = re.sub(r'\*\*(.*?)\*\*', r'<h2>\1</h2>', cleaned_output)

    return formatted_output, body_area


def getBmi(w, h): # get weight and height values, divide weight by height in metres^2 and return bmi rounded to 1 dec point
    bmi = w / ((h / 100) ** 2)
    return round(bmi, 2)

def evalBmi(bmi):
    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi > 24.9 and bmi < 30:
        bmi_status = "Overweight"
    elif bmi > 30:
        bmi_status = "Obese"
    else:
        bmi_status = "Normal"
    return bmi_status


@app.route('/image', methods=['GET'])
def returnImage():
    global body_area # very simple decision tree that accesses global var and returns relevant image based on user chief complaint

    selected_img = "img/anatomy.png"
    match body_area:
        case "ankles":
            selected_img = "img/ankles.png"
        case "digestive system":
            selected_img = "img/dig-sys.png"
        case "elbows":
            selected_img = "img/elbows.png"
        case "hands":
            selected_img = "img/hands.png"
        case "head":
            selected_img = "img/head.png"
        case "heart":
            selected_img = "img/heart.png"
        case "hips":
            selected_img = "img/hips.png"
        case "kidneys":
            selected_img = "img/kidneys.png"
        case "knees":
            selected_img = "img/knees.png"
        case "liver":
            selected_img = "img/liver.png"
        case "lungs":
            selected_img = "img/lungs.png"
        case "reproductive system":
            selected_img = "img/re-sys.png"
        case "shoulders":
            selected_img = "img/shoulders.png"
        case "spine":
            selected_img = "img/spine.png"
        case "neck/throat":
            selected_img = "img/throat.png"
        case "wrists":
            selected_img = "img/wrists.png"
        case "whole body/skin":
            selected_img = "img/red.png"
    
    return selected_img
