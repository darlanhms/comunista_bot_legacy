import twitter
import random
import math

#credenciais tweetdev
api = twitter.Api(consumer_key='',
                consumer_secret='',
                access_token_key='',
                access_token_secret='')

def initContador():
    with open('palavrasUsadas.txt', encoding='utf8', mode='r') as u:
        #quantidade de palavras totais no txt
        quantidadePalavras = 28091

        #quantidade de palavras usadas
        palavrasUsadas = len(u.readlines())

        #formula para pegar a porcentagem
        porcentagemUsada = palavrasUsadas * 100 / quantidadePalavras

        #formatação da porcentagem
        porcentagemFinal = round(porcentagemUsada, 5)

        #calculo de dias restantes
        dias  = math.floor((quantidadePalavras - palavrasUsadas) / 24)

        #montagem do tweet e post
        frase = f'O bot já jogou {palavrasUsadas} palavras do helicóptero. Isso corresponde a {porcentagemFinal}% do dicionário. Faltam {dias} dias para o bot chamar o dicionário inteiro de comunista.'
            
        #enfim posta o status no twitter
        api.PostUpdate(frase)
        print('executou')

initContador()