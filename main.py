# passo 1 --> importar bibliotecas
import tkinter as tk
import pandas as pd
import sqlite3

# CONEXÃO COM BANCO E CRIAÇÃO DA TABELA
# conexao = sqlite3.connect('banco_clientes.db')
#
# c = conexao.cursor()
#
# c.execute(''' CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
# ''')
# conexao.commit()
#conexao.close()

def cadastrar_cliente():
    conexao = sqlite3.connect('banco_clientes.db')

    c = conexao.cursor()

    c.execute("INSERT INTO clientes VALUES(:nome, :sobrenome, :email, :telefone)",
                {
                    'nome': entry_nome.get(),
                    'sobrenome': entry_sobrenome.get(),
                    'email': entry_email.get(),
                    'telefone': entry_telefone.get()
                }
              )
    conexao.commit()

    conexao.close()

    entry_nome.delete(0,'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')

def exportar_cliente():
    conexao = sqlite3.connect('banco_clientes.db')

    c = conexao.cursor()

    c.execute("SELECT * FROM clientes")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome','sobrenome','email','telefone'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
    conexao.commit()

    conexao.close()


janela = tk.Tk()
janela.title('Cadastro de Clientes')

# Label

label_nome = tk.Label(janela, text="Nome")
label_nome.grid(row= 0, column=0, pady=10, padx=10)

label_sobrenome = tk.Label(janela, text="Sobrenome")
label_sobrenome.grid(row= 1, column=0, pady=10, padx=10)

label_email = tk.Label(janela, text="Email")
label_email.grid(row= 2, column=0, pady=10, padx=10)

label_telefone = tk.Label(janela, text="Telefone")
label_telefone.grid(row= 3, column=0, pady=10, padx=10)

# Entry

entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row= 0, column=1, pady=10, padx=10)

entry_sobrenome = tk.Entry(janela, width=30,)
entry_sobrenome.grid(row= 1, column=1, pady=10, padx=10)

entry_email = tk.Entry(janela, width=30)
entry_email.grid(row= 2, column=1, pady=10, padx=10)

entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid(row= 3, column=1, pady=10, padx=10)

# botões

botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command= cadastrar_cliente)
botao_cadastrar.grid(row= 4, column=0, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text='Exportar Cliente', command= exportar_cliente)
botao_exportar.grid(row= 5, column=0, pady=10, columnspan=2, ipadx=80)

janela.mainloop()