import os

os.chdir(os.path.dirname(__file__))

list_of_calories = []
line_num = 0
with open ('input.txt', 'r+') as fle:
    fle.write('\n')
    for line in fle:
        if line == '\n':
            list_of_calories.append(line_num)
            line_num = 0
            continue
        else: 
            line_num = int(line.strip()) + line_num
            
list_of_calories.sort(reverse=True)

#Max
print(f'Highest amount of calories carried by one Elf: {list_of_calories[0]}')

#Max(Top 3)
print(f'Total Calories carried by Top 3 Elfs: {list_of_calories[0]+list_of_calories[1]+list_of_calories[2]}')


