#PROJETO - Gerador de Senhas - Aplicativo com Interface Gráfica

import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha():
    tamanho = int(entry_tamanho.get())
    incluir_maiusculas = var_maiusculas.get()
    incluir_minusculas = var_minusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_especiais = var_especiais.get()

    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += "!@#$%^&*()"

    if not caracteres:
        messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere!")
        return

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        root.update()
        messagebox.showinfo("Copiar", "Senha copiada para a área de transferência!")

#Janela principal
root = tk.Tk()
root.title("Gerador de Senhas Seguras")

#Tamanho da senha
tk.Label(root, text="Tamanho da senha:").grid(row=0, column=0, padx=10, pady=10)
entry_tamanho = tk.Entry(root)
entry_tamanho.grid(row=0, column=1, padx=10, pady=10)

#Opções dos caracteres
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_especiais = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Letras maiúsculas", variable=var_maiusculas).grid(row=1, column=0, columnspan=2)
tk.Checkbutton(root, text="Letras minúsculas", variable=var_minusculas).grid(row=2, column=0, columnspan=2)
tk.Checkbutton(root, text="Números", variable=var_numeros).grid(row=3, column=0, columnspan=2)
tk.Checkbutton(root, text="Caracteres especiais", variable=var_especiais).grid(row=4, column=0, columnspan=2)

#Botões
tk.Button(root, text="Gerar Senha", command=gerar_senha).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Copiar Senha", command=copiar_senha).grid(row=5, column=1, padx=10, pady=10)

#Exibe a senha gerada
entry_senha = tk.Entry(root, width=30)
entry_senha.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
