import os

os.chdir(os.path.dirname(__file__))

def get_range(range_num:str):
    seperator = range_num.find('-')
    start = int(range_num[:seperator])
    end = int(range_num[seperator+1:])
    range_list = []
    for i in range(start,end+1):
        range_list.append(i)
    return set(range_list)

overlap = 0
empty_set = set()
with open ('input.txt', 'r') as fle:
    for line in fle:
        section_id_full = line.strip().split(",")
        section_id_1 = section_id_full[0]
        section_id_2 = section_id_full[1]
        if not list(get_range(section_id_1).intersection(get_range(section_id_2))) == []:
            overlap+=1
print(overlap)