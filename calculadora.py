import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Definir as funções para cada botão
def somar():
    """Soma os dois números inseridos nos campos de entrada."""
    num1 = float(campo1.get())
    num2 = float(campo2.get())
    resultado = num1 + num2
    campo_resultado.delete(0, tk.END)
    campo_resultado.insert(0, resultado)

def subtrair():
    """Subtrai o segundo número inserido do primeiro."""
    num1 = float(campo1.get())
    num2 = float(campo2.get())
    resultado = num1 - num2
    campo_resultado.delete(0, tk.END)
    campo_resultado.insert(0, resultado)

def multiplicar():
    """Multiplica os dois números inseridos."""
    num1 = float(campo1.get())
    num2 = float(campo2.get())
    resultado = num1 * num2
    campo_resultado.delete(0, tk.END)
    campo_resultado.insert(0, resultado)

def dividir():
    """Divide o primeiro número inserido pelo segundo."""
    num1 = float(campo1.get())
    num2 = float(campo2.get())
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        resultado = "Divisão por zero"
    campo_resultado.delete(0, tk.END)
    campo_resultado.insert(0, resultado)

# Criar os campos de entrada para os números
campo1 = tk.Entry(janela)
campo1.grid(row=0, column=0)
campo2 = tk.Entry(janela)
campo2.grid(row=0, column=1)

# Criar os botões para as operações
botao_somar = tk.Button(janela, text="+", command=somar)
botao_somar.grid(row=1, column=0)
botao_subtrair = tk.Button(janela, text="-", command=subtrair)
botao_subtrair.grid(row=1, column=1)
botao_multiplicar = tk.Button(janela, text="*", command=multiplicar)
botao_multiplicar.grid(row=2, column=0)
botao_dividir = tk.Button(janela, text="/", command=dividir)
botao_dividir.grid(row=2, column=1)

# Criar o campo para exibir o resultado
campo_resultado = tk.Entry(janela)
campo_resultado.grid(row=3, column=0, columnspan=2)

# Exibir a janela
janela.mainloop()