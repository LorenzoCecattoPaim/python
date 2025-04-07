import xml.etree.ElementTree as ET
import pyautogui as py
import time



namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

tree = ET.parse('TabMath/43250495111100000282550010000506581406664811-nfe.XML')
root = tree.getroot()

nome_engenho = root.find(".//nfe:emit/nfe:xNome", namespaces)
Cliente = root.find(".//nfe:dest/nfe:xNome", namespaces)
NotaF = root.find(".//nfe:ide/nfe:nNF", namespaces)
Fardos = root.find(".//nfe:transp/nfe:vol/nfe:qVol", namespaces)
Motorista = root.find(".//nfe:infAdic/nfe:infCpl", namespaces)


if nome_engenho is not None:
    print(f"Nome do engenho: {nome_engenho.text}")
    print(f"Nota Fiscal: {NotaF.text}")
    print(f"Cliente: {Cliente.text}")
    print(f"Motorista: {nome_engenho.text}")
    print(f"Placa: {nome_engenho.text}")
    print(f"Fardos: {Fardos.text}")
    print(f"Motorista: {Motorista.text}")
    nome_motora = Motorista.text.find('Motorista')
else:
    print("Valor Total não encontrado!")

infCpl = root.find(".//nfe:infAdic/nfe:infCpl").text

# Extrai o nome do motorista
start_motorista = infCpl.find("Motorista:") + len("Motorista: ")
end_motorista = infCpl.find(";;", start_motorista)
nome_motorista = infCpl[start_motorista:end_motorista]

# Extrai as placas
placas = []
for label in ["Placa 2:", "Placa 3:"]:
    start_placa = infCpl.find(label) + len(label)
    end_placa = infCpl.find(" ", start_placa)
    placas.append(infCpl[start_placa:end_placa])

# Exibe os resultados
print("Nome do Motorista:", nome_motorista)
print("Placas:", placas)
"""
time.sleep(5)
py.click(x=42, y=181)
py.write(NotaF.text)
py.press('Tab')
time.sleep(2)
py.write(nome_engenho.text)
py.press('Tab')
time.sleep(2)
py.write(NotaF.text)
py.press('Tab')
time.sleep(2)
py.write(NotaF.text)
py.press('Tab')
time.sleep(2)
py.write(Fardos.text)
py.press('Tab')
time.sleep(2)
py.write(Cliente.text)
py.press('Tab')
time.sleep(2)
py.press('Enter')
"""