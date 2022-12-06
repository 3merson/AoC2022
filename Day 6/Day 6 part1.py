import os
import re

os.chdir(os.path.dirname(__file__))

with open ('input.txt', 'r') as fle:
    char_counter=1
    last_four_packets= []
    transmition = []
    for line in fle:
        signal = line.strip()
        for i in range(len(signal)):
            last_four_packets.append(signal[i])
            if len(last_four_packets) > 4:
                last_four_packets.pop(0)
            if len(last_four_packets) == 4:
                # print(f'Last 4 packets sent: {last_four_packets}')
                transmition = last_four_packets[:]
                transmition.sort()
                transmition_compare = list(set(transmition))
                transmition_compare.sort()
                if transmition == transmition_compare:
                    print(char_counter)
                    char_counter=1
                    last_four_packets = []
                    break
            transmition = []
            char_counter+=1

#start of a packet is indicated by a sequence of four characters that are all different
#creates a queue where it checks the first 4 digits it recives and then removes the first digit it recived and adds a new one to check.
#uses set to check for duplicates if no duplicate is found then that 4 send are the packet marker.
#returns character that maker was found on