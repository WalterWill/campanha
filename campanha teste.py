bronze = int(30)
prata = int(60)
ouro = int(120)
adamantium = int(250)
apoiadores = int(18)
valor = int(2500)
cont = int(0)
dinheiro = int(0)
a = int(0)
b = int(0)
c = int(0)
d = int(0)
avalor = int(0)
bvalor = int(0)
cvalor = int(0)
dvalor = int(0)
poss = int(0)

#Abre o arquivo calculos.txt
arq = open('calculos.txt', 'w' , encoding="utf8")

while a != apoiadores and b != apoiadores and c != apoiadores and d != apoiadores :
    print('Iniciou Codigo')

    #Calculo Bronze
    if a < apoiadores :
        a = a + 1

    if a == apoiadores :
        a = 0
        b = b + 1

    #Calculo Prata
    if b == apoiadores :
        b = 0
        c = c + 1

    #Calculo Ouro
    if c == apoiadores :
        c = 0
        d = d + 1

    #Equações
    dinheiro = int((a*bronze)+(b*prata)+(c*ouro)+(d*adamantium))
    cont = int(a+b+c+d)

    #Verificação

    if dinheiro == valor and cont == apoiadores:
        poss = poss + 1
        avalor = int(a * bronze)
        bvalor = int(b * prata)
        cvalor = int(c * ouro)
        dvalor = int(d * adamantium)
        arq.write("%s %d\n" %('cont:', cont))
        arq.write("%s %d\n" %('dinheiro:', dinheiro))
        arq.write("%s %d %s %d\n" %('a:', a, '=', avalor))
        arq.write("%s %d %s %d\n" %('b:', b, '=', bvalor))
        arq.write("%s %d %s %d\n" %('c:', c, '=', cvalor))
        arq.write("%s %d %s %d\n" %('d:', d, '=', dvalor))
        arq.write("%s %d\n" %('possibilidade:', poss))
        arq.write('==========\n')

    #Mostra as variaveis e seus resultados
    print('Fim do Loop')
    print('Cont=',cont)
    print('Dinheiro=',dinheiro)
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
    print('Possibilidades=',poss)

#Fecha o arquivo calculos.txt
arq.close()
if a == apoiadores and b == apoiadores and c == apoiadores and d == apoiadores :
    print('Fim do Script')
    print('Cont=', cont)
    print('Dinheiro=', dinheiro)
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
    print('Possibilidades=', poss)