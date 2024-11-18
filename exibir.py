import tkinter as tk
from tkinter import ttk

def exibir_texto():
    texto = entrada.get()
    label.config(text=f"Você digitou: {texto}")

def limpar_texto():
    entrada.delete(0, tk.END)
    label.config(text="")

janela = tk.Tk()
janela.title("Exibidor de Texto")
janela.geometry("400x200")

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

btn_exibir = tk.Button(janela, text="Exibir Texto", command=exibir_texto)
btn_exibir.pack(pady=5)

btn_limpar = tk.Button(janela, text="Limpar Texto", command=limpar_texto)
btn_limpar.pack(pady=5)

label = tk.Label(janela, text="")
label.pack(pady=10)

janela.mainloop()
