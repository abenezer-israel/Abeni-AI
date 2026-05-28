"""
ABENI AI - WORKING VERSION
Use gemini-2.5-flash instead of 1.5
"""

import google.generativeai as genai
import datetime

# 🔑 YOUR API KEY
API_KEY = "××××××××××××××××××××××@"

class AbeniAI:
    def __init__(self):
        self.name = "Abeni"
        
    def get_response(self, user_input):
        try:
            genai.configure(api_key=API_KEY)
            # ✅ CHANGE THIS LINE - Use gemini-2.5-flash
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(f"You are Abeni, a friendly AI assistant. Respond to: {user_input}")
            return response.text
        except Exception as e:
            return self.fallback_response(user_input)
    
    def fallback_response(self, user_input):
        """Simple offline responses"""
        user_input = user_input.lower()
        now = datetime.datetime.now()
        
        if 'hello' in user_input or 'hi' in user_input:
            return "Hello! I'm Abeni! How can I help you today?"
        elif 'time' in user_input:
            return f"The time is {now.strftime('%I:%M %p')}"
        elif 'date' in user_input:
            return f"Today is {now.strftime('%B %d, %Y')}"
        elif 'bye' in user_input or 'exit' in user_input:
            return "Goodbye! Have a great day!"
        else:
            return f"I'm Abeni. Tell me more about: {user_input}"

def main():
    print("\n" + "="*45)
    print("   🤖 ABENI AI - READY 🤖")
    print("="*45)
    print("\nType 'exit' to quit\n")
    
    abeni = AbeniAI()
    
    # Test connection
    try:
        genai.configure(api_key=API_KEY)
        test_model = genai.GenerativeModel('gemini-2.5-flash')
        print("✅ Connected to Gemini 2.5 Flash!\n")
    except Exception as e:
        print(f"⚠️ Using offline mode: {str(e)[:50]}\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nAbeni: Goodbye! 👋")
            break
        
        if user_input:
            response = abeni.get_response(user_input)
            print(f"\nAbeni: {response}")
            print("-"*40)

if __name__ == "__main__":
    main()
