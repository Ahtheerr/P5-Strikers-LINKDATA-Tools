import tkinter as tk
from tkinter import filedialog, messagebox
import os

def extrair_dados_hex(arquivo_origem, arquivo_destino, offset_inicio, offset_fim):
    try:
        with open(arquivo_origem, 'rb') as exe_file:
            exe_file.seek(offset_inicio)
            tamanho = offset_fim - offset_inicio + 1
            dados = exe_file.read(tamanho)
        
        with open(arquivo_destino, 'wb') as idx_file:
            idx_file.write(dados)
        
        messagebox.showinfo("Success", f"Extracted to {arquivo_destino}")
    except PermissionError:
        messagebox.showerror("Permission error", f"Without permission to create {arquivo_destino}. Try other folder or open as admin.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract: {e}")

def importar_dados_hex(arquivo_origem, arquivo_idx, offset_inicio):
    try:
        with open(arquivo_idx, 'rb') as idx_file:
            dados = idx_file.read()
        
        with open(arquivo_origem, 'r+b') as exe_file:
            exe_file.seek(offset_inicio)
            exe_file.write(dados)
        
        messagebox.showinfo("Success", f"Data imported to {arquivo_origem}")
    except PermissionError:
        messagebox.showerror("Permission error", f"No permission to modify {arquivo_origem}. Try other file or open as admin.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to import data: {e}")

class GerenciadorArquivos:
    def __init__(self, root):
        self.root = root
        self.root.title("Program")
        self.root.geometry("400x250")
        
        self.arquivo_exe = None
        self.arquivo_idx = None
        self.offset_inicio = 0x01970520
        self.offset_fim = 0x019E159F
        
        # Label para o arquivo .exe
        self.label_exe = tk.Label(root, text="No .exe selected")
        self.label_exe.pack(pady=5)
        
        # Botão para selecionar o .exe
        self.btn_selecionar_exe = tk.Button(root, text="Select the game.exe", command=self.selecionar_arquivo_exe)
        self.btn_selecionar_exe.pack(pady=5)
        
        # Label para o arquivo LINKDATA.IDX
        self.label_idx = tk.Label(root, text="No LINKDATA.IDX selected")
        self.label_idx.pack(pady=5)
        
        # Botão para extrair
        self.btn_extrair = tk.Button(root, text="Extract LINKDATA.IDX", command=self.extrair, state="disabled")
        self.btn_extrair.pack(pady=5)
        
        # Botão para importar
        self.btn_importar = tk.Button(root, text="Inject LINKDATA.IDX", command=self.importar, state="disabled")
        self.btn_importar.pack(pady=5)
        
        # Botão para sair
        self.btn_sair = tk.Button(root, text="Quit", command=root.quit)
        self.btn_sair.pack(pady=5)

    def selecionar_arquivo_exe(self):
        self.arquivo_exe = filedialog.askopenfilename(
            title="Select the .exe",
            filetypes=[("EXE", "*.exe")]
        )
        if self.arquivo_exe:
            self.label_exe.config(text=f"EXE: {os.path.basename(self.arquivo_exe)}")
            self.btn_extrair.config(state="normal")
            self.btn_importar.config(state="normal")
        else:
            self.label_exe.config(text="No .exe selected")
            self.btn_extrair.config(state="disabled")
            self.btn_importar.config(state="disabled")

    def extrair(self):
        if not self.arquivo_exe:
            messagebox.showwarning("Warning", "Select a .exe first!")
            return
        
        # Pergunta onde salvar o LINKDATA.IDX
        self.arquivo_idx = filedialog.asksaveasfilename(
            title="Save LINKDATA.IDX",
            defaultextension=".idx",
            initialfile="LINKDATA.IDX",
            filetypes=[("IDX Files", "*.idx"), ("Every file", "*.*")]
        )
        if self.arquivo_idx:
            self.label_idx.config(text=f"IDX: {os.path.basename(self.arquivo_idx)}")
            extrair_dados_hex(self.arquivo_exe, self.arquivo_idx, self.offset_inicio, self.offset_fim)
        else:
            self.label_idx.config(text="No LINKDATA.IDX selected")

    def importar(self):
        if not self.arquivo_exe:
            messagebox.showwarning("Warning", "Select the .exe first!")
            return
        
        # Pergunta qual LINKDATA.IDX usar para importar
        self.arquivo_idx = filedialog.askopenfilename(
            title="Select LINKDATA.IDX",
            filetypes=[("IDX", "*.idx"), ("Every file", "*.*")]
        )
        if self.arquivo_idx:
            self.label_idx.config(text=f"IDX: {os.path.basename(self.arquivo_idx)}")
            importar_dados_hex(self.arquivo_exe, self.arquivo_idx, self.offset_inicio)
        else:
            messagebox.showwarning("Warning", "No LINKDATA.IDX selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorArquivos(root)
    root.mainloop()