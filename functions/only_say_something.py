class OnlySaySomething:
    def __init__(self):
        self.name = "respond"
        self.description = "Responder con un mensaje"
        self.parameters = {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "Respuesta a enviar",
                },
            },
            "required": ["message"],
        }

    def execute(self, parameters):
        return {"status": "success", "message": parameters["message"]}