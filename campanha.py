bronze = 30
prata = 60
ouro = 120
adamantium = 250
apoiadores = 554
valor = 36890
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

    #Calculo apoiadores Adamantium

        if dcont == 0:
            while dcont == 0:
                print('Entrou Adamantium')
                cont = cont+1
                dinheiro = dinheiro + adamantium
                d = d + 1
                if (dinheiro > valor):
                    cont = cont - 1
                    d = d - 1
                    dcont = 1
                    dinheiro = dinheiro - 250
                    print('Adamantium>Dinheiro')

                if cont > apoiadores:
                    d = d - 1
                    cont = cont - 1
                    dinheiro = dinheiro - adamantium
                    print('Adamantium>Apoiadores')

            print('Setor Adamantium')
            print('Cont=', cont)
            print('Dinheiro=', dinheiro)
            print('a=', a)
            print('b=', b)
            print('c=', c)
            print('d=', d)

        # Calculo apoiadores Ouro

        if dcont == 1 :
            while ccont == 0 :
                print('Entrou Ouro')
                cont = cont + 1
                dinheiro = dinheiro + ouro
                c = c + 1

                if (dinheiro > valor):
                        cont = cont - 1
                        d = d - 1
                        ccont = 1
                        dinheiro = dinheiro - adamantium
                        print('Ouro>dinheiro')

                if cont > apoiadores:
                        d = d - 1
                        cont = cont - 1
                        dinheiro = dinheiro - adamantium
                        print('Ouro>Apoiadores')

                print('Setor Ouro')
                print('Cont=', cont)
                print('Dinheiro=', dinheiro)
                print('a=', a)
                print('b=', b)
                print('c=', c)
                print('d=', d)

            # Calculo apoiadores Prata

        if ccont == 1:
                while bcont == 0:
                    print('Entrou Prata')
                    cont = cont + 1
                    dinheiro = dinheiro + prata
                    b = b + 1

                    if (dinheiro > valor):
                        cont = cont - 1
                        d = d - 1
                        bcont = 1
                        dinheiro = dinheiro - adamantium
                        print('Prata>dinheiro')

                    if cont > apoiadores:
                        d = d - 1
                        cont = cont - 1
                        dinheiro = dinheiro - adamantium
                        print('Prata>apoiadores')

                    print('Setor Prata')
                    print('Cont=', cont)
                    print('Dinheiro=', dinheiro)
                    print('a=', a)
                    print('b=', b)
                    print('c=', c)
                    print('d=', d)

            # Calculo apoiadores Bronze

        if bcont == 1 :
                while acont == 0 :
                    print('Entrou Bronze')
                    cont = cont + 1
                    dinheiro = dinheiro + bronze
                    a = a + 1

                    if (dinheiro > valor) :
                        cont = cont - 1
                        d = d - 1
                        acont = 1
                        dinheiro = dinheiro - adamantium
                        print('Bronze>dinheiro')

                    if cont > apoiadores:
                        d = d - 1
                        cont = cont - 1
                        dinheiro = dinheiro - adamantium
                        print('Bronze>apoiadores')

                    print('Setor Bronze')
                    print('Cont=', cont)
                    print('Dinheiro=', dinheiro)
                    print('a=', a)
                    print('b=', b)
                    print('c=', c)
                    print('d=', d)

            #Calculo de ajustes

        if acont == 1:
                while ajuste == 0 :
                    print('Estrou no setor Ajustes')

                    if (dinheiro > valor) :

                        print('Ajustes>Dinheiro')

                    if cont > apoiadores :
                        d = d - 1
                        acont = 0
                        bcont = 0
                        ccont = 0
                        cont = cont - 1
                        dinheiro = dinheiro - adamantium
                        print('Ajustes>Apoiadores')

                    else:
                        print('Ajustes>else')
                        cont = cont - 1
                        d = d - 1
                        dinheiro = dinheiro - adamantium
                        acont = 0
                        bcont = 0
                        ccont = 0


                    print('Setor ajuste')
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
