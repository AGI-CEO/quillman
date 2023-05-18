from elevenlabs import generate, play, set_api_key
from elevenlabs.api import History
from modal import method


set_api_key("73691b48e701784d320f3ab8e759b16a")

class ElevenLabs:
    def __init__(self, voice_name):
        """
        Initialize the class with the provided voice name.
        """
        self.voice_name = voice_name

    def __enter__(self):
        """
        Set the voice to the provided voice name when the container starts.
        """
        self.voice = self.voice_name

    @method()
    def speak(self, text):
        """
        Runs ElevenLabs TTS on a given text with the provided voice.
        """

        text = text.strip()
        if not text:
            return

        audio = generate(text=text, voice=self.voice)

        return audio

elevenlabs = ElevenLabs("Elon Tusk")
