class CreateFile:
    def __init__(self):
        self.name = "create_file"
        self.description = "Crear un archivo con el contenido que quieras"
        self.parameters = {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "El nombre del archivo a crear",
                },
                "content": {
                    "type": "string",
                    "description": "El contenido del archivo",
                },
            },
            "required": ["filename", "content"],
        }

    def execute(self, parameters):
        f = open(parameters["filename"], "w")
        f.write(parameters["content"])
        f.close()
        return {"status": "success"}