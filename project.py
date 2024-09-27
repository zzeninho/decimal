def horarios(a):
    #função para retornar o horario de trabalho pois tem diferencia cada
    print('horario:\n 7:00 as 17:00 == 1 \n 7:30 as 17:30 == 2')
    ponto =int(input('qual você escolhe?'))
    return ponto
def sexta(a):
    #função para retornar se o dia é sexta pois sexta paga mais
    sexta =str(input('é sexta(s/n)?'))
    return sexta
def saida(bsaida, saida): #colocar  a saida para funcionar
    minutos = 0
    if saida >= bsaida :   
        saida -= bsaida
    if saida >= 100:
        while saida >= 100:
            saida -= 100
            minutos += 60
    minutos += saida
    resultado = (minutos/60)     
    return resultado 
def entrada(bentrada, entrada, resultado):
    add = 0
    resutado = resultado
    if entrada < bentrada:
        while entrada != bentrada:
            entrada += 1 
            add += 1
            if entrada == 660 or entrada == 560 or entrada == 460:
                entrada -= 60
                entrada += 100
    resutado += (add/60)
    print('o total é {:.2f}'.format(resutado))

horarios = horarios(0)
sexta = sexta(0)

#o h da variavel significa hora
hentrada = float(input('qual foi o horario de entrada:'))
hsaida =float(input('qual foi o horario de saida:'))

if horarios == 1 and sexta == "n":
    Bentrada = 700
    Bsaida = 1700
    resulsaida = saida(Bsaida, hsaida)
    entrada(Bentrada, hentrada,resulsaida)

if horarios == 2 and sexta == "n":
    Bentrada = 730
    Bsaida = 1730
    resulsaida = saida(Bsaida, hsaida)
    entrada(Bentrada, hentrada,resulsaida)

if horarios == 1 and sexta == "s":
    Bentrada = 700
    Bsaida = 1600
    resulsaida = saida(Bsaida, hsaida)
    entrada(Bentrada, hentrada,resulsaida)

if horarios == 2 and sexta == "s":
    Bentrada = 730
    Bsaida = 1630
    resulsaida = saida(Bsaida, hsaida)
    entrada(Bentrada, hentrada,resulsaida)