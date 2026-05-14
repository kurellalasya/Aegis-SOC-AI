import google.generativeai as genai
from .prompts import SYSTEM_PROMPTS

class SecurityAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        
        # Updated to the stable 3.1 Flash Lite model from your list
        self.model_name = 'gemini-3.1-flash-lite' 
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def run_stage(self, stage_name, user_input):
        try:
            # Constructing the agentic prompt
            full_prompt = f"SYSTEM ROLE: {SYSTEM_PROMPTS[stage_name]}\n\nUSER INPUT LOGS:\n{user_input}"
            
            response = self.model.generate_content(full_prompt)
            
            if response.text:
                return response.text
            return "Agent Error: Model returned no content."
                
        except Exception as e:
            print(f"DEBUG: {e}")
            return f"Technical Error: {str(e)}"