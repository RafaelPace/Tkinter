import tkinter as tk

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

janela.mainloop()
