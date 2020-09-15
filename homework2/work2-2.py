with open('referat.txt', 'r', encoding='utf-8') as test:
    print(len(test.read()))
    
print(len(set(open(r'referat.txt').read().split())))

with open('referat.txt', 'r', encoding='utf-8') as f:
    f = f.read().replace('.', '!')
    my_file = open('referat2.txt', 'w')
    my_file.write(f)
    my_file.close()