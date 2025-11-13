import customtkinter as ctk
import sqlite3 as sq
import platform

so = platform.system()

#configurando o banco de dados
conn = sq.connect("databases/database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS extrato (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor REAL, description TEXT, option TEXT)")

def puxar_extrato():
    cursor.execute("SELECT nome, valor, description, option FROM extrato ORDER BY id DESC")
    puxada_resultado = cursor.fetchall()
    return puxada_resultado

if so == "Darwin":
    ctk.set_widget_scaling(0.9)   # aumenta tamanho geral dos widgets
    ctk.set_window_scaling(1.1)   # aumenta janela e texto

a = "San Francisco"

#criar o aplicativo
janela = ctk.CTk()
janela.title("Organização Monetaria - By Antunes")
janela.geometry("1700x900")
janela.resizable(False,False)
janela.iconbitmap("images/icone.ico")
janela._set_appearance_mode("dark")

def destruir():
    for widget in janela.winfo_children():
        widget.destroy()


def tela_dashboard():
    destruir()

    bar_frame = ctk.CTkFrame(janela, width=1700, height=50, fg_color="#022200")
    bar_frame.place(x=0, y=0)

    extrato_frame = ctk.CTkScrollableFrame(janela, width=250, height=700, fg_color="#2f2f2f")
    extrato_frame.place(relx=0.15, rely=0.63, anchor="center")

    for nome, valor, description, option in puxar_extrato():
        if option == "VENDA":
            item = ctk.CTkLabel(extrato_frame, text=f"+R${valor} | {nome}", fg_color="green", corner_radius=10)
            item.pack(pady=3)
        else:
            item = ctk.CTkLabel(extrato_frame, text=f"-R${valor} | {nome}", fg_color="red", corner_radius=10)
            item.pack(pady=3)

    extrato_title = ctk.CTkLabel(janela, text="Seu extrato", font=(a, 20))
    extrato_title.place(relx=0.15, rely=0.2, anchor="center")

    adicionar_entrada = ctk.CTkButton(bar_frame, text="Adicione uma entrada", font=(a, 20), fg_color="#0A3E0F", command=tela_add_entrada)
    adicionar_entrada.place(relx=0.02, rely=0.2)

    remover_entrada = ctk.CTkButton(bar_frame, text="Remova entrada", font=(a, 20), fg_color="#0A3E0F", command=tela_remove_entrada)
    remover_entrada.place(relx=0.15, rely=0.2)

    botao_analisar = ctk.CTkButton(bar_frame, text="Analisar extrato", font=(a, 20), fg_color="#0A3E0F", command=tela_analisar_extrato)
    botao_analisar.place(relx=0.255, rely=0.2)


def tela_add_entrada():
    destruir()

    option_var = ctk.StringVar(value="")

    botao_voltar = ctk.CTkButton(janela, text="Voltar",width=200, height=50, fg_color="#620000", command=tela_dashboard)
    botao_voltar.place(relx=0.5, rely=0.9, anchor="center")

    box_frame = ctk.CTkFrame(janela, width=400, height=600, fg_color="#2f2f2f", corner_radius=10)
    box_frame.place(relx=0.5, rely=0.5, anchor="center")

    titulo = ctk.CTkLabel(janela, text="Adicione sua entrada", font=(a,40))
    titulo.place(relx=0.5, rely=0.13, anchor="center")

    nome_prompt = ctk.CTkEntry(box_frame, placeholder_text="Digite o nome da entrada", width=300, height=40, font=(a,20))
    nome_prompt.place(relx=0.5, rely=0.1, anchor="center")

    valor_prompt = ctk.CTkEntry(box_frame, placeholder_text="Digite o valor da entrada", width=300, height=40, font=(a,20))
    valor_prompt.place(relx=0.5, rely=0.2, anchor="center")

    description_prompt = ctk.CTkEntry(box_frame, placeholder_text="Digite uma descrição", width=300, height=40, font=(a,20))
    description_prompt.place(relx=0.5, rely=0.3, anchor="center")

    aviso_label = ctk.CTkLabel(box_frame, text="", text_color="#620000")
    aviso_label.place(relx=0.5, rely=0.8, anchor="center")

    frame_venda = ctk.CTkFrame(box_frame, width=100, height=40, corner_radius=10, fg_color="green")
    frame_venda.place(relx=0.3, rely=0.4, anchor="center")
    button_venda = ctk.CTkRadioButton(box_frame, text="Venda", value="VENDA", corner_radius=10, fg_color="green", font=(a,13), variable=option_var)
    button_venda.place(relx=0.3, rely=0.4, anchor="center")

    frame_compra = ctk.CTkFrame(box_frame, width=100, height=40, corner_radius=10, fg_color="green")
    frame_compra.place(relx=0.65, rely=0.4, anchor="center")
    button_compra = ctk.CTkRadioButton(box_frame, text="Compra", value="COMPRA", fg_color="green", font=(a,13), variable=option_var)
    button_compra.place(relx=0.65, rely=0.4, anchor="center")



    def enviar_entrada():
        nome = nome_prompt.get()
        try:
            valor = float(valor_prompt.get())
        except:
            aviso_label.configure(text="Digite apenas numeros")

        description = description_prompt.get()
        try:
            if option_var.get() == "VENDA":
                option = "VENDA"
            elif option_var.get() == "COMPRA":
                option = "COMPRA"
        except:
            aviso_label.configure(text="Selecione uma opção")
        cursor.execute("INSERT INTO extrato (nome, valor, description, option) VALUES (?,?,?,?)", (nome, valor, description, option))
        conn.commit()
        tela_dashboard()


    botao_enviar = ctk.CTkButton(box_frame, text="Enviar", width=300, height=50, font=(a,10), corner_radius=10, command=enviar_entrada)
    botao_enviar.place(relx=0.5, rely=0.9, anchor="center")

def tela_remove_entrada():
    destruir()

def tela_analisar_extrato():
    destruir()


tela_dashboard()

janela.mainloop()