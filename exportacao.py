import os
import csv
import json

# verificar o formato
# garantir q a pasta existe
# abrir o arquivo e escrever os dados dentro do arquivo

def exportar(dados, nome_arquivo, formato):
    pasta = "dados"
    os.makedirs(pasta, exist_ok=True)  # verifica se a pasta "dados" existe, caso não exista essa função cria a pasta

    caminho = os.path.join(pasta, nome_arquivo)  # Caminho completo do arquivo

    try:
        if formato == "csv":
            # verifica se os dados estão no formado q o CSV aceita (listas ou tuplas)
            if not all(isinstance(i, (list, tuple)) for i in dados):
                raise ValueError("Os dados para CSV devem ser uma lista de listas ou tuplas.")
            with open(caminho, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(dados)

        elif formato == "json":
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4)

        elif formato == "txt":
            with open(caminho, "w", encoding="utf-8") as f:
                for linha in dados:
                    # Formata as linhas para ajudar a entender o arquivo
                    f.write(" | ".join(str(x) for x in linha) + "\n")

        #esse else nem vai ser usado, pq não tem como escolher outra opção além dessas 3 na interface
        else:
            raise ValueError("Formato não suportado. Use 'csv', 'json' ou 'txt'.")

    except Exception as e:
        print(f"Erro ao exportar dados: {e}")
        return None

    return caminho  # retorna o caminho do arquivo gerado (pra mostrar na interface)
