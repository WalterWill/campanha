bronze = 30
prata = 60
ouro = 120
adamantium = 250
apoiadores = 18
valor = 2500
cont = 0
dinheiro = 0
a = 0
b = 0
c = 0
d = 0
acont = 0
bcont = 0
ccont = 0
dcont = 0
ajuste = 0

while (cont != apoiadores) and (dinheiro != valor):
    print('Iniciou Codigo')
    while(cont < apoiadores) and (dinheiro < valor):

    #Calculo Bronze
        if acont == 0:
            while acont == 0 :
                print('Entrou Bronze')
                if (dinheiro > valor) :
                    cont = cont - 1
                    acont = 1
                    a = a - 1
                    dinheiro = dinheiro - bronze
                    print('Bronze>Dinheiro')
                if (cont > apoiadores):
                    a = a - 1
                    cont = cont - 1
                    acont = 1
                    dinheiro = dinheiro - bronze
                    print('Bronze>Apoiadores')
                else :
                    cont = cont + 1
                    a = a + 1
                    dinheiro = dinheiro + bronze
                    print('Bronze>Else')
                print('Setor Bronze')
                print('Cont=', cont)
                print('Dinheiro=', dinheiro)
                print('a=', a)
                print('b=', b)
                print('c=', c)
                print('d=', d)

    #Calculo Prata

        if acont == 1:  #verifica se a classe anterior ja encheu
            while bcont == 0 :
                print('Entrou Prata')
                if (dinheiro > valor) : #Se estrapolar o valor, é retirado 1 apoiador Bronze
                    cont = cont - 1
                    bcont = 1   #Ativa chave indicando que o dinheiro de Apoiadores Pratas ja encheu
                    a = a - 1
                    dinheiro = dinheiro - bronze
                    print('Prata>Dinheiro')
                if (cont > apoiadores):
                    a = a - 1
                    cont = cont - 1
                    dinheiro = dinheiro - bronze
                    print('Prata>Apoiadores')
                else :
                    cont = cont + 1
                    b = b + 1
                    dinheiro = dinheiro + prata
                    print('Prata>Else')

                print('Setor Prata')
                print('Cont=', cont)
                print('Dinheiro=', dinheiro)
                print('a=', a)
                print('b=', b)
                print('c=', c)
                print('d=', d)

    # Calculo Ouro

        if bcont == 1:  #verifica se a classe anterior ja encheu
            while ccont == 0 :  #Verifica se a classe atual ainda não encheu
                print('Entrou Ouro')
                if (dinheiro > valor) : #Se estrapolar o valor, é retirado 1 apoiador Bronze
                    cont = cont - 1
                    ccont = 1   #Ativa chave indicando que o dinheiro de Apoiadores Ouro ja encheu
                    a = a - 1
                    dinheiro = dinheiro - bronze
                    print('Ouro>Dinheiro')
                if (cont > apoiadores):
                    a = a - 1
                    cont = cont - 1
                    dinheiro = dinheiro - bronze
                    print('Ouro>Apoiadores')
                else :
                    cont = cont + 1
                    b = b + 1
                    dinheiro = dinheiro + prata
                    print('Ouro>Else')
                print('Setor Ouro')
                print('Cont=', cont)
                print('Dinheiro=', dinheiro)
                print('a=', a)
                print('b=', b)
                print('c=', c)
                print('d=', d)

        print('Fim do Code')
        print('Cont=',cont)
        print('Dinheiro=',dinheiro)
        print('a=',a)
        print('b=',b)
        print('c=',c)
        print('d=',d)
