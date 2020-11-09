import re
import time
from bot import wppbot

bot = wppbot('robozin')
#bot.treina('treino')
#bot.inicia('Ti isprico')
#bot.inicia('MOTOROLA CUSTOM ROMs')
#bot.inicia('grupoteste')
bot.inicia('Rick')
bot.saudacao(['Bot: Oi, sou o robozin','Bot: Use :: no início para falar comigo'])
ultimo_texto = ''



while True:
    time.sleep(1)
    texto = bot.escuta()
   
    
    if texto != ultimo_texto and re.match(r'^::', texto):

        ultimo_texto = texto
        texto = texto.replace('::', '')
        texto = texto.lower()

        if (texto == 'aprender' or texto == ' aprender' or texto == 'ensinar' or texto == ' ensinar'):
            bot.aprender(texto,'bot: Escreva a pergunta e após o ? a resposta.','bot: Obrigado por ensinar! Agora já sei!','bot: Você escreveu algo errado! Comece novamente..')
        elif (texto == 'noticias' or texto == ' noticias' or texto == 'noticia' or texto == ' noticia' or texto == 'notícias' or texto == ' notícias' or texto == 'notícia' or texto == ' notícia'):
            bot.noticias()
        elif (texto == 'mega-sena' or texto == 'sena'):
            bot.mega()
        elif (texto == 'default'):
            bot.default()
        else:
            palavra = str(texto)            
            palavra = palavra.replace('+', '')
            palavra = palavra.replace('-', '')
            palavra = palavra.replace('%', '')
            palavra = palavra.replace('@', '')
            palavra = palavra.replace('=', '')
            palavra = palavra.replace('/', '')
            
            bot.responde(palavra)
            #bot.default()