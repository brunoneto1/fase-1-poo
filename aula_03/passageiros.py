import xml.etree.ElementTree as ET

class ExtratorDadosXML:
    def __init__(self, arquivo_xml):
        self.arquivo_xml = arquivo_xml

    def extrair_dados(self):
        tree = ET.parse(self.arquivo_xml)
        root = tree.getroot()
        passageiros = root.findall('passageiro')

        num_passageiros = len(passageiros)
        origens_destinos = []

        for passageiro in passageiros:
            nome = passageiro.find('nome').text
            origem = passageiro.find('origem').text
            destino = passageiro.find('destino').text
            origens_destinos.append((nome, origem, destino))

        return num_passageiros, origens_destinos


xml_filename = "passageiros.xml"

extrator = ExtratorDadosXML(xml_filename)
num_passageiros, origens_destinos = extrator.extrair_dados()

print(f"Número de passageiros: {num_passageiros}")
print("Origens e destinos:")
for nome, origem, destino in origens_destinos:
    print(f"Nome: {nome}, Origem: {origem}, Destino: {destino}")
