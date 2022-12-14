import os
import re
# from collections import deque as LinkedList

# ll = LinkedList()
# ll.append(1)
# ll.append(2)

# for node in ll:
#     #print(node)

os.chdir(os.path.dirname(__file__))


def getMapVales(input,line_stop):
    crate_checker = []
    counter = 0
    with open (input, 'r') as fle:
        list_of_columns = []
        line_checked = 0
        for line in fle:
            column=1
            if line_checked == line_stop:
                break
            for char in range(len(line)):
                if not line[char] == '\n':
                    crate_checker.append(line[char])
                counter += 1
                if counter == 4:
                    counter = 0
                    tmp_list=[crate_checker[1],column]
                    list_of_columns.append(tmp_list)
                    crate_checker = []
                    column+=1
            line_checked+=1
    return list_of_columns

def buildMap(map_values):
    test = map_values
    column_1 = []
    column_2 = []
    column_3 = []
    column_4 = []
    column_5 = []
    column_6 = []
    column_7 = []
    column_8 = []
    column_9 = []

    for i in range(len(test)):
        # #print(test[i])
        if test[i][1] == 1:
            column_1.append(test[i][0])
        elif test[i][1] == 2:
            column_2.append(test[i][0])
        elif test[i][1] == 3:
            column_3.append(test[i][0])
        elif test[i][1] == 4:
            column_4.append(test[i][0])
        elif test[i][1] == 5:
            column_5.append(test[i][0])
        elif test[i][1] == 6:
            column_6.append(test[i][0])
        elif test[i][1] == 7:
            column_7.append(test[i][0])
        elif test[i][1] == 8:
            column_8.append(test[i][0])
        else:
            column_9.append(test[i][0])
    column_1.reverse(), column_2.reverse(), column_3.reverse(),column_4.reverse(),column_5.reverse(), column_6.reverse(), column_7.reverse(),column_8.reverse(),column_9.reverse()
    return [column_1, column_2, column_3,column_4, column_5, column_6,column_7, column_8, column_9]
    
def getColumn(column):
    c =buildMap(getMapVales('input.txt',8)) 
    if column == 1:
        return c[0]
    if column == 2:
        return c[1]
    if column == 3:
        return c[2]
    if column == 4:
        return c[3]
    if column == 5:
        return c[4]
    if column == 6:
        return c[5]
    if column == 7:
        return c[6]
    if column == 8:
        return c[7]
    if column == 9:
        return c[8]

def removeSpaces(column_space):
    new_list = []
    for i in range(len(column_space)):
        if not column_space[i] == " ": 
            new_list.append(column_space[i])
    return new_list    





def followMoves(input):
    line_num = 0
    with open (input, 'r') as fle:
        column_1 = getColumn(1) 
        column_2 = getColumn(2) 
        column_3 = getColumn(3)
        column_4 = getColumn(4) 
        column_5 = getColumn(5) 
        column_6 = getColumn(6)
        column_7 = getColumn(7) 
        column_8 = getColumn(8) 
        column_9 = getColumn(9)
        column_1 =removeSpaces(column_1)
        column_2 =removeSpaces(column_2)
        column_3 =removeSpaces(column_3)
        column_4 =removeSpaces(column_4)
        column_5 =removeSpaces(column_5)
        column_6 =removeSpaces(column_6)
        column_7 =removeSpaces(column_7)
        column_8 =removeSpaces(column_8)
        column_9 =removeSpaces(column_9)
        for line in fle:
            numbers=re.findall(r'[0-9]{1,3}',line)
            line_num+=1
            if line_num >=11:
                #print(numbers)
                amount =int(numbers[0])
                #print(f'Amount: {amount}')
                column = int(numbers[1])
                destination = int(numbers[2])
                start = 0
                #store values from list you will remove
                for i in range(1):
                    if column == 1:
                        start=len(column_1)-amount
                        #print(f"Lenght of Column:{len(column_1)}")
                        result = column_1[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                        # values_removed.append(result)
                    if column == 2:
                        start=len(column_2)-amount
                        #print(f"Lenght of Column:{len(column_2)}")
                        result = column_2[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                        # values_removed.append(result)
                    if column == 3:
                        start=len(column_3)-amount
                        #print(f"Lenght of Column:{len(column_3)}")
                        result = column_3[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                    if column == 4:
                        start=len(column_4)-amount
                        #print(f"Lenght of Column:{len(column_4)}")
                        result = column_4[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                        # values_removed.append(result)
                    if column == 5:
                        start=len(column_5)-amount
                        #print(f"Lenght of Column:{len(column_5)}")
                        result = column_5[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                        # values_removed.append(result)
                    if column == 6:
                        #print(f'Column 6(is it blank):{column_6}')
                        start=len(column_6)-amount
                        #print(f"Lenght of Column:{len(column_6)}")
                        result = column_6[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                    if column == 7:
                        start=len(column_7)-amount
                        #print(f"Lenght of Column:{len(column_7)}")
                        result = column_7[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                        # values_removed.append(result)
                    if column == 8:
                        start=len(column_8)-amount
                        #print(f"Lenght of Column:{len(column_8)}")
                        result = column_8[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                        # values_removed.append(result)
                    if column == 9:
                        start=len(column_9)-amount
                        #print(f"Lenght of Column:{len(column_9)}")
                        result = column_9[start:]
                        # result.reverse()
                        #print(f"Values being removed: {result}")
                        # values_removed.append(result)
                    #remove values from list
                    #move 1(amount) from 2(column) to 1(destination)
                    #column_2[:-1]
                    #column_1.append(values_removed)
                    if column == 1:
                        column_1 = column_1[:-amount]
                        #print(f'column_1: {column_1}')
                    if destination == 1:
                        [column_1.append(result[x]) for x in range(len(result))] 
                        # column_1.append(values_removed)
                    if column == 2:
                        column_2 = column_2[:-amount]
                        #print(f'column_2: {column_2}')
                    if destination == 2:
                        [column_2.append(result[x]) for x in range(len(result))] 
                        # column_2.append(values_removed)
                    if column == 3:
                        column_3 = column_3[:-amount]
                        #print(f'column_3: {column_3}')
                    if destination == 3:
                        [column_3.append(result[x]) for x in range(len(result))]
                    if column == 4:
                        column_4 = column_4[:-amount]
                        #print(f'column_4: {column_4}')
                    if destination == 4:
                        [column_4.append(result[x]) for x in range(len(result))] 
                        # column_1.append(values_removed)
                    if column == 5:
                        column_5 = column_5[:-amount]
                        #print(f'column_5: {column_5}')
                    if destination == 5:
                        [column_5.append(result[x]) for x in range(len(result))] 
                        # column_2.append(values_removed)
                    if column == 6:
                        column_6 = column_6[:-amount]
                        #print(f'column_6: {column_6}')
                    if destination == 6:
                        [column_6.append(result[x]) for x in range(len(result))]
                    if column == 7:
                        column_7 = column_7[:-amount]
                        #print(f'column_7: {column_7}')
                    if destination == 7:
                        [column_7.append(result[x]) for x in range(len(result))] 
                        # column_1.append(values_removed)
                    if column == 8:
                        column_8 = column_8[:-amount]
                        #print(f'column_8: {column_8}')
                    if destination == 8:
                        [column_8.append(result[x]) for x in range(len(result))] 
                        # column_2.append(values_removed)
                    if column == 9:
                        column_9 = column_9[:-amount]
                        #print(f'column_9: {column_9}')
                    if destination == 9:
                        [column_9.append(result[x]) for x in range(len(result))]
 
                        # column_3.append(values_removed)    
                    # getColumn(column)[:-amount]
                    # getColumn(destination).append(values_removed)
    print(column_1[-1],column_2[-1],column_3[-1],column_4[-1],column_5[-1],column_6[-1],column_7[-1],column_8[-1],column_9[-1])



followMoves('input.txt')
















# with open ('input_test.txt', 'r') as fle2:
#     input_columns = fle2.readlines()
#     #print(input_columns)
#     list_column_numbers= re.findall(r'\d',input_columns[3].strip())
                

            
            

    
    # for line in input_columns:
    #     line_output = re.sub(r'\n','',line)
    #     line_output = re.sub(r'\s{2}','[]',line_output)
    #     # line_output = re.sub(r'\n','',line_output)
    #     # line_output = re.sub(r' ','',line_output)
    #     #print(line_output)
