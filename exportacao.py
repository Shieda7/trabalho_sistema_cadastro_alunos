import os
import csv
import json

def exportar(dados, nome_arquivo, formato):
    pasta = "dados"
    os.makedirs(pasta, exist_ok=True)  # Cria a pasta 'dados', se não existir

    caminho = os.path.join(pasta, nome_arquivo)  # Caminho completo do arquivo

    try:
        if formato == "csv":
            # Verifique se os dados estão no formato adequado para CSV (listas ou tuplas)
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
                    # Formata cada linha para melhorar a legibilidade
                    f.write(" | ".join(str(x) for x in linha) + "\n")

        else:
            raise ValueError("Formato não suportado. Use 'csv', 'json' ou 'txt'.")

    except Exception as e:
        print(f"Erro ao exportar dados: {e}")
        return None

    return caminho  # Retorna o caminho do arquivo gerado
