import os
from subprocess import run

class ExecuteCommand:
    def __init__(self):
        self.name = "execute_command"
        self.description = "Ejecutar un comando en la terminal de linux"
        self.parameters = {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "El comando a ejecutar",
                },
            },
            "required": ["command"],
        }

    def execute(self, parameters):
        command = parameters["command"]
        print("Ejecutando comando: " + command)
        result = run(command, capture_output=True, shell=True, text=True)
        return {"status": "success", "stdout": result.stdout, "stderr": result.stderr }