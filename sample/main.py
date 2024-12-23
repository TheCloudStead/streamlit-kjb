import json
import os
import azure.cognitiveservices.speech as speechsdk

# Load configuration from a JSON file
with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# Extract configuration values
KEY = config['primary_access_key']
LOCATION = config['location']
BOOK_PATH = "book.json"
VOICE = "en-US-BrianNeural"

# Load the book content from a JSON file
with open(BOOK_PATH, 'r', encoding='utf-8') as json_file:
    book = json.load(json_file)

def generate_audio(chapter_number, title, text):
    """
    Generate audio files for each chapter.

    :param chapter_number: The chapter number of the book.
    :param title: The title of the chapter.
    :param text: The content of the chapter.
    """
    audio_output_file = f"audio-files/chapter-{chapter_number}-{title}.mp3"

    # Configure Azure Speech SDK
    speech_config = speechsdk.SpeechConfig(subscription=KEY, region=LOCATION)
    speech_config.speech_synthesis_voice_name = VOICE
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)

    audio_config = speechsdk.AudioConfig(filename=audio_output_file)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Generate speech and save to file
    resp = synthesizer.speak_text(text)
    print(f"Generated audio for chapter {chapter_number}: {title} -> {audio_output_file}")

# Loop through each chapter in the book and generate audio
for chapter in book['chapters']:
    generate_audio(chapter['chapter_number'], chapter['title'], chapter['content'])