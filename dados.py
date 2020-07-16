import json

def criando_json(dado):
    with open('dados221.json','w', encoding='utf8') as n:
        json.dump(dado,n,ensure_ascii=False, indent=4, separators=(','':'))


dados5 = {'nome':'washington',
         'idade':'35',
         'Linguagem Favorita':'Python'
         }
criando_json(dados5)

#with open('dados221.json','r',encoding='utf8') as z:
#    print(z.read())

