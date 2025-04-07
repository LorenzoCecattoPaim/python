import xml.etree.ElementTree as ET
import pyautogui as py
import time


def arquivo(arquivo):
    namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

    tree = ET.parse(arquivo)
    root = tree.getroot()

    nome_engenho = root.find(".//nfe:emit/nfe:xNome", namespaces)
    Cliente = root.find(".//nfe:dest/nfe:xNome", namespaces)
    NotaF = root.find(".//nfe:ide/nfe:nNF", namespaces)
    Fardos = root.find(".//nfe:transp/nfe:vol/nfe:qVol", namespaces)
    if nome_engenho is not None:
        print(f"Nome do engenho: {nome_engenho.text}")
        print(f"Nota Fiscal: {NotaF.text}")
        print(f"Cliente: {Cliente.text}")
        print(f"Motorista: {nome_engenho.text}")
        print(f"Placa: {nome_engenho.text}")
        print(f"Fardos: {Fardos.text}")
    else:
        print("Valor Total não encontrado!")
    return nome_engenho.text, Cliente.text, NotaF.text, Fardos.text

def colocar(NotaF,nome_engenho,Fardos,Cliente):
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


arquivo('TabMath/43250495111100000282550010000506581406664811-nfe.XML')


