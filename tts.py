import requests

#Texto a voz. Esta impl utiliza ElevenLabs
class TTS():
    voice_dict = {
        "Adam": "pNInz6obpgDQGcFmaJgB",
        "Antoni": "ErXwobaYiN019PkySvjV",
        "Arnold": "VR6AewLTigWG4xSOukaG",
        "Bella": "EXAVITQu4vr4xnSDxMaL",
        "Domi": "AZnzlk1XvdvUeBnXmlld",
        "Elli": "MF3mGyEYCl7XYWbV9V6O",
        "Josh": "TxGEqnHWrfWFTfGW9XjX",
        "Rachel": "21m00Tcm4TlvDq8ikWAM",
        "Sam": "yoZ06aMxZJJ28mfd3POQ"
    }

    def __init__(self, key):
        self.key = key
    
    def voices(self):
        return self.voice_dict

    def process(self, text):
        CHUNK_SIZE = 1024
        #Utiliza la voz especifica de Bella
        #Me robe este codigo de su pagina hoh
        url = "https://api.elevenlabs.io/v1/text-to-speech/" + self.voice_dict[voice]

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.key
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v1",
            "voice_settings": {
                "stability": 0.55,
                "similarity_boost": 0.55
            }
        }

        #Lo guarda en static/response.mp3 para que el sitio web
        #pueda leerlo y reproducirlo en el explorador
        file_name = "response.mp3"
        response = requests.post(url, json=data, headers=headers)
        with open("static/" + file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    
        return file_name

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv()
    elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
    tts = TTS(elevenlabs_key)
    print(tts.voices())
    tts.process("Esta es una respuesta", "Bella")
