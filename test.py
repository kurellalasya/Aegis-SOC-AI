import google.generativeai as genai

# Use the API Key you provided earlier
genai.configure(api_key="AIzaSyChm0nI2Q3QchZ2__yqfU5JiuO81pZ5bXc")

print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Model Name: {m.name}")