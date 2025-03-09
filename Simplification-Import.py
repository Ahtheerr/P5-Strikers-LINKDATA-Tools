import tkinter as tk
from tkinter import filedialog
import os

# Função principal
def importar_textos_modificados():
    # Abre o gerenciador de arquivos para selecionar o arquivo TSV
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    caminho_tsv = filedialog.askopenfilename(
        title="Select the TSV",
        filetypes=[("TSV", "*.tsv"), ("Every file", "*.*")]
    )
    
    if not caminho_tsv:
        print("No TSV selected.")
        return

    # Dicionário para armazenar as modificações por arquivo
    modificacoes = {}
    
    # Lê o arquivo TSV
    with open(caminho_tsv, 'r', encoding='utf-8') as arquivo_tsv:
        linhas_tsv = arquivo_tsv.readlines()
        
        for linha in linhas_tsv:
            colunas = linha.strip().split('\t')
            if len(colunas) >= 4:  # Verifica se há pelo menos 4 colunas
                nome_arquivo = colunas[0]
                numero_linha = int(colunas[1]) - 1  # Converte para índice (base 0)
                texto_modificado = colunas[3]  # 4ª coluna (índice 3)
                
                # Adiciona ao dicionário
                if nome_arquivo not in modificacoes:
                    modificacoes[nome_arquivo] = {}
                modificacoes[nome_arquivo][numero_linha] = texto_modificado
    
    if not modificacoes:
        print("No modification found.")
        return
    
    # Processa cada arquivo de origem
    pasta_origem = os.path.dirname(caminho_tsv)  # Assume que os arquivos estão na mesma pasta do TSV
    arquivos_modificados = 0
    
    for nome_arquivo, alteracoes in modificacoes.items():
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
        
        if not os.path.exists(caminho_arquivo):
            print(f"Original file not found: {caminho_arquivo}")
            continue
        
        # Lê o arquivo original
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_origem:
            linhas_origem = arquivo_origem.readlines()
        
        # Aplica as modificações
        for indice, texto_modificado in alteracoes.items():
            if 0 <= indice < len(linhas_origem):
                linhas_origem[indice] = texto_modificado + '\n'  # Substitui a linha, mantendo a quebra
        
        # Salva o arquivo modificado
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_origem:
            arquivo_origem.writelines(linhas_origem)
        
        arquivos_modificados += 1
        print(f"Modified file: {caminho_arquivo} ({len(alteracoes)} lines modified)")
    
    print(f"\nDone. Number of edited files: {arquivos_modificados}")

# Executa o script
if __name__ == "__main__":
    importar_textos_modificados()