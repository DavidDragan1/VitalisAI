# Flask NLP app
This app is an online symptom diagnosis tool consisting of:
- a multi-step form allowing user to input contextual data and symptoms
- a diagnosis page which outputs:
  - the most probable diagnosis in plain english, avoiding medical jargon
  - the identified symptoms, to ensure lower rate of hallucination/ misinterpretation
  - BMI calculation, with traffic light indicator of whether the user is underweight, normal, overweight, or obese
  - an anatomical model with the user's identified pain area highlighted in red, serving as another visual confirmation to avoid misdiagnosis
- a logging and feedbadck utility, so that logs may be used to further evaluate model response accuracy, and feedback for refining the UI

I used flask, with python handling the backend routing, calculations, and inference. It is actually quite a simple app but the functionality achieved has made me realise just how overkill frameworks are most of the time for small projects. Plain HTML, CSS, and JS for the frontend - in all fairness using react would have probably made it less annoying to implement the multistep form, but the focus was purely on the data science so I opted for the most barebones configuration possible.

It is easy to see the potential utility of such an application. This was for a University assignment so achieved in a short burst, but nevertheless, with a more robust implementation and more features such as image input for identifying rashes, lesions and such, the time-cost benefits become readily apparent.


---
```
TO RUN YOURSELF:
1. fork the repo
2. open in GH codespaces
3. make new .env and add your OpenAI key as: API_KEY="<your key here>"
4. $ flask run
```