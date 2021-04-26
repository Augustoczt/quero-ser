resp = 's'
soma = 0
quant = 0 
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int (input('DIGITE UM NUMERO:'))
    soma = soma + num
    quant = quant + 1
    if quant == 1: 
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    

    resp = str (input('QUER CONTINUAR? [S/N]  ')).upper().strip()[0]
    media = soma / quant
print ('Voce digitou {} numeros e a média foi {}'.format(quant, media))
print ('O maior valor foi {} e o menor   valor foi {}'.format(maior, menor))
