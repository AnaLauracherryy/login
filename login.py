import tkinter as tk
from banco import Banco
from tkinter import messagebox
from PIL import image, ImageTk

class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x400")


        try:
            img = Image.open("Image/pimentinha.jpg")
            img = img.resize((250, 250))
            self.photo = ImageTk.PhotoImage(img)
            self.image_label = tk.Label(self.master, image=self.photo)
            self.image_label.pack(pady=20)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar a imagem: {e}")

        self.janela40 = tk.Frame(master)
        self.janela40["padx"] = 20
        self.janela40.pack()

        self.usuario_label = tk.Label(self.janela40, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = tk.Entry(self.janela40, width=20)
        self.usuario.pack(side="left")

        self.janela41 = tk.Frame(master)
        self.janela41["padx"] = 20
        self.janela41.pack()

        self.senha_label = tk.Label(self.janela41, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = tk.Entry(self.janela41, width=20, show="*")
        self.senha.pack(side="left")

        self.janela42 = tk.Frame(master)
        self.janela42["padx"] = 20
        self.janela42.pack()

        self.botao10 = tk.Button(self.janela42, width=10, text="Login", command=self.entrar)
        self.botao10.pack(side="left")
        self.new_window = None

    def entrar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        banco = Banco()
        cursor = banco.conexao.cursor()

        cursor.execute("SELECT * FROM tbl_usuarios WHERE usuario=? AND senha=?", (usuario, senha))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.abrir()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

        cursor.close()
        banco.conexao.close()

    def abrir(self):

        if self.new_window is None or not self.new_window.winfo_exists():
            self.new_window = tk.Toplevel(self.master)
            self.new_window.title("Nova Janela")
            self.new_window.geometry("400x400")


if __name__ == "__main__":
    print("Executando o script...")
    root = tk.Tk()
    root.state("zoomed")
    app = Login(master=root)
    root.mainloop()