import speech_recognition as sr
import pyttsx3
import re
import asyncio
from googletrans import Translator, LANGUAGES

class VoiceTranslator:
    def __init__(self, voice_index=0):
        self.translator = Translator()
        self.engine = pyttsx3.init()
        self.set_voice(voice_index)
        self.language_mapping = {name.lower(): code for code, name in LANGUAGES.items()}

    def set_voice(self, voice_index):
        """Set the TTS engine to use the specified voice."""
        voices = self.engine.getProperty('voices')
        if 0 <= voice_index < len(voices):
            self.engine.setProperty('voice', voices[voice_index].id)
        else:
            print("Invalid voice index. Using default voice.")

    def listen(self):
        """Capture voice input and convert it to text."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return None
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return None

    async def translate_text(self, text, dest_language='en'):
        """Translate the given text to the specified destination language."""
        translated = await self.translator.translate(text, dest=dest_language)
        return translated.text

    def speak(self, text):
        """Convert the given text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

    def parse_command(self, command):
        """Parse the command to extract the phrase and target language."""
        match = re.search(r'translate (.+?) to (.+)', command, re.IGNORECASE)
        if match:
            phrase = match.group(1).strip()
            target_language = match.group(2).strip()
            return phrase, target_language
        return None, None

    def show_supported_languages(self):
        """Display the supported languages."""
        print("Supported languages:")
        for lang_code, lang_name in LANGUAGES.items():
            print(f"{lang_code}: {lang_name}")
        self.speak("Here are the supported languages. Please check the console.")

    def ask_for_supported_languages(self):
        """Ask the user if they want to see supported languages."""
        print("Would you like to see the supported languages? Please say 'yes' or 'no'.")
        response = self.listen()
        if response and "yes" in response.lower():
            self.show_supported_languages()
        elif response and "no" in response.lower():
            print("Okay, let's proceed with the translation.")
        else:
            print("I didn't catch that. Let's proceed with the translation.")

    async def run(self):
        """Main function to execute the translation process."""
        self.ask_for_supported_languages()
        
        while True:
            print("Keep translating or say exit to close translator:")
            input_text = self.listen()
            if input_text:
                if "exit" in input_text.lower():
                    print("Exiting the translator. Goodbye!")
                    break
                
                phrase, target_language = self.parse_command(input_text)
                print(f"Phrase: '{phrase}', To language: '{target_language}'")
                
                if phrase and target_language:
                    # Checks if the target language is valid for translation
                    target_language_code = self.language_mapping.get(target_language.lower())
                    
                    if target_language_code:
                        translated_text = await self.translate_text(phrase, dest_language=target_language_code)
                        print(f"Translated text: {translated_text}")
                        self.speak(translated_text)
                    else:
                        print(f"'{target_language}' is not a valid language code. Please use a supported language.")
                else:
                    print("Could not parse the command. Please use the format 'translate (phrase) to (language).")


async def main():
    translator = VoiceTranslator(voice_index=3)  # Change the number to use a different voice
    await translator.run()

if __name__ == "__main__":
    asyncio.run(main())
