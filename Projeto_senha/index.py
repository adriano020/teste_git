from tkinter import*
from tkinter import messagebox


cliente = Tk()
cliente.title("Solicitar Senha")
cliente.geometry("300x350")
cliente.configure(bg="grey")

contador = 1
fila = []
senha_atual = StringVar()
senha_atual.set("---")

admin = Toplevel(cliente)
admin.title("Administrador")
admin.geometry("300x350")
admin.configure(bg="grey")

Label(admin, text="Fila de Senhas", font=("arial", 14)).pack(pady=10)

lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

painel = Toplevel(cliente)
painel.title("Painel de Senhas")
painel.geometry("300x350")
painel.configure(bg="grey")

Label(painel, text="Senha Atual", font=("arial", 20)).pack(pady=20)

Label(
    painel,
    textvariable=senha_atual,
    font=("arial", 30),
    fg="black"
).pack(pady=20)

def solicitar_senha():
    global contador

    senha = F"A{contador:03}"
    fila.append(senha)

    lista_admin.insert(END, senha)

    messagebox.showinfo("senha gerada", f"sua senha é {senha}")

    contador += 1

def chamar_senha():
    if len(fila) == 0:
        messagebox.showwarning("aviso", "fila vazia")
    else:
        senha = fila.pop(0)

        lista_admin.delete(0)

        senha_atual.set(senha)

Label(cliente, text="Retirar Senha",font=("arial", 16)).pack(pady=20)

Button(
    cliente,
    text="gerar senha",
    width=20,
    command=solicitar_senha
).pack(pady=10)

Button(
    admin,
    text="chamar próxima",
    width=20,
    command=chamar_senha
).pack(pady=10)


cliente.mainloop()
