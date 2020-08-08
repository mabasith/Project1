import speech_recognition as sr 
AUDIO_FILE=("file_example_WAV_1MG.wav[;")
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	audio=r.record(source)
try:
	print("audio file contains" + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Could not understand")
except sr.RequestError:
	print("Couldn't get")