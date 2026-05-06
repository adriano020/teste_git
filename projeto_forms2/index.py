from tkinter import*
from tkinter import ttk
from tkinter import messagebox

#janela principal
janela = Tk()
janela.title("Cadastro de Pacientes")
janela.geometry("500x500")

##notebook (abas)
abas = ttk.Notebook(janela)
abas.pack(fill="both", expand = True)

#aba1 - Cadastro
aba1 = Frame(abas)
abas.add(aba1, text="Cadastro de pacientes")

#aba2 - Tabela
aba2 = Frame(abas)
abas.add(aba2, text="Pacientes Cadastrados")

## Função Cadastrar

def cadastrar():
    nome_completo = entry_nome_completo.get()
    cpf = entry_cpf.get()
    data_nascimento = entry_data_nascimento.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio = entry_convenio.get()
    contato_urgencia = entry_contato_urgencia.get()

    if nome_completo == "" or cpf == "" or data_nascimento == "" or telefone == "" or email == "" or convenio == "" or contato_urgencia == "":
        messagebox.showwarning("erro", "preencha todos os campos!")
    else:
        tabela.insert("", END, values=(nome_completo, cpf, data_nascimento, telefone, email, convenio, contato_urgencia,))
        entry_nome_completo.delete(0, END)
        entry_cpf.delete(0, END)
        entry_data_nascimento.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_convenio.delete(0, END)
        entry_contato_urgencia.delete(0, END)

        messagebox.showinfo("Sucesso","Paciente cadastrado!")

## Aba Cadastro

Label(aba1, text="nome_completo").pack(pady=7)
entry_nome_completo = Entry(aba1, width=40)
entry_nome_completo.pack()

Label(aba1, text="cpf").pack(pady=7)
entry_cpf = Entry(aba1, width=20)
entry_cpf.pack()

Label(aba1, text="Data_Nascimento").pack(pady=7)
entry_data_nascimento = Entry(aba1, width=20)
entry_data_nascimento.pack()

Label(aba1, text="telefone").pack(pady=7)
entry_telefone = Entry(aba1, width=20)
entry_telefone.pack()

Label(aba1, text="email").pack(pady=7)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="convenio").pack(pady=7)
entry_convenio = Entry(aba1, width=20)
entry_convenio.pack()

Label(aba1, text="contato urgencia").pack(pady=7)
entry_contato_urgencia = Entry(aba1, width=20)
entry_contato_urgencia.pack()

Button(
    aba1,
    text="cadastrar",
    bg="green",
    fg="white",
    width=20,
    command=cadastrar
).pack(pady=20)

## Aba tabela
colunas = ("nome_completo", "cpf", "data_nascimento", "telefone", "email", "convenio", "contato_urgencia")

tabela = ttk.Treeview(
    aba2,
    columns = colunas,
    show = "headings"
)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack(fill="both", expand=True,pady=20)

janela.mainloop()

