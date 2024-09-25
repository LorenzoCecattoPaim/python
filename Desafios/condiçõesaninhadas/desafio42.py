med1=float(input('Qual a medida de um lado do seu triângulo? '))
med2=float(input('Qual a medida do outro lado do seu triângulo? '))
med3=float(input('Qual a  3º medida do lado do seu triângulo? '))
if med1 < med2 + med3 and med2 <med1 + med3 and med3 < med1 + med2:
    print('Os segmentos acima PODEM formar um triângulo!')
    if med1==med2==med3:
        print('EQUILÁTERO')
    elif med1!=med2!=med3!=med1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')