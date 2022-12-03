import os

os.chdir(os.path.dirname(__file__))

def find_common_items(item_1,item_2):
    for character in item_1:
        for c in range(len(item_2)):
            if character == item_2[c]:
                common_item = character
    return common_item
                
def convert_item_to_priority(item):
    priority_ranking = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return priority_ranking.find(item) + 1

sum_priority  = 0
with open ('input.txt', 'r') as fle:
    for line in fle:
        half = int(len(line)/2)
        compartment_1 = line.strip()[:half]
        compartment_2 = line.strip()[half:]
        sum_priority += convert_item_to_priority(find_common_items(compartment_1,compartment_2))
print(sum_priority)








# Rules:
# All items of a given type are meant to go into exactly one of the two compartments.
# Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
# first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

# Ex: The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# To help prioritize item rearrangement, every item type can be converted to a priority:

#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.

# Find the item type that appears in both compartments of each rucksack.
