import google.generativeai as genai
import os

def code_builder(prompt):
    file_path = "C:\\Users\\bharg\\OneDrive\\Desktop\\gemini api key.txt"
    with open(file_path, 'r') as f:
        api_key = f.read().strip()

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    checker_prompt = f"Is the following prompt related to programming or code? Respond with only 'yes' or 'invalid prompt'. Prompt: {prompt}"
    checker = model.generate_content(checker_prompt)

    clean_text = checker.text.lower().strip().replace("`", "").replace("\n", "")

    if clean_text == 'yes':
        result = model.generate_content(prompt+".code without any description.")
        return result
    else:
        return checker





