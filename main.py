import customtkinter as ctk
import sqlite3 as sq

#configurando o banco de dados
conn = sq.connect("databases/database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, senha TEXT)")

#criar o aplicativo
janela = ctk.CTk()
janela.title("Organização Monetaria - By Antunes")
janela.geometry("1700x900")
janela.resizable(False,False)
janela.iconbitmap("images/icone.ico")

    
def tela_inicial():
    titulo = ctk.CTkLabel(janela, text="Organizador Monetario", width=300, height=50, font=("San Francisco", 30))
    titulo.place(x=700, y=350)
    botao_continue = ctk.CTkButton(janela, text="Continue", fg_color="#3078AB", corner_radius=10, font=("San Francisco", 20))
    botao_continue.place(relx=0.5, y=420, anchor="center")

tela_inicial()

janela.mainloop()