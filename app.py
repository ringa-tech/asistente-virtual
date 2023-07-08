import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json
from transcriber import Transcriber
from llm import LLM
from weather import Weather
from tts import TTS
from pc_command import PcCommand
from functions.execute_command import ExecuteCommand
from functions.only_say_something import OnlySaySomething
from functions.create_file import CreateFile
from functions.command_sequence import CommandSequence

#Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("recorder.html")

@app.route("/audio", methods=["POST"])
def audio():
    #Obtener audio grabado y transcribirlo
    audio = request.files.get("audio")
    text = Transcriber().transcribe(audio)

    print(f"TEXT: {text}")
    
    functions = [OnlySaySomething(),ExecuteCommand(),CreateFile(),CommandSequence()]

    #Utilizar el LLM para ver si llamar una funcion
    llm = LLM(functions)
    function_name, args, message = llm.process_functions(text)
    if function_name is not None:

        for function in functions:
            if function.name == function_name:
                function_response = function.execute(args)
                function_response = json.dumps(function_response)
                print(f"Respuesta de la funcion: {function_response}")

                final_response = llm.process_response(text, message, function_name, function_response)
                tts_file = TTS().process(final_response)
                print(f"Respuesta final: {final_response}")
                return {"result": "ok", "text": final_response, "file": tts_file}
                break
        
        return {"result": "ok", "text": "No se encontró la función"}

    else:
        print("No se llamó a ninguna función")
        final_response = llm.process_message(text)
        tts_file = TTS().process(final_response)
        return {"result": "ok", "text": final_response, "file": tts_file}