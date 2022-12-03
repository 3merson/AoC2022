import os

os.chdir(os.path.dirname(__file__))

def find_common_items(item_1,item_2,item_3):
    common_item = ''
    for character in item_1:
        for c in range(len(item_2)):
            if character == item_2[c]:
                for c3 in range(len(item_3)):
                    if character == item_3[c3]:
                        common_item = character
    return common_item
                
def convert_item_to_priority(item):
    priority_ranking = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return priority_ranking.find(item) + 1

sum_priority= 0
group = []
with open ('input.txt', 'r') as fle:
    line_counter = 0 
    for line in fle:
        group.append(line.strip())
        line_counter += 1
        if line_counter == 3:
            find_common_items(group[0],group[1],group[2]) 
            sum_priority += convert_item_to_priority(find_common_items(group[0],group[1],group[2]))
            group = []
            line_counter = 0
print(sum_priority)








# Rules:
# Every set of three lines in your list corresponds to a single group
# Each group can have a different badge item type
# Priority still the same
