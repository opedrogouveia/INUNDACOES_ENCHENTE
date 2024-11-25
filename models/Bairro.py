from models.Municipio import Municipio

class Bairro(Municipio):
    def __init__(self, estado, municipio, bairro, situacao, nivel, alerta, energia, agua):
        super().__init__(estado, municipio)
        self.bairro = bairro
        self.situacao = situacao
        self.nivel = nivel
        self.alerta = alerta
        self.energia = energia
        self.agua = agua