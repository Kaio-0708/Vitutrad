from googletrans import Translator
from gtts import gTTS
import os

def main():
    while True:
        print("Escolha uma opção:")
        print("1- Traduzir")
        print("2- Finalizar")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            texto_em_portugues = input("Digite um texto em português: ")
            print("Escolha o idioma para traduzir:")
            print("1- Inglês")
            print("2- Espanhol")
            print("3- Francês")
            print("4- Italiano")
            
            idioma_opcao = input("Digite a opção do idioma desejado: ")
            
            if idioma_opcao == '1':
                idioma_destino = 'en'
            elif idioma_opcao == '2':
                idioma_destino = 'es'
            elif idioma_opcao == '3':
                idioma_destino = 'fr'
            elif idioma_opcao == '4':
                idioma_destino = 'it'
            else:
                print("Opção de idioma inválida! Traduzindo para inglês por padrão.")
                idioma_destino = 'en'
                
            texto_traduzido = traduzir_texto(texto_em_portugues, idioma_destino)
            falar_texto(texto_traduzido, idioma_destino)
        
        elif opcao == '2':
            print("Finalizando")
            break
        else: 
            print("Opção inválida! Tente novamente.")

def traduzir_texto(texto, idioma_destino):
    tradutor = Translator()
    traducao = tradutor.translate(texto, src='pt', dest=idioma_destino)
    texto_traduzido = traducao.text
    print(f"Tradução para o idioma escolhido: {texto_traduzido}")
    return texto_traduzido

def falar_texto(texto, idioma_destino):
    tts = gTTS(texto, lang=idioma_destino)
    tts.save("traducao.mp3")
    os.system("start traducao.mp3")  

if __name__ == "__main__":
    main()