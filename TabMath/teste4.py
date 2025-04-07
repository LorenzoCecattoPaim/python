namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

# Carregar o arquivo XML
tree = ET.parse('TabMath/outros/43250495111100000282550010000506571578321826-nfe.XML')
root = tree.getroot()

# Localizar os elementos no XML
nome_engenho = root.find(".//nfe:emit/nfe:xNome", namespaces)
cliente = root.find(".//nfe:dest/nfe:xNome", namespaces)
nota_fiscal = root.find(".//nfe:ide/nfe:nNF", namespaces)
fardos = root.find(".//nfe:transp/nfe:vol/nfe:qVol", namespaces)
infCpl = root.find(".//nfe:infAdic/nfe:infCpl", namespaces)

# Exibir os valores encontrados
if nome_engenho is not None and infCpl is not None:
    print(f"Nome do Engenho: {nome_engenho.text}")
    print(f"Cliente: {cliente.text}")
    print(f"Nota Fiscal: {nota_fiscal.text}")
    print(f"Fardos: {fardos.text}")
    
    # Extrair o nome do motorista
    start_motorista = infCpl.text.find("Motorista:") + len("Motorista: ")
    end_motorista = infCpl.text.find(";;", start_motorista)
    nome_motorista = infCpl.text[start_motorista:end_motorista]
    print(f"Motorista: {nome_motorista}")
    time.sleep(5)
    py.click(x=42, y=181)
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