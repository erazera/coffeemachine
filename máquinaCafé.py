
import time;
''' 
Etapa 0 = Esperando cliente 
Etapa 1 = Escolha o tipo de ingresso
Etapa 2 = Escolha a quantidade de ingressos
Etapa 3 = Finalizar reserva de ingressos
Etapa 4 = Forma de pagamento
Etapa 5 = Imprimir ingressos
'''
etapa = 0

'''
Forma 1 = Pagamento via cartão credito visa
Forma 2 = Pagamento via cartão credito mastercard
Forma 3 = Pagamento via cartão débito
Forma 4 = Pagamento via PIX
'''
forma_pagamento = 0

' Configuração da máquina: '
preco_inteiro = 30
preco_meio = 15
max_ingresso = 6

while True:
    if etapa == 0: 
        input("Clique na tela para iniciar sua compra ou digite alguma coisa. ")
        etapa = 1;
        
    elif etapa == 1:
        tipo_ingresso = int(input("Você deseja adquirir qual tipo de ingresso:\n(1) Ingresso-inteiro (R$ {})\n(2) Meio-ingresso (R$ {})\n".format(preco_inteiro, preco_meio)))
        if tipo_ingresso == 1 or tipo_ingresso == 2:
            etapa = 2
        else:
            print("Tipo de ingresso inválido")
        
    elif etapa == 2:
        if tipo_ingresso == 1:
            ingressos = int(input("Quantos ingressos inteiros você deseja comprar (Máximo {}): ".format(max_ingresso)))
            etapa = 3;
        else:
            ingressos = int(input("Quantos meios ingressos você deseja comprar (Máximo {}): ".format(max_ingresso)))
            etapa = 3;
    
    elif etapa == 3:
        if ingressos <= 0:
            print("Você precisa comprar pelo menos um ingresso.")
            etapa = 2
        elif ingressos > max_ingresso:
            print("Você não pode comprar mais que {} ingressos.".format(max_ingresso))
            etapa = 2
        else:
            if tipo_ingresso == 1:
                valor_total = ingressos * preco_inteiro
                print("Você está prestes a comprar {}x ingressos inteiros.".format(ingressos))
            else:
                valor_total = ingressos * preco_meio
                print("Você está prestes a comprar {}x meios ingressos.".format(ingressos))
            print("O valor total da sua compra é R$ {}.\n".format(valor_total))
            etapa = 4;
        
    
    elif etapa == 4:
        forma_pagamento = int(input("Qual a forma de pagamento desejada?\n(1) Cartão de Crédito Visa\n(2) Cartão de Crédito Mastercard\n(3) Cartão de Débito\n(4) PIX\n"))
        if forma_pagamento > 0 and forma_pagamento <= 3:
            print("Insira o seu cartão...")
            time.sleep(3)
            print("Digite a sua senha...")
            time.sleep(5)
            etapa = 5
        elif forma_pagamento == 4:
            print("Estamos gerando o QR-Code para sua compra...")
            time.sleep(2)
            print("Código gerado, aguardando pagamento...")
            time.sleep(6)
            etapa = 5
        else:
            print("Forma de pagamento inválida.")
    elif etapa == 5:
        print("Sua compra foi aprovada com sucesso. Retire seus ingressos")
        time.sleep(2)
        etapa = 0;
            
            
        
        
