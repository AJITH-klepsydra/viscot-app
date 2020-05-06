import requests
import matplotlib.pyplot as plt
import url1

def convert(number):
    accum = 0
    numbers = number.split(',')
    for i in numbers:
        accum = accum * 100 + int(i)
    return accum
k=url1.k
if(k==1):
    info = requests.get('https://www.worldometers.info/coronavirus/').text






    lines = info.split('\n')
    flag = 0
    confirmed = ''
    recovered = ''
    death = ''
    for line in lines:
        if flag == 1:
            flag = 0
            words = line.split('>')
            recovered = words[1].split('<')[0]
        if line.startswith('<title>'):
            words = line.split()
            confirmed = words[words.index('Cases')-1]
            death = words[words.index('Deaths')-1]

        if line.startswith('<div class="maincounter-number" style="color:#8ACA2B ">'):
            flag = 1




confirmed1 = [x for x in confirmed if x!=',']
confirmed = ''
for y in confirmed1:
    confirmed += y 
death1 = [x for x in death if x!=',']
death=''
for y in death1:
    death += y 
recovered1 = [x for x in recovered if x!=',']
recovered =''
for y in recovered1:
    recovered += y 
confirmed=int(confirmed)
death=int(death)
recovered=int(recovered)
