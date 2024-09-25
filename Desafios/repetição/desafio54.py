import datetime
data=datetime.date.today().year
tot=0
totme=0
for i in range(1,8):
    nas=int(input('Em que ano a {}º pessoa nasceu? '.format(i)))
    idade=(data)-(nas)
    if idade>21:
        tot+=1
    else:
        totme+=1
print('{} são de maior e {} não são!'.format(tot,totme))
