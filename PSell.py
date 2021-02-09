"""

Sergio Luis Franzin Junior

Avaliação Prática do Processo Seletivo
Tecnologia da Informação
Raccoon Marketing Digital
Janeiro de 2021

"""

import xml.etree.ElementTree as ET #Essa bibliboteca é para lidar com arquivos .xml
import requests #Essa bibliboteca é para puxar os dados do arquivo .xml de um web-service, tive que instalar esse pacote por meio de um pip, essa biliboteca tambem vai me ajudar com a requisição POST

url="https://storage.googleapis.com/psel-2021/soleng%26backoffice/Psel2021.xml" #O domínio do arquivo .xml
header = { 'Accept': 'application/xml' } #Estou mostrando que vai ser um arquivo do tipo .xml
r = requests.get(url, headers=header) #Estou puxando os dados para minha máquina
 
tree =  ET.ElementTree(ET.fromstring(r.content)) #Não entendi muito bem, mas parece que estou transformando o conteúdo de r em string

root = tree.getroot() #É sobre a hierarquia

#Para manipular os dados, coloquei eles em um dicionário com o algoritmo abaixo, cada chave contém todos os dados de um empregado

Empregados = {}
aux = []
x = 0

for n in root.findall("employee"): 
    
    for nome in n.findall("name"):
        aux.append(nome.text)
    for CPF in n.findall("CPF"):
        aux.append(CPF.text)
    for salário in n.findall("salary"):
        aux.append(int(salário.text))
    for posição in n.findall("position"):
        aux.append(posição.text)
    for status in n.findall("marital_status"):
        aux.append(status.text)
    
    x+=1
    Empregados[x] = aux
    aux = []

###################################################################################################################################################
    
"""
Exercício 1
Ordene os funcionários por salário de forma decrescente.
"""

lista = [] #Essa lista vai guardar as informações dos funcionários na mesma ordem que estão no arquivo .xml

for i in Empregados:
    lista.append(Empregados[i])

#O algortimo abaixo ordena números de forma crescente

listaaux = [] #Essa lista vai guardar as informações em ordem crescente de salário
flag = False

for k in range (len(lista)):
    tamanho = len(listaaux)
    m = lista[k][2]

    if( tamanho > 0 ):
        for y in range(tamanho):
            if (m <= listaaux[y][2]):
                listaaux.insert(y, lista[k])
                flag = True
                break

    if((k == 0) or (flag == False)):
        listaaux.append(lista[k])

    else:
        flag = False


listaaux2=listaaux[::-1] #inverti a lista para ordem descrecente de salário

print('Funcionários ordenados por salário de forma decrescente:\n')
print('%21s'%('Empregado'), '  Salário')

response1=[] #vou usar na resposta no arquivo .json

for a in range (len(listaaux2)):
    response1.append(listaaux2[a][0])
     
    print('%21s'%listaaux2[a][0], "  R$ %i,00"%listaaux2[a][2])

###################################################################################################################################################

"""
Exercício 2
Liste a quantidade de funcionários que há em cada cargo, ordenando os cargos em ordem alfabética.
"""

analistas = [] #Essa lista vai guardar os dados dos analistas
coordenadores = [] #Essa lista vai guardar os dados dos coordenadores
diretores = [] #Essa lista vai guardar os dados dos diretores
gerentes = [] #Essa lista vai guardar os dados dos gerentes


for j in range(len(listaaux)): #Usei a listaaux pq já esta em ordem crescente de salário, vou usar isso no exercício 3
    if listaaux[j][3] == 'ANALISTA':
        analistas.append(listaaux[j])

    elif listaaux[j][3] == 'COORDENADOR':
        coordenadores.append(listaaux[j])

    elif listaaux[j][3] == 'DIRETOR':
        diretores.append(listaaux[j])

    else:
        gerentes.append(listaaux[j])


print()
print('********************************************************************************************************************************************')
print()
print('Quantidade de funcionários que há em cada cargo:\n')
print('Número de Analistas: ', len(analistas))
print('Número de Coordenadores: ', len(coordenadores))
print('Número de Diretores: ', len(diretores))
print('Número de Gerentes: ', len(gerentes))
print()
print('********************************************************************************************************************************************')

response2a = len(analistas) #Vou usar essas respostas no arquivo .json
response2c = len(coordenadores)
response2d = len(diretores)
response2g = len(gerentes)

###################################################################################################################################################

"""
Exercício 3
Retorne as informações dos 5 Coordenadores casados com menor salário, em ordem crescente de salário.
"""

coordcas = [] #Essa lista vai guardar os dados dos coordenadores casados

for q in range(len(coordenadores)): #A lista de coordenadores já esta em ordem crescente de salário, como dito no exercício 2
    if coordenadores[q][4] == 'CASADO':
        coordcas.append(coordenadores[q])

print()
print('Informações dos 5 Coordenadores casados com menor salário, em ordem crescente de salário:\n')
print('Nome', '%20s'%('CPF'), '%23s'%('Salário'), '%15s'%('Posição'), '%22s'%('Estado civil')) 

response3 = [] #vou usar na resposta no arquivo .json

for h in range (5):
    response3.append(coordcas[h])
    print('%17s'%coordcas[h][0], '%18s'%coordcas[h][1], '     R$ %i,00'%coordcas[h][2], '%16s'%coordcas[h][3], '%12s'%coordcas[h][4])

###################################################################################################################################################

"""
Exercício 4
Valide todos os CPFs dos funcionários que não são coordenadores casados, listando os possíveis estados deles caso o CPF seja válido, se não retorne uma lista vazia; não altere a ordem original dos dados.
"""

validar = [] #Essa lista guarda os dados dos funcionários que não são coordenadores casados

for z in range(len(lista)):
    if lista[z][3]!= 'COORDENADOR':
        validar.append(lista[z])       

    else:
        if lista[z][4]!='CASADO':
            validar.append(lista[z])

print()
print('********************************************************************************************************************************************')
print()
print('Validade dos CPFs dos funcionários que não são coordenadores casados e possíveis estados:\n')

response4 = [] #Vou usar essa lista no arquivo .json
        
for w in range(len(validar)):

    elem = validar[w][1]
    A = int(elem[0])
    B = int(elem[1])
    C = int(elem[2])
    D = int(elem[4])
    E = int(elem[5])
    F = int(elem[6])
    G = int(elem[8])
    H = int(elem[9])
    I = int(elem[10])

    JJ = int(elem[12])
    KK = int(elem[13])

    soma1 = 10*A+9*B+8*C+7*D+6*E+5*F+4*G+3*H+2*I
    resto1 = soma1%11

    if resto1 == 0 or resto1 == 1:
        J = 0

    else:
        J = 11 - resto1

    soma2 = 11*A+10*B+9*C+8*D+7*E+6*F+5*G+4*H+3*I+2*J
    resto2 = soma2%11

    if resto2 == 0 or resto2 == 1:
        K = 0

    else:
        K = 11 - resto2

    sinal = False

    if JJ == J and KK == K:
        sinal = True
        print('CPF válido: %i%i%i.%i%i%i.%i%i%i-%i%i'%(A,B,C,D,E,F,G,H,I,J,K))
              
        if I == 0:
            print('Jurisdição: RS')            
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['RS']))          

        elif I == 1:
            print('Jurisdição: DF, GO, MT, MS e TO')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['DF', 'GO', 'MT', 'MS', 'TO']))

        elif I == 2:
            print('Jurisdição: AC, AM, AP, PA, RO e RR')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['AC', 'AM', 'AP', 'PA', 'RO', 'RR']))

        elif I == 3:
            print('Jurisdição: CE, MA e PI')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['CE', 'MA', 'PI']))

        elif I == 4:
            print('Jurisdição: AL, PB, PE e RN')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['AL', 'PB', 'PE', 'RN']))

        elif I == 5:
            print('Jurisdição: BA e SE')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['BA', 'SE']))

        elif I == 6:
            print('Jurisdição: MG')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = 'MG'))

        elif I == 7:
            print('Jurisdição: ES e RJ')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['ES', 'RJ']))

        elif I == 8:
            print('Jurisdição: SP')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['SP']))

        else:
            print('Jurisdição: PR e SC')
            response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = ['PR', 'SC']))

        print()
    else:
        print('CPF inválido: %i%i%i.%i%i%i.%i%i%i-%i%i'%(A,B,C,D,E,F,G,H,I,J,K))
        print()

        response4.append(dict(valid_cpf = sinal, name = validar[w][0], CPF = validar[w][1], possibles_origin = []))
        
        
###################################################################################################################################################

"""
Exercício 5
Retornar qual o custo total para a empresa dos funcionários que estão no cargo de Analista.
"""

custo = 0

for t in range(len(analistas)):
    custo = custo + int(analistas[t][2])

custototal = custo*1.95
response5 = custototal #resposta para o arquivo .json

print('********************************************************************************************************************************************')
print()
print('O custo total para a empresa dos funcionários que estão no cargo de Analista é de R$ %.2f'%custototal)

###################################################################################################################################################


#Opcional

"""
Soma do salário por cargo
"""

an = 0
di = 0
co = 0
ge = 0

for t1 in range(len(analistas)):
    an = an + int(analistas[t1][2])

for t2 in range(len(diretores)):
    di = di + int(diretores[t2][2])

for t3 in range(len(coordenadores)):
    co = co + int(coordenadores[t3][2])

for t4 in range(len(gerentes)):
    ge = ge + int(gerentes[t4][2])


print()
print('********************************************************************************************************************************************')
print()
print('Soma dos salários por cargo:\n')
print('Analistas: R$ %i,00'%an)
print('Coordenadores: R$ %i,00'%co)
print('Gerentes: R$ %i,00'%ge)
print('Diretores: R$ %i,00'%di)
print()
print('********************************************************************************************************************************************')
print()

"""
Quantidade de funcionários cujo sobrenome inicia com a letra P
"""

listaP = [] #Vai armazenar os funcionários cujo sobrenome inicia com a letra
espaço = ord(' ')

for p1 in range(len(lista)):

    for p2 in range(len(lista[p1][0])):

        nomeP = lista[p1][0]
        caracter =(nomeP[p2])

        if ord(caracter) == espaço:

            caracter2 =(nomeP[p2+1])

            if caracter2 == 'P':

                listaP.append(lista[p1])
                break
            
            else:
                
                break

print('Quantidade de funcionários cujo sobrenome inicia com a letra P: ',len(listaP))
print('\nnomes:\n')

for v in range (len(listaP)):
      print(listaP[v][0])
print()
print('********************************************************************************************************************************************')
print()

###################################################################################################################################################

import json #Essa bibliboteca é para lidar com arquivos .json

#Coloquei as respostas no formato solicitado

dados={
"api_key" : "ca523c5b-c198-4c96-ac58-5bc3e40f1b1f",
"full_name" : "Sergio Luis Franzin Junior",
"email" : "sergio.franzin@raccoon.ag",
"code_link" : "https://github.com/SergioFranzin/PSel",
"response_1" : response1,
"response_2" : {
    "analista" : response2a,
    "coordenador" : response2c,
    "diretor" : response2d,
    "gerente" : response2g,
},
"response_3" : response3,
"response_4" : response4,
"response_5" : response5,
}

#Enviando as respostas por requerimento POST

api_token = 'ca523c5b-c198-4c96-ac58-5bc3e40f1b1f'
api_url = 'https://us-central1-psel-solution.cloudfunctions.net/first-2021'

header2 = { 'Content-Type': 'application/json',
            'Authorization': 'token {}'.format(api_token)}

r2 = requests.post(api_url, data=json.dumps(dados),  headers=header2)

print(r2.status_code) #Verifiquei se a requisição foi bem-sucedida, cod. 200

z = input('\nAperte qualquer tecla para sair')










