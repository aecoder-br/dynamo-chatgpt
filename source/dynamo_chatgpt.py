"""
-----------------------------------
Created by Maycon Freitas
AECOder
www.aecoder.com.br
www.linkedin.com/in/maycon-freitas/
maycon.freitas@aecoder.com.br
-----------------------------------
"""


### Libraries ###
import os
import clr
import json
import sys
import urllib2
import traceback

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *


### Classes ###
class OpenAIMessage:
	def __init__(self, message, role="user"):
		self.role = role
		self.content = [{
			"type": "text",
			"text": message
		}]
	
	def __dict__(self):
		return {
			"role": self.role,
			"content": self.content
		}


class OpenAIHistory:
	def __init__(self):
		self.messages = []
		self.path = os.getenv('APPDATA') + "\\AECOder\\dynamochatgpt\\history.json"
		if not os.path.exists(self.path):
			os.makedirs(os.path.dirname(self.path))
			self.save_to_file(self.path)
		else:
			self.load_from_file(self.path)
	
	def save_to_file(self, file_path):
		with open(file_path, 'w') as file:
			json.dump(self.messages, file)

	def load_from_file(self, file_path):
		with open(file_path, 'r') as file:
			try:
				self.messages = json.load(file)
			except:
				self.messages = []
				self.save_to_file(self.path)

	def add_message(self, message):
		self.messages.append(message.__dict__)
		self.save_to_file(self.path)

	def get_messages(self):
		self.load_from_file(self.path)
		return self.messages
	
	def clear(self):
		self.messages = []
		self.save_to_file(self.path)


class OpenAI:
	def __init__(self, api_key, organization_id="", project_id="", clear_history=False):
		self.api_key = api_key
		self.organization_id = organization_id
		self.project_id = project_id

		# Set the API key
		self.headers = {
			'Content-Type': 'application/json',
			'Authorization': 'Bearer ' + self.api_key
		}

		if self.organization_id != "":
			self.headers['OpenAI-Organization'] = self.organization_id

		if self.project_id != "":
			self.headers['OpenAI-Project'] = self.project_id
		
		self.history = OpenAIHistory()
		if clear_history:
			self.clear_history()


	def create_completion(self, prompt, model="gpt-4o", temperature=0, max_tokens=4095, top_p=1, frequency_penalty=0, presence_penalty=0):
		url = 'https://api.openai.com/v1/chat/completions'

		openai_message = OpenAIMessage(prompt)
		self.history.add_message(openai_message)

		data = "{ \"messages\": " + json.dumps(self.history.get_messages()) + ", \"model\": \"" + model + "\", \"temperature\": " + str(temperature) + ", \"max_tokens\": " + str(max_tokens) + ", \"top_p\": " + str(top_p) + ", \"frequency_penalty\": " + str(frequency_penalty) + ", \"presence_penalty\": " + str(presence_penalty) + " }"

		req = urllib2.Request(url, data, self.headers)
		response = urllib2.urlopen(req)

		system_response = json.loads(response.read().decode('utf-8')).get('choices')[0].get('message').get('content')
		self.history.add_message(OpenAIMessage(system_response, "system"))

		return system_response

	def get_history(self):
		return self.history.get_messages()
	
	def clear_history(self):
		self.history.clear()


### Main ###
api_key = IN[0]
organization_id = IN[1]
project_id = IN[2]

prompt = IN[3]
model = IN[4]
temperature = IN[5]
max_tokens = IN[6]
top_p = IN[7]
frequency_penalty = IN[8]
presence_penalty = IN[9]
clear_history = bool(IN[10])

try:
	openai = OpenAI(api_key, organization_id, project_id, clear_history)

	if len(prompt) > 0:
		response = openai.create_completion(prompt, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty)
		OUT = response
	else:
		raise Exception("Prompt is empty")
	

except:
	try:
		msg = traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1])[0].replace("Exception: ", "")
	except:
		msg = "An error has occurred. See details to get more information."
	errorReport = traceback.format_exc()
	taskDialog = TaskDialog("Error")
	taskDialog.MainInstruction = msg
	taskDialog.ExpandedContent = errorReport
	taskDialog.Show()
	OUT = errorReport