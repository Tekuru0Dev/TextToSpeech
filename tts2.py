from gtts import gTTS
from playsound import playsound
import os

# Text to convert to speech
text = input("Enter what you want as tts: ")

# Specify the language
language = "en"

# Create a gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Save the speech to a file
file_path = "output.mp3"
tts.save(file_path)

# Play the audio file
playsound(file_path)

# Optionally, delete the file after playing
os.remove(file_path)
