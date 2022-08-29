import math

my_file = open('input4.txt', 'r')
output_file = open('output4.txt', 'w')

for file in my_file:
    a, b = map(int, file.split())
    sq = int(math.sqrt(a))
    if sq*sq < a:
        sq += 1
    counter = 0
    while sq*sq <= b:
        sq += 1
        counter += 1
    output_file.write(str(counter) + '\n')
    
    