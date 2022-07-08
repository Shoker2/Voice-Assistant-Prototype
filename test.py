import pyttsx3
import requests
import os
import pyaudio
import wave

# client
text = 'Добрейший 123 вечерочек!'

response = requests.post('http://httpbin.org/post',json={'text': text})

# server
def server(response):
	text = response.json()['json']['text']
	id_client = (response.json()['headers']['X-Amzn-Trace-Id'])[5::]

	engine = pyttsx3.init()
	engine.save_to_file(text, f'./audios/{id_client}.mp3')
	engine.runAndWait()

	with open(f'./audios/{id_client}.mp3', 'rb') as file:
		data = file.read()

	res = requests.post('http://httpbin.org/post',json={
		'data': data.hex()
		})
	os.remove(f'./audios/{id_client}.mp3')
	return res

ress = server(response)
p = pyaudio.PyAudio()

ress = ress.json()['json']
data = bytes.fromhex(ress['data'])

name = 'speach'
with open(f"./audios/{name}.mp3", 'wb') as file:
	file.write(data)

wf = wave.open(f'./audios/{name}.mp3', 'rb')

p = pyaudio.PyAudio()

FORMAT = p.get_format_from_width(wf.getsampwidth())
CHANNELS = wf.getnchannels()
RATE = wf.getframerate()
CHUNK = 1024

data = wf.readframes(CHUNK)
wf.close()

stream = p.open(format=FORMAT,
				channels=CHANNELS,
				rate=RATE,
				frames_per_buffer=CHUNK,
				output=True)
wf = wave.open(f'./audios/{name}.mp3', 'rb')
while len(data) > 0:
	stream.write(data)
	data = wf.readframes(CHUNK)