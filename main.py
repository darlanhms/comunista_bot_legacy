import twitter
import random
import threading

#twitter dev
api = twitter.Api(consumer_key='',
                consumer_secret='',
                access_token_key='',
                access_token_secret='')

palavra = ''

#timer para executas as funcoes em determinado tempo
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def buscarPalavra():
    with open('palavras.txt', encoding="utf8", mode='r') as f:
         with open('palavrasUsadas.txt', mode='a') as u:
            with open('palavrasUsadas.txt', mode='r') as ra:
                #armazena as palavras ja usadas em uma lista
                usadas = ra.readlines()
                arrayNovo = []

                #remover o \n das palavras por conta do txt
                for i in usadas:
                    novaPalavra = i.replace('\n', '')
                    arrayNovo.append(novaPalavra)

                # armazena os resultados do arquivo em uma lista
                data=f.readlines()

                #filtra para palavras para mais de 4 letras
                listaNova = list(filter(lambda item: len(item) > 4, data))

                #gera um número random que seja dentro da lista
                number = random.randint(0, len(listaNova))

                #pega a palavra na posição da lista e deixa em letras minúsculas
                palavra = listaNova[number].lower()
                
                #tira o espaço em branco da palavra
                palavra = palavra.strip()
                
                #valida se a palavra já existe no txt, pra não houver palavras repetidas
                if palavra in arrayNovo:
                    #se houver ele da recall na função até achar uma que não seja repetida
                    buscarPalavra()
                else:
                    # escreve a palavra usada em outro txt para não repetir
                    u.write(palavra + '\n')
                        
                    #enfim posta o status no twitter
                    api.PostUpdate(f'{palavra} é comunista')

 

set_interval(buscarPalavra, 600.0)

buscarPalavra()



