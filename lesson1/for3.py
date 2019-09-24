counts = [
    {'school_class': '4a', 'scores': [3,4,5,5,2]}, 
    {'school_class': '4b', 'scores': [2,3,4,5,4]}, 
    {'school_class': '4c', 'scores': [3,4,2,2,2]}
    ]
summa_class = 0
summa_school = 0
quantity = 0
for s_class in range(len(counts)):
    for count_number in counts[s_class]['scores']:
        summa_class += count_number
        quantity += 1
    print('Среднее по классу: ', summa_class/len(counts[s_class]['scores']))
    summa_school += summa_class
    summa_class = 0
print('Среднее по школе:', summa_school/quantity)