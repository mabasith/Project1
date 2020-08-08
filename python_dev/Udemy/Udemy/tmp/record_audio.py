import pyaudio
import wave
FORMAT = pyaudio.paInt16
CHANNEL = 2
RATE = 44100
CHUNK = 1024
RECORD_SECOND = 5
WAVE_OUTPUT_FILENAME = 'file.wav'

audio = pyaudio.PyAudio()
stream = audio.open(format = FORMAT, channels=CHANNEL,
rate = RATE, input= True, frames_per_buffer=CHUNK)
print("recording...")

frames=[]

for i in range(0, int(RATE/RECORD_SECOND)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished")
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME,'wb')
waveFile.setchannels(CHANNEL)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frame))
waveFile.close()