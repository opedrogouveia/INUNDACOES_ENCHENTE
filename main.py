from models.Estado import Estado
from models.Municipio import Municipio
from models.Bairro import Bairro
from utils.menus import menu

# CADASTRANDO ESTADOS
e1 = Estado("RS")
e2 = Estado("SC")
e3 = Estado("PR")

# CADASTRANDO MUNICIPIOS
m1 = Municipio("RS", "Porto Alegre")    # RS
m2 = Municipio("RS", "Alvorada")
m3 = Municipio("RS", "Cachoeirinha")
m4 = Municipio("RS", "Canoas")
m5 = Municipio("RS", "Guaiba")
m6 = Municipio("RS", "Gravatai")
m7 = Municipio("SC", "Florianopolis")   # SC
m8 = Municipio("SC", "Joinville")
m9 = Municipio("SC", "Blumenau")
m10 = Municipio("SC", "Chapeco")
m11 = Municipio("SC", "Criciuma")
m12 = Municipio("PR", "Curitiba")       # PR
m13 = Municipio("PR", "Londrina")
m14 = Municipio("PR", "Maringa")
m15 = Municipio("PR", "Ponta Grossa")
m16 = Municipio("PR", "Cascavel")

# RIO GRANDE DO SUL

# CADASTRO BAIRROS PORTO ALEGRE
b1 = Bairro("RS", "Porto Alegre", "Cidade Baixa", "Inacessível", "3.5", "Urgente", "Não", "Não")
b2 = Bairro("RS", "Porto Alegre", "Bom Fim", "Acessível", "0", "Seguro", "Sim", "Sim")
b3 = Bairro("RS", "Porto Alegre", "Centro", "Parcialmente Acessível", "1.2", "Crítico", "Não", "Não")
b4 = Bairro("RS", "Porto Alegre", "Harmonia", "Parcialmente Acessível", "2.0", "Urgente", "Sim", "Sim")
b5 = Bairro("RS", "Porto Alegre", "Fatima", "Inacessível", "4.0", "Urgente", "Não", "Não")
# CADASTRO BAIRROS ALVORADA
b6 = Bairro("RS", "Alvorada", "Jardim Algarve", "Acessível", "0", "Seguro", "Sim", "Sim")
b7 = Bairro("RS", "Alvorada", "Americana", "Inacessível", "3.0", "Crítico", "Não", "Não")
b8 = Bairro("RS", "Alvorada", "Formoza", "Parcialmente Acessível", "1.5", "Urgente", "Sim", "Não")
b9 = Bairro("RS", "Alvorada", "Bela Vista", "Acessível", "0", "Seguro", "Sim", "Sim")
b10 = Bairro("RS", "Alvorada", "Aparecida", "Parcialmente Acessível", "2.2", "Crítico", "Não", "Não")
# CADASTRO BAIRROS CACHOEIRINHA
b11 = Bairro("RS", "Cachoeirinha", "Vista Alegre", "Acessível", "0", "Seguro", "Sim", "Sim")
b12 = Bairro("RS", "Cachoeirinha", "Centro", "Inacessível", "4.5", "Urgente", "Não", "Não")
b13 = Bairro("RS", "Cachoeirinha", "Cohab", "Parcialmente Acessível", "1.7", "Crítico", "Não", "Não")
b14 = Bairro("RS", "Cachoeirinha", "Fatima", "Acessível", "0", "Seguro", "Sim", "Sim")
b15 = Bairro("RS", "Cachoeirinha", "Imbuí", "Inacessível", "3.8", "Urgente", "Não", "Não")
# CADASTRO BAIRROS CANOAS
b16 = Bairro("RS", "Canoas", "Centro", "Inacessível", "3.2", "Urgente", "Não", "Não")
b17 = Bairro("RS", "Canoas", "Rio Branco", "Acessível", "0", "Seguro", "Sim", "Sim")
b18 = Bairro("RS", "Canoas", "Fatima", "Parcialmente Acessível", "1.3", "Crítico", "Sim", "Não")
b19 = Bairro("RS", "Canoas", "Mathias Velho", "Parcialmente Acessível", "0.5", "Urgente", "Sim", "Não")
b20 = Bairro("RS", "Canoas", "Harmonia", "Inacessível", "4.1", "Crítico", "Não", "Não")
# CADASTRO BAIRROS GUAIBA
b21 = Bairro("RS", "Guaiba", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b22 = Bairro("RS", "Guaiba", "Cohab", "Inacessível", "4.2", "Urgente", "Não", "Não")
b23 = Bairro("RS", "Guaiba", "Colina", "Parcialmente Acessível", "1.9", "Crítico", "Sim", "Não")
b24 = Bairro("RS", "Guaiba", "Florida", "Parcialmente Acessível", "0.8", "Urgente", "Não", "Não")
b25 = Bairro("RS", "Guaiba", "São Francisco", "Inacessível", "3.6", "Crítico", "Não", "Não")
# CADASTRO BAIRROS GRAVATAI
b26 = Bairro("RS", "Gravatai", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b27 = Bairro("RS", "Gravatai", "Neopolis", "Inacessível", "3.9", "Urgente", "Não", "Não")
b28 = Bairro("RS", "Gravatai", "Santa Cruz", "Parcialmente Acessível", "1.8", "Crítico", "Sim", "Não")
b29 = Bairro("RS", "Gravatai", "Cadiz", "Parcialmente Acessível", "0.6", "Urgente", "Não", "Não")
b30 = Bairro("RS", "Gravatai", "Parque Itacolomi", "Inacessível", "4.0", "Crítico", "Não", "Não")

# SANTA CATARINA

#CADASTRO BAIRROS FLORIANOPOLIS
b31 = Bairro("SC", "Florianopolis", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b32 = Bairro("SC", "Florianopolis", "Trindade", "Parcialmente Acessível", "1.5", "Crítico", "Sim", "Não")
b33 = Bairro("SC", "Florianopolis", "Ingleses", "Inacessível", "3.7", "Urgente", "Não", "Não")
b34 = Bairro("SC", "Florianopolis", "Estreito", "Acessível", "0", "Seguro", "Sim", "Sim")
b35 = Bairro("SC", "Florianopolis", "Lagoa da Conceição", "Parcialmente Acessível", "2.1", "Urgente", "Sim", "Não")
# CADASTRO BAIRROS JOINVILLE
b36 = Bairro("SC", "Joinville", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b37 = Bairro("SC", "Joinville", "Iririu", "Parcialmente Acessível", "1.8", "Crítico", "Sim", "Não")
b38 = Bairro("SC", "Joinville", "Aventureiro", "Inacessível", "4.0", "Urgente", "Não", "Não")
b39 = Bairro("SC", "Joinville", "Comasa", "Acessível", "0", "Seguro", "Sim", "Sim")
b40 = Bairro("SC", "Joinville", "Paranaguamirim", "Parcialmente Acessível", "2.5", "Urgente", "Não", "Não")
# CADASTRO BAIRROS BLUMENAU
b41 = Bairro("SC", "Blumenau", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b42 = Bairro("SC", "Blumenau", "Velha", "Parcialmente Acessível", "1.6", "Crítico", "Sim", "Não")
b43 = Bairro("SC", "Blumenau", "Garcia", "Inacessível", "3.5", "Urgente", "Não", "Não")
b44 = Bairro("SC", "Blumenau", "Fortaleza", "Acessível", "0", "Seguro", "Sim", "Sim")
b45 = Bairro("SC", "Blumenau", "Ponta Aguda", "Parcialmente Acessível", "2.0", "Urgente", "Sim", "Não")
# CADASTRO BAIRROS CHAPECO
b46 = Bairro("SC", "Chapeco", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b47 = Bairro("SC", "Chapeco", "Passos Fortes", "Parcialmente Acessível", "1.9", "Crítico", "Sim", "Não")
b48 = Bairro("SC", "Chapeco", "Eldorado", "Inacessível", "4.2", "Urgente", "Não", "Não")
b49 = Bairro("SC", "Chapeco", "Presidente Médici", "Acessível", "0", "Seguro", "Sim", "Sim")
b50 = Bairro("SC", "Chapeco", "Jardim Italia", "Parcialmente Acessível", "2.3", "Urgente", "Não", "Não")
# CADASTRO BAIRROS CRICIUMA
b51 = Bairro("SC", "Criciuma", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b52 = Bairro("SC", "Criciuma", "Santa Luzia", "Parcialmente Acessível", "1.7", "Crítico", "Sim", "Não")
b53 = Bairro("SC", "Criciuma", "Prospera", "Inacessível", "3.9", "Urgente", "Não", "Não")
b54 = Bairro("SC", "Criciuma", "Pinheirinho", "Acessível", "0", "Seguro", "Sim", "Sim")
b55 = Bairro("SC", "Criciuma", "Rio Maina", "Parcialmente Acessível", "2.2", "Urgente", "Sim", "Não")

# PARANÁ
 
# CADASTRO BAIRROS CURITIBA
b56 = Bairro("PR", "Curitiba", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b57 = Bairro("PR", "Curitiba", "Batel", "Parcialmente Acessível", "1.8", "Crítico", "Sim", "Não")
b58 = Bairro("PR", "Curitiba", "Agua Verde", "Inacessível", "3.4", "Urgente", "Não", "Não")
b59 = Bairro("PR", "Curitiba", "Mercês", "Acessível", "0", "Seguro", "Sim", "Sim")
b60 = Bairro("PR", "Curitiba", "Cabral", "Parcialmente Acessível", "2.1", "Urgente", "Sim", "Não")
# CADASTRO BAIRROS LONDRINA
b61 = Bairro("PR", "Londrina", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b62 = Bairro("PR", "Londrina", "Jardim Piza", "Parcialmente Acessível", "1.9", "Crítico", "Sim", "Não")
b63 = Bairro("PR", "Londrina", "Vila Nova", "Inacessível", "4.1", "Urgente", "Não", "Não")
b64 = Bairro("PR", "Londrina", "Gleba Palhano", "Acessível", "0", "Seguro", "Sim", "Sim")
b65 = Bairro("PR", "Londrina", "Jardim Sol", "Parcialmente Acessível", "2.3", "Urgente", "Sim", "Não")
# CADASTRO BAIRROS MARINGA
b66 = Bairro("PR", "Maringa", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b67 = Bairro("PR", "Maringa", "Zona Sete", "Parcialmente Acessível", "1.5", "Crítico", "Sim", "Não")
b68 = Bairro("PR", "Maringa", "Jardim Alvorada", "Inacessível", "3.8", "Urgente", "Não", "Não")
b69 = Bairro("PR", "Maringa", "Vila Operaria", "Acessível", "0", "Seguro", "Sim", "Sim")
b70 = Bairro("PR", "Maringa", "Parque Itaipu", "Parcialmente Acessível", "2.0", "Urgente", "Sim", "Não")
# CADASTRO BAIRROS PONTA GROSSA
b71 = Bairro("PR", "Ponta Grossa", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b72 = Bairro("PR", "Ponta Grossa", "Uvaranas", "Parcialmente Acessível", "1.6", "Crítico", "Sim", "Não")
b73 = Bairro("PR", "Ponta Grossa", "Oficinas", "Inacessível", "3.9", "Urgente", "Não", "Não")
b74 = Bairro("PR", "Ponta Grossa", "Jardim Carvalho", "Acessível", "0.5", "Seguro", "Sim", "Sim")
b75 = Bairro("PR", "Ponta Grossa", "Nova Russia", "Parcialmente Acessível", "1.8", "Crítico", "Sim", "Não")
# CADASTRO BAIRROS CASCAVEL
b76 = Bairro("PR", "Cascavel", "Centro", "Acessível", "0", "Seguro", "Sim", "Sim")
b77 = Bairro("PR", "Cascavel", "Coqueiral", "Parcialmente Acessível", "1.5", "Crítico", "Sim", "Não")
b78 = Bairro("PR", "Cascavel", "Cancelli", "Inacessível", "3.3", "Urgente", "Não", "Não")
b79 = Bairro("PR", "Cascavel", "Santa Cruz", "Acessível", "0.7", "Seguro", "Sim", "Sim")
b80 = Bairro("PR", "Cascavel", "Country", "Parcialmente Acessível", "2.2", "Urgente", "Sim", "Não")

# LISTA DE BAIRROS
lista_bairros = [
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16,  # RS
    b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30,   # RS
    b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43,        # SC
    b44, b45, b46, b47, b48, b49, b50,b51, b52, b53, b54, b55,              # SC
    b56, b57, b58, b59, b60, b61, b62, b63, b64, b65, b66, b67, b68,        # PR
    b69, b70, b71, b72, b73, b74, b75, b76, b77, b78, b79, b80              # PR
]

menu()  # INICIALIZA O SISTEMA