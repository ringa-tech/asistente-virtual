import openai
import json

#Clase para utilizar cualquier LLM para procesar un texto
#Y regresar una funcion a llamar con sus parametros
#Uso el modelo 0613, pero puedes usar un poco de
#prompt engineering si quieres usar otro modelo
class LLM():
    def __init__(self, functions):
        self.functions = functions
        pass
    
    def process_message(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                    #Si no te gusta que te hable feo, cambia aqui su descripcion
                    {"role": "system", "content": "Eres un asistente"},
                    {"role": "user", "content": text},
            ]
        )

        message = response["choices"][0]["message"]["content"]

        return message

    def process_functions(self, text):

        functions = []
        for function in self.functions:
            functions.append({
                "name": function.name,
                "description": function.description,
                "parameters": function.parameters,
            })

        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                    #Si no te gusta que te hable feo, cambia aqui su descripcion
                    {"role": "system", "content": "Eres un asistente"},
                    {"role": "user", "content": text},
            ], functions=functions,
            function_call="auto",
        )
        
        message = response["choices"][0]["message"]
        
        #Nuestro amigo GPT quiere llamar a alguna funcion?
        if message.get("function_call"):
            #Sip
            function_name = message["function_call"]["name"] #Que funcion?
            args = message.to_dict()['function_call']['arguments'] #Con que datos?
            print("Funcion a llamar: " + function_name)
            args = json.loads(args)
            return function_name, args, message
        
        return None, None, message
    
    #Una vez que llamamos a la funcion (e.g. obtener clima, encender luz, etc)
    #Podemos llamar a esta funcion con el msj original, la funcion llamada y su
    #respuesta, para obtener una respuesta en lenguaje natural (en caso que la
    #respuesta haya sido JSON por ejemplo
    def process_response(self, text, message, function_name, function_response):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                #Aqui tambien puedes cambiar como se comporta
                {"role": "system", "content": "Eres un asistente malhablado"},
                {"role": "user", "content": text},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )
        return response["choices"][0]["message"]["content"]