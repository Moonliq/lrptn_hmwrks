scrs = [
{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
{'school_class': '7b', 'scores': [3,2,3,3,3]}, 
{'school_class': '5c', 'scores': [5,5,4,5,3]}
]
srbttl = 0
scrsttl = 0
classtotal = len(scrs)
for x in scrs:
    srb =  sum(x['scores']) / len(x['scores'])
    srbttl += sum(x['scores'])
    scrsttl += len(x['scores'])
    clss = x['school_class']
    print(f'Cредняя оценка по {clss} классу {srb}')
print(f'Средий балл по школе {srbttl / scrsttl}')
