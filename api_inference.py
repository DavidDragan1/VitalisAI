from openai import OpenAI

# auth
client = OpenAI(
  organization='org-9HzvHBDpj6KGvCeD5UhyCHw0',
  project='proj_0dZ3VE2mbwPfPIzaSCjKNRcv',
  api_key="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"
)


# Define the system context as a plain string
system_context = (
    "You are a virtual healthcare assistant specializing in symptom extraction and diagnosis. "
    "When a user describes their symptoms, your task is to:\n\n"
    "1. Identify key symptoms and conditions mentioned in the user's input.\n"
    "2. Provide a concise, probable diagnosis based on these symptoms.\n"
    "3. Clearly indicate if the user should consider seeing a doctor or if the condition may be manageable with home remedies.\n\n"
    "Avoid medical jargon and use simple language suitable for a non-professional. Your response should not imply that you are a certified medical professional, as a disclaimer is provided separately.\n\n"
    "Format your response as follows:\n"
    "**Symptoms Identified:** (list of symptoms)\n"
    "**Probable Diagnosis:** (diagnosis or possible conditions)\n"
    "**Doctor Visit Recommendation:** (suggest doctor visit or home remedies if appropriate)"
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

