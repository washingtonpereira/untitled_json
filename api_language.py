import json

def cria_json(dado):
    with open('livros.json','w',encoding='utf8') as b:
        json.dump(dado,b,ensure_ascii=False,indent=4 , separators=(','';'))




Livro1 = {'nome_1':'Programacao em Python3',
          'Linguagem_1':"Python"}

Livro2 = {'nome_2':'Sistemas Operacionais',
          'Linguagem_2':'Java'}

Livro3 = {'nome_3':'Programacao com Java Dummies',
          'Linguagem_3':'Java'}

Livro4 = {'nome_4':'Aprendendo C++',
           'Linguagem_4':'C++'}

Livros = Livro1
Livros['nome_2']= 'Sistemas Operacionais'
Livros ['Linguagem_2'] = 'Java'
Livros['nome_3'] = 'Programação com Java Dummies'
Livros['Linguagem_3']= 'Java'
Livros ['nome_4'] = 'Aprendendo C++'
Livros['Linguagem_4'] = 'C++'

cria_json(Livros)

#with open('livros.json','r',encoding='utf8') as w:
#    print(w.read())







