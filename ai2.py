"""
ABENI AI - Beautiful Modern UI
Premium Interface for Pydroid 3
"""

import google.generativeai as genai
import datetime
import random
import os
import time

# 🔑 YOUR API KEY
API_KEY = "×××××××××××××××××××××××"

# ============================================
# MODERN UI DESIGN
# ============================================

class ModernUI:
    """Handles all visual elements"""
    
    @staticmethod
    def clear():
        """Clear screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    @staticmethod
    def color(text, color_code):
        """Add color to text"""
        colors = {
            'red': '91',
            'green': '92',
            'yellow': '93',
            'blue': '94',
            'purple': '95',
            'cyan': '96',
            'white': '97',
            'bold': '1',
            'dim': '2'
        }
        code = colors.get(color_code, '97')
        return f"\033[{code}m{text}\033[0m"
    
    @staticmethod
    def box(text, color='cyan', width=60):
        """Create a beautiful box around text"""
        color_code = {'cyan': '96', 'green': '92', 'purple': '95', 'yellow': '93'}.get(color, '96')
        lines = text.split('\n')
        
        box_top = f"\033[{color_code}m╔{'═' * (width-2)}╗\033[0m"
        box_bottom = f"\033[{color_code}m╚{'═' * (width-2)}╝\033[0m"
        
        result = [box_top]
        for line in lines:
            padding = width - len(line) - 4
            if padding < 0:
                line = line[:width-5] + "..."
                padding = 0
            result.append(f"\033[{color_code}m║\033[0m {line} {' ' * padding} \033[{color_code}m║\033[0m")
        result.append(box_bottom)
        
        return '\n'.join(result)
    
    @staticmethod
    def header():
        """Display modern header"""
        logo = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║      █████╗ ██████╗ ███████╗███╗   ██╗██╗              ║
    ║     ██╔══██╗██╔══██╗██╔════╝████╗  ██║██║              ║
    ║     ███████║██████╔╝█████╗  ██╔██╗ ██║██║              ║
    ║     ██╔══██║██╔══██╗██╔══╝  ██║╚██╗██║██║              ║
    ║     ██║  ██║██████╔╝███████╗██║ ╚████║██║              ║
    ║     ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝              ║
    ║                                                          ║
    ║                 ✨ PREMIUM AI ASSISTANT ✨               ║
    ║                   Next Generation AI                    ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
        """
        print(ModernUI.color(logo, 'cyan'))
        
        # Status bar
        now = datetime.datetime.now()
        status = f"  🟢 ONLINE  |  {now.strftime('%I:%M %p')}  |  Gemini 2.5 Flash  "
        print(ModernUI.color(status, 'dim'))
        print("═" * 70)

class ChatBubble:
    """Creates chat bubbles for messages"""
    
    @staticmethod
    def user_message(text):
        """Format user message"""
        border = "─" * 55
        return f"""
{ModernUI.color('┌' + '─' * 53 + '┐', 'yellow')}
{ModernUI.color('│ 💬 YOU ', 'yellow')}{ModernUI.color(' ' * 45, 'yellow')}{ModernUI.color('│', 'yellow')}
{ModernUI.color('│', 'yellow')} {text[:50]}{' ' * (52 - len(text[:50]))}{ModernUI.color('│', 'yellow')}
{ModernUI.color('└' + '─' * 53 + '┘', 'yellow')}
"""
    
    @staticmethod
    def ai_message(text):
        """Format AI message with typing animation"""
        # Split long text
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + " " + word) <= 50:
                current_line += " " + word if current_line else word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        
        # Build message
        result = f"""
{ModernUI.color('┌' + '─' * 53 + '┐', 'green')}
{ModernUI.color('│ 🤖 ABENI ', 'green')}{ModernUI.color(' ' * 43, 'green')}{ModernUI.color('│', 'green')}
"""
        for line in lines:
            result += f"{ModernUI.color('│', 'green')} {line:<52} {ModernUI.color('│', 'green')}\n"
        
        result += f"{ModernUI.color('└' + '─' * 53 + '┘', 'green')}"
        return result
    
    @staticmethod
    def typing_effect(text, delay=0.02):
        """Simulate typing animation"""
        print(ModernUI.color("╭" + "─" * 53 + "╮", 'green'))
        print(ModernUI.color("│ 🤖 ABENI ", 'green') + ModernUI.color(" " * 43, 'green') + ModernUI.color("│", 'green'))
        
        # Type character by character
        current_line = ""
        for char in text:
            current_line += char
            if len(current_line) > 50 and char == ' ':
                print(ModernUI.color("│", 'green') + " " + current_line + " " * (52 - len(current_line)) + ModernUI.color("│", 'green'))
                current_line = ""
                time.sleep(delay)
            else:
                time.sleep(delay/2)
        
        if current_line:
            print(ModernUI.color("│", 'green') + " " + current_line + " " * (52 - len(current_line)) + ModernUI.color("│", 'green'))
        
        print(ModernUI.color("╰" + "─" * 53 + "╯", 'green'))

class MenuSystem:
    """Interactive menu system"""
    
    @staticmethod
    def show_main_menu():
        """Display main menu"""
        menu = """
    ╔════════════════════════════════════════╗
    ║           🎮 MAIN MENU 🎮              ║
    ╠════════════════════════════════════════╣
    ║  [1] 💬  Start Chatting               ║
    ║  [2] 📊  View Statistics              ║
    ║  [3] 🎨  Change Theme                 ║
    ║  [4] 💾  Export Chat History          ║
    ║  [5] ❓  Help & Commands              ║
    ║  [6] 🚪  Exit                         ║
    ╚════════════════════════════════════════╝
        """
        print(ModernUI.color(menu, 'purple'))
        return input(ModernUI.color("\n👉 Select option (1-6): ", 'yellow')).strip()
    
    @staticmethod
    def show_help():
        """Display help menu"""
        help_text = """
    ╔══════════════════════════════════════════════════════════╗
    ║                    📚 COMMANDS GUIDE                     ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║  💬 BASIC COMMANDS:                                      ║
    ║     • Just type anything to chat with Abeni             ║
    ║     • Ask questions, get answers, have conversations    ║
    ║                                                          ║
    ║  🎮 SPECIAL COMMANDS:                                   ║
    ║     • /help     - Show this menu                        ║
    ║     • /stats    - View session statistics               ║
    ║     • /clear    - Clear chat history                    ║
    ║     • /theme    - Change interface colors               ║
    ║     • /save     - Export conversation                   ║
    ║     • /menu     - Return to main menu                   ║
    ║                                                          ║
    ║  🚀 TIPS:                                                ║
    ║     • Be specific with your questions                   ║
    ║     • Ask follow-up questions                           ║
    ║     • Abeni remembers context in conversation          ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
        """
        print(ModernUI.color(help_text, 'cyan'))
        input(ModernUI.color("\nPress Enter to continue...", 'dim'))

class AbeniAI:
    """Main AI class"""
    
    def __init__(self):
        self.name = "Abeni"
        self.chat_history = []
        self.start_time = datetime.datetime.now()
        self.conversation = []
        
    def get_response(self, user_input):
        """Get response from Gemini"""
        try:
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            prompt = f"""You are Abeni, a friendly, intelligent AI assistant.
            
User: {user_input}

Respond naturally, conversationally, and helpfully. Keep responses concise but informative. Use occasional emojis to be friendly."""
            
            response = model.generate_content(prompt)
            
            # Save to history
            self.chat_history.append({
                'user': user_input,
                'ai': response.text,
                'time': datetime.datetime.now()
            })
            
            return response.text
            
        except Exception as e:
            return f"I'm having a small technical issue. Let me try a different approach! What would you like to know? (Error: {str(e)[:50]})"
    
    def get_stats(self):
        """Get session statistics"""
        duration = datetime.datetime.now() - self.start_time
        minutes = int(duration.total_seconds() / 60)
        messages = len(self.chat_history)
        
        stats = f"""
    ╔════════════════════════════════════════╗
    ║           📊 SESSION STATS             ║
    ╠════════════════════════════════════════╣
    ║  🕐 Session Duration: {minutes:>3} minutes      ║
    ║  💬 Messages Exchanged: {messages:>2}            ║
    ║  ⚡ Avg messages/min: {messages/(minutes+1):>4.1f}          ║
    ║  🤖 AI Status: ONLINE                  ║
    ║  🎨 Theme: Modern UI                   ║
    ╚════════════════════════════════════════╝
        """
        return stats
    
    def save_chat(self):
        """Export chat history"""
        if not self.chat_history:
            return "No chat history to save."
        
        filename = f"abeni_chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("═" * 60 + "\n")
                f.write("ABENI AI CHAT HISTORY\n")
                f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("═" * 60 + "\n\n")
                
                for i, chat in enumerate(self.chat_history, 1):
                    f.write(f"[{i}] You: {chat['user']}\n")
                    f.write(f"    Abeni: {chat['ai']}\n\n")
            
            return f"✅ Chat saved to: {filename}"
        except Exception as e:
            return f"❌ Error saving: {str(e)}"

# ============================================
# MAIN APPLICATION
# ============================================

def chat_mode(abeni):
    """Main chat interface"""
    ModernUI.clear()
    print(ModernUI.color(ModernUI.box("💬 CHAT MODE - Type /menu to exit", 'cyan', 60), 'cyan'))
    print(ModernUI.color("Type your message and press Enter\n", 'dim'))
    
    while True:
        try:
            # User input with nice prompt
            print(ModernUI.color("┌" + "─" * 53 + "┐", 'yellow'))
            user_input = input(ModernUI.color("│ You: ", 'yellow'))
            print(ModernUI.color("└" + "─" * 53 + "┘", 'yellow'))
            
            user_input = user_input.strip()
            
            # Exit conditions
            if user_input.lower() == '/menu':
                return
            elif user_input.lower() in ['exit', 'quit', 'bye']:
                print(ModernUI.color("\n👋 Thanks for chatting with Abeni!\n", 'green'))
                time.sleep(1)
                return
            
            # Special commands
            if user_input.lower() == '/stats':
                print(ModernUI.color(abeni.get_stats(), 'cyan'))
                continue
            elif user_input.lower() == '/save':
                print(ModernUI.color(abeni.save_chat(), 'green'))
                continue
            elif user_input.lower() == '/help':
                MenuSystem.show_help()
                continue
            elif user_input.lower() == '/clear':
                abeni.chat_history = []
                print(ModernUI.color("✨ Chat history cleared!", 'green'))
                continue
            
            if not user_input:
                continue
            
            # Get AI response with typing effect
            response = abeni.get_response(user_input)
            ChatBubble.typing_effect(response)
            print()  # Extra line for spacing
            
        except KeyboardInterrupt:
            print(ModernUI.color("\n\n⚠️ Press Ctrl+C again to exit, or type /menu\n", 'yellow'))
        except Exception as e:
            print(ModernUI.color(f"\n❌ Error: {str(e)}\n", 'red'))

def main():
    """Main program"""
    ModernUI.clear()
    
    # Show header
    ModernUI.header()
    
    # Initialize AI
    print(ModernUI.color("\n⏳ Initializing Abeni AI...", 'dim'))
    time.sleep(1)
    
    abeni = AbeniAI()
    
    # Test connection
    try:
        genai.configure(api_key=API_KEY)
        test_model = genai.GenerativeModel('gemini-2.5-flash')
        print(ModernUI.color("✅ Connection successful! Abeni is ready.\n", 'green'))
    except Exception as e:
        print(ModernUI.color(f"⚠️ Limited mode: {str(e)[:50]}\n", 'yellow'))
    
    time.sleep(1)
    
    # Welcome message
    welcome_msg = "✨ Hello! I'm Abeni, your AI assistant! I'm ready to help you with anything - questions, creative tasks, or just a friendly chat! What would you like to talk about? ✨"
    ChatBubble.typing_effect(welcome_msg)
    print()
    
    # Main menu loop
    while True:
        choice = MenuSystem.show_main_menu()
        
        if choice == '1':
            chat_mode(abeni)
            ModernUI.clear()
            ModernUI.header()
        elif choice == '2':
            print(ModernUI.color(abeni.get_stats(), 'cyan'))
            input(ModernUI.color("\nPress Enter to continue...", 'dim'))
            ModernUI.clear()
            ModernUI.header()
        elif choice == '3':
            print(ModernUI.color("\n🎨 Theme options coming soon!\n", 'yellow'))
            input(ModernUI.color("Press Enter to continue...", 'dim'))
        elif choice == '4':
            print(ModernUI.color(f"\n{abeni.save_chat()}\n", 'green'))
            input(ModernUI.color("Press Enter to continue...", 'dim'))
        elif choice == '5':
            MenuSystem.show_help()
        elif choice == '6':
            print(ModernUI.color("\n╔════════════════════════════════════════╗", 'green'))
            print(ModernUI.color("║    👋 THANK YOU FOR USING ABENI AI!    ║", 'green'))
            print(ModernUI.color("║         Have a wonderful day!          ║", 'green'))
            print(ModernUI.color("╚════════════════════════════════════════╝\n", 'green'))
            break
        else:
            print(ModernUI.color("\n❌ Invalid option! Please choose 1-6\n", 'red'))
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        input("\nPress Enter to exit...")
