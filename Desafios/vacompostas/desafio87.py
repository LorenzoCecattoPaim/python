matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=tcol=mai=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um número para a posição [{l} , {c}]:'))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 ==0:
            soma+=matriz[l][c]
        if c==2:
            tcol+=matriz[l][c]
        if l==1:
            mai=matriz[l][c]
            if matriz[l][c]>mai:
                mai=matriz
    print()
print(f'A soma dos números pares é {soma}')
print(f'A soma dos números da 3º coluna é {tcol}')
for c in range(0,3):
    if c == 0:
        mai=matriz[1][c]
    elif matriz[1][c] > mai:
        mai=matriz[1][c]
print(f'O maior número da 2ª linha é {mai}')
# 2 linha: 1:0, 1:1, 1:2
