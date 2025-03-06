import openai
import google.generativeai
import json

openai.api_key = "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"
google.generativeai.configure(api_key="YOUR_GEMINI_API_KEY")

def call_chatgpt(prompt):
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
    return response["choices"][0]["message"]["content"]

def call_gemini(prompt):
    response = google.generativeai.generate_text(model="gemini-pro", prompt=prompt)
    return response.text

def generate_response(user, prompt):
    history = memory_manager.retrieve_context(user)
    combined_prompt = f"Previous context: {history}\n\nCurrent query: {prompt}"
    
    response_gpt = call_chatgpt(combined_prompt)
    response_gemini = call_gemini(combined_prompt)
    
    final_response = f"GPT-4: {response_gpt}\n\nGemini: {response_gemini}"
    
    memory_manager.store_context(user, prompt + " -> " + final_response)
    
    return final_response
