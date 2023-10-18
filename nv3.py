import time
import sys
import requests

print("Opa! C chegou até aqui? Caraca, agora adivinhe a senha.")
print("Porque só sei que nada sei. \nVá para o primeiro cmd e coloque a senha: 11 de setembro")

# Receba a entrada do usuário
resposta = input("Digite a senha: ")

# Verifique se a senha está correta
if resposta == "Sócrates":
    print("Haha, foi esperto, hein?")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Acesso concedido!")

    # Seu código que você deseja escrever no arquivo nv4.py
    codigo_nv4 = """import time
import sys
import requests

print("Caraca agora só falta 2 levels!")
# Receba a entrada do usuário
resposta = input("Digite a senha: ")

# Verifique se a senha está correta
if resposta == "TEXTO":
    print("Acesso concedido!")
    time.sleep(1)
    print("Usou photoshop ou oq? haha")
    time.sleep(2)

"""

    # Nome do arquivo que você deseja criar
    nome_do_arquivo_nv4 = "nv4.py"

    # Escreva o código no arquivo
    with open(nome_do_arquivo_nv4, "w") as arquivo_nv4:
        arquivo_nv4.write(codigo_nv4)

    print(f"Arquivo {nome_do_arquivo_nv4} criado com sucesso!")

else:
    print("Senha incorreta! Acesso negado.")
    sys.exit()
