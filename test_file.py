a = 6656.52468
b = 0
answer = hex(int(a))
a -= int(a)
answer +='.'

while b != 10 and a != 0:
    a = a * 16
    answer += hex(int(a))
    a -=int(a)

amount_count = answer.count('0x')
#for intstance in range(amount_count):
answer = answer.replace('x','',amount_count)
print(answer)
print(f'\n {amount_count}')
    



#print(hex(a))

