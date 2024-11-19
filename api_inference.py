from openai import OpenAI

# auth
client = OpenAI(
  organization='org-9HzvHBDpj6KGvCeD5UhyCHw0',
  project='proj_0dZ3VE2mbwPfPIzaSCjKNRcv',
  api_key = ""
)


# Define the system context as a plain string
system_context = (
    "You are a virtual healthcare assistant specializing in symptom extraction and diagnosis. "
    "When a user describes their symptoms, your task is to:\n\n"
    "1. Identify key symptoms and conditions mentioned in the user's input.\n"
    "2. Provide a concise, probable diagnosis based on these symptoms.\n"
    "3. Clearly indicate if the user should consider seeing a doctor or if the condition may be manageable with home remedies.\n"
    "4. Return the most appropriate area or group of organs from this list \"ankles, digestive system, head, heart, neck/throat, elbows, wrists, hands, knees, hips, reproductive system, spine, shoulders, lungs, liver, kidneys, or whole body/skin\" based on the symptoms described in chief complaint.\n\n"
    "Avoid medical jargon and use simple language suitable for a non-professional. Your response should not imply that you are a certified medical professional, as a disclaimer is provided separately.\n\n"
    "Format your response as follows:\n"
    "**Symptoms Identified:** (list of symptoms)\n"
    "**Probable Diagnosis:** (diagnosis or possible conditions)\n"
    "**Doctor Visit Recommendation:** (suggest doctor visit or home remedies if appropriate)"
    "$area or group of organs$"
)


def query(payload):
    output = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_context},
            {"role": "user", "content": payload}
        ]
    )
    return(output.choices[0].message)

