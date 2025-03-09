import os

# Define o diretório atual como o diretório de trabalho
diretorio = os.getcwd()

# Lista todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Percorre cada arquivo no diretório
for arquivo in arquivos:
    try:
        # Tenta converter o nome do arquivo (sem extensão) para inteiro
        # Remove a extensão do arquivo usando splitext
        nome_sem_extensao = os.path.splitext(arquivo)[0]
        
        # Se o nome não for numérico, vai para o except
        numero = int(nome_sem_extensao)
        
        # Verifica se o número é 0 ou múltiplo de 8
        if numero != 0 and numero % 8 != 0:
            # Remove o arquivo se não atender aos critérios
            os.remove(arquivo)
            print(f"Arquivo '{arquivo}' apagado")
        else:
            print(f"Arquivo '{arquivo}' mantido (é 0 ou múltiplo de 8)")
            
    except ValueError:
        # Se o nome do arquivo não for um número, apaga o arquivo
        os.remove(arquivo)
        print(f"Arquivo '{arquivo}' apagado (não é número)")
    except Exception as e:
        # Trata outros possíveis erros
        print(f"Erro ao processar '{arquivo}': {str(e)}")

print("Processamento concluído!")