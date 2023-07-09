from subprocess import run
class CommandSequence:
    def __init__(self):
        self.name = "command_sequence"
        self.description = "Ejecutar una secuencia de comandos"
        self.parameters = {
            "type": "object",
            "properties": {
                "commands": {
                    "type": "array",
                    "description": "La lista de comandos a ejecutar",
                    "items": {
                        "type": "object",
                        "properties": {
                            "command": {
                                "type": "string",
                                "description": "El comando a ejecutar",
                            },
                        },
                        "required": ["command"],
                    }
                }
            },
            "required": ["commands"],
        }

    def execute(self, parameters):
        commands = parameters["commands"]
        print("Ejecutando secuencia de comandos: " + str(commands))
        for command in commands:
            result = run(command["command"], capture_output=True, shell=True, text=True)
            print(result.stdout)
            print(result.stderr)
        return {"status": "success"}