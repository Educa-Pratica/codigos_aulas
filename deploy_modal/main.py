# 1º Passo: Criar a conta
# 2º Passo: pip install modal
# 3º Passo: Criar a chave a API e rodar o comando no cmd
# 4º Passo: Criar arquivo .py e configurar o modal
# 5º Passo: modal run NOME_DO_ARQUIVO.py   -> Para testar a execução no ambiente modal
# 6º Passo: modal deploy NOME_DO_ARQUIVO.py

from utils.utils import get_stock_info
import modal

# 1. Definimos o ambiente (Image) que o Modal vai criar na nuvem.
# Aqui você pode instalar pacotes pip e incluir arquivos locais.
imagem_customizada = (
    modal.Image.debian_slim()
    .pip_install("requests", "yfinance") # Pip install nas bibliotecas necessárias
    # .add_local_file("utils/utils.py", remote_path="/root/utils/utils.py") # se quiser adicionar um arquivo específico
    .add_local_dir("./utils", remote_path="/root/utils") # se quiser adicionar uma pasta inteira
)

# 2. Criamos o App do Modal
app = modal.App(name="Video_YT", image=imagem_customizada)


# 3. Adicionamos o agendamento (Schedule)
@app.function(schedule=modal.Period(seconds=30)) #Garante que a função main seja executada na imagem docker do Modal a cada 45 segundos
def main():
    print("Executando o cron job...")
    get_stock_info()
    print("Cron job finalizado.")
    print("Inscreva-se no Canal do Educa Pratica!!")
    
if __name__ == "__main__":
    main()