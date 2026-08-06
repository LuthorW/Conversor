import os
from PIL import Image

pasta_origem = "imagens_originais"
pasta_destino = "fotos" 

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)
    
arquivos = os.listdir(pasta_origem)
conversoes_feitas = 0

print("Iniciando a conversão...")

for arquivo in arquivos:
    if arquivo.lower().endswith(('.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.avif', '.tiff', '.png')):
        caminho_completo = os.path.join(pasta_origem, arquivo)
        
        try:
            img = Image.open(caminho_completo)

            nome_sem_extensao = os.path.splitext(arquivo)[0]
            novo_caminho = os.path.join(pasta_destino, f"{nome_sem_extensao}.png")
            
            img.convert("RGBA").save(novo_caminho, "PNG")
            
            print(f"Sucesso: {arquivo} -> {nome_sem_extensao}.png")
            conversoes_feitas += 1
            
        except Exception as e:
            print(f"Erro ao converter {arquivo}: {e}")

print(f"{conversoes_feitas} imagens foram convertidas para PNG com sucesso!")