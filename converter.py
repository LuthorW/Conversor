import os
from PIL import Image

# 1. Defina o nome das pastas
pasta_origem = "imagens_originais" # Coloque as imagens baixadas aqui
pasta_destino = "fotos"            # Onde os PNGs vão parar

# Cria a pasta de destino se ela não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# 2. Pega todos os arquivos da pasta original
arquivos = os.listdir(pasta_origem)
conversoes_feitas = 0

print("✨ Iniciando a conversão mágica...")

for arquivo in arquivos:
    # Verifica se é uma imagem (ignora outros tipos de arquivo)
    if arquivo.lower().endswith(('.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.avif', '.tiff')): # se funcionar
        caminho_completo = os.path.join(pasta_origem, arquivo)
        
        try:
            # Abre a imagem
            img = Image.open(caminho_completo)
            
            # Pega o nome do arquivo sem a extensão antiga (ex: "mal.webp" vira "mal")
            nome_sem_extensao = os.path.splitext(arquivo)[0]
            novo_caminho = os.path.join(pasta_destino, f"{nome_sem_extensao}.png")
            
            # Converte para PNG mantendo a transparência (RGBA) e salva
            img.convert("RGBA").save(novo_caminho, "PNG")
            
            print(f"✅ Sucesso: {arquivo} -> {nome_sem_extensao}.png")
            conversoes_feitas += 1
            
        except Exception as e:
            print(f"❌ Erro ao converter {arquivo}: {e}")

print(f"🎉 Fim! {conversoes_feitas} imagens foram convertidas para PNG com sucesso!")