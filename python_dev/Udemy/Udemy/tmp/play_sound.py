import pyaudio
import wave

chunck = 1024
wf = wave.open('file_example_WAV_1MG.wav')
p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
channels = wf.getnchannels(),
rate = wf.getframerate(),
output= True)
data = wf.readframes(chunck)

while data != '':
    stream.write(data)
    data = wf.readframes(chunck)
stream.close()
p.terminate()
