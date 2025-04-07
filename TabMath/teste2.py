import xml.etree.ElementTree as ET
import pyautogui as py
import time
import os


def extrair(arquivo, casa):
    namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}


    tree = ET.parse(arquivo)
    root = tree.getroot()


    nome_engenho = root.find(".//nfe:emit/nfe:xNome", namespaces)
    cliente = root.find(".//nfe:dest/nfe:xNome", namespaces)
    nota_fiscal = root.find(".//nfe:ide/nfe:nNF", namespaces)
    fardos = root.find(".//nfe:transp/nfe:vol/nfe:qVol", namespaces)
    infCpl = root.find(".//nfe:infAdic/nfe:infCpl", namespaces)


    if nome_engenho is not None and infCpl is not None:
        print(f"Nome do Engenho: {nome_engenho.text}")
        print(f"Cliente: {cliente.text}")
        print(f"Nota Fiscal: {nota_fiscal.text}")
        print(f"Fardos: {fardos.text}")
        

        start_motorista = infCpl.text.find("Motorista:") + len("Motorista: ")
        end_motorista = infCpl.text.find(";;", start_motorista)
        nome_motorista = infCpl.text[start_motorista:end_motorista]
        print(f"Motorista: {nome_motorista}")
        time.sleep(1)
        py.press('win')
        time.sleep(3)
        py.write('Edge')
        time.sleep(1)
        py.press('Enter')
        time.sleep(3)
        py.write('https://docs.google.com/spreadsheets/d/120Jov_99o9hjdWyMTS8YJnGQXfaPyxelPfVgvaL_3ww/edit?gid=0#gid=0')
        time.sleep(5)
'''
        py.click(x=45, y=181)
        py.write(casa)
        py.press('Enter')
        py.write(nota_fiscal.text)
        py.press('Tab')
        time.sleep(2)
        py.write(nome_engenho.text)
        py.press('Tab')
        time.sleep(2)
        py.write(nome_motorista)
        py.press('Tab')
        time.sleep(2)
        py.write(nota_fiscal.text)
        py.press('Tab')
        time.sleep(2)
        py.write(fardos.text)
        py.press('Tab')
        time.sleep(2)
        py.write(cliente.text)
        py.press('Tab')
        time.sleep(2)
        py.press('Enter')
    else:
        print("Dados não encontrados no arquivo XML!")
pasta = "TabMath/outros"
cont = 1
arquivos = os.listdir(pasta)
for arquivo in arquivos:
    cont += 1
    print(cont)
    extrair("TabMath/outros/" + arquivo, casa= 'A' + str(cont))
'''