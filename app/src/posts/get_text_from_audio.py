import speech_recognition as sr
import base64

from app.src.posts.schemas import Audio

recognizer = sr.Recognizer()


def get_text(encoding: Audio):
    tmp_file = open("temp.wav", "wb")
    decoded_string = base64.b64decode(encoding.encoding)
    tmp_file.write(decoded_string)

    with sr.AudioFile("temp.wav") as source:
        audio_text = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio_text, language="de-DE")
        except Exception as e:
            print(print(f"There was an error: {e}"))
