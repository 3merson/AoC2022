import os

os.chdir(os.path.dirname(__file__))

elfs={}
elf_counter=1
line_num = 0
with open ('input.txt', 'r') as fle:
    for line in fle:
        if line == '\n':
            elfs[f'Elf{elf_counter}'] = line_num
            line_num = 0
            elf_counter+= 1
            continue
        else: 
            line_num = int(line.strip()) + line_num
        
list_of_calories = []

for key in elfs:
    list_of_calories.append(elfs[key])

list_of_calories.sort(reverse=True)

#Max
print(f'Highest amount of calories carried by one Elf: {list_of_calories[0]}')

#Max(Top 3)
print(f'Total Calories carried by Top 3 Elfs: {list_of_calories[0]+list_of_calories[1]+list_of_calories[2]}')


