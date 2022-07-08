from fastapi import Request, FastAPI
from pydantic import BaseModel
import pyttsx3
import requests
import os

import time

app = FastAPI()

class text_format(BaseModel):
	text: str
	UID: str

class data_format(BaseModel):
	command_id: int
	action: int
	value: float
	UID: str

class auth_format(BaseModel):
	UID: str
	code: int

def text2speach(text, id_client):
	engine = pyttsx3.init()
	engine.save_to_file(text, f'./audios/{id_client}.mp3')
	engine.runAndWait()

	with open(f'./audios/{id_client}.mp3', 'rb') as file:
		data = file.read()

	os.remove(f'./audios/{id_client}.mp3')
	return {'data': data.hex()}

@app.post("/")
async def get_text(text_data: text_format):
	text = text_data.text
	UID = text_data.UID

	responce = text2speach(text, UID)
	return responce

@app.post("/rts")
async def get_data(data: data_format):
	value = data.value
	return value

@app.post("/auth")
async def get_data(auth: auth_format):
	value = auth.code

	time.sleep(1)
	return ({'status':'OK'})