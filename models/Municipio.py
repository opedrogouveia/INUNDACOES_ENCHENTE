from models.Estado import Estado

class Municipio(Estado):
    def __init__(self, estado, municipio):
        super().__init__(estado)
        self.municipio = municipio