

import csv
import pandas as pd
from csv import reader, writer
import numpy as np 
etc201501_A1A2 = []
etc_20150101_inlatehour0 = []
etc_20150101_inlatehour = []
def read_csv_file(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        for row in file:
            etc201501_A1A2.append(row)
        return csv.reader(file)
def read_csv_file1(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        for row in file:
            etc_20150101_inlatehour0.append(row)
        return csv.reader(file)
def avr(num):
    nsum = 0
    for i in range(len(num)):
        nsum += float(num[i])
    if len(num) == 0:
        return 0
    else:
        return nsum / len(num)
df = read_csv_file('/Users/lofangyu/Documents/data_analytics/etc201503_A1A2_sum.csv')      
for i in range (len(etc201501_A1A2)):
    etc201501_A1A2[i] = etc201501_A1A2[i].split(',')
print(etc201501_A1A2[:7])
etc201501_A1A2 = etc201501_A1A2[:1] + etc201501_A1A2[2:]
for r in range(len(etc201501_A1A2)):
    if len(etc201501_A1A2[r][1]) == 1:
        etc201501_A1A2[r][1] = '0' + (etc201501_A1A2[r][1])
#print(etc201501_A1A2[:7])
print(etc201501_A1A2[1])
#print(etc_20150101_inlatehour[0])


for j in range(len(etc201501_A1A2)):
    etc201501_A1A2[j][0] = etc201501_A1A2[j][0].split('/')
    if len(etc201501_A1A2[j][0][-1]) == 1:
        etc201501_A1A2[j][0][-1] = '0' + etc201501_A1A2[j][0][-1]



month_date = []
for h in range(int(etc201501_A1A2[-1][0][-1])):
    month_date.append(0)



for j in range(len(month_date)):
    for i in range(len(etc201501_A1A2)-1):
        if int(etc201501_A1A2[i+1][0][-1]) == j+1:
            month_date[j]+=1


strange = []

for l in range(1):
    #print(l)    
    a = 0
    for j in range(len(etc201501_A1A2)-1):        
        Q = []
        
        #print(etc201501_A1A2[j+1])
        if etc201501_A1A2[j+1][0] == etc201501_A1A2[j][0]:
            a +=1
        else:
            a = 0
        df1 = read_csv_file1('/Users/lofangyu/Documents/data_analytics/etc03/etc_201503' + etc201501_A1A2[j+1][0][-1] + '_inlatehour' + str(a) + '.csv')    
        etc_20150101_inlatehour = []
        for i in range (len(etc_20150101_inlatehour0)):
            
            if type(etc_20150101_inlatehour0[i]) == str:
                if etc_20150101_inlatehour0[i][0] !='"':
                    etc_20150101_inlatehour0[i] = etc_20150101_inlatehour0[i].split(',')
                    etc_20150101_inlatehour.append(etc_20150101_inlatehour0[i])
        
        for i in range (len(etc_20150101_inlatehour)):
            
            if etc_20150101_inlatehour[i][2] == etc201501_A1A2[j+1][l+9][:8]:  #後門架車量數
                if etc_20150101_inlatehour[i][2][0:2] =='05':
                    Q.append(0)
                if int(etc201501_A1A2[j+1][1]) == 0 and etc_20150101_inlatehour[i][2][0:2] !='05'and etc_20150101_inlatehour[i][0]!= 'QFno2BwkH+XltGIwUrsNQn+9DLVXcmIbxVI7BYKvUO0=':     
                    if  int(etc_20150101_inlatehour[i][1][11:13]) == 23: #hr<happen
                        if etc_20150101_inlatehour[i][2][-1] == 'N':
                            for g in range(len(etc_20150101_inlatehour)):
                                if etc_20150101_inlatehour[i][0] == etc_20150101_inlatehour[g][0] and etc_20150101_inlatehour[g][2] != etc_20150101_inlatehour[i][2]:
                                    
                                    km = int(etc_20150101_inlatehour[g][2][3:7])/10 - int(etc_20150101_inlatehour[i][2][3:7])/10
                                    hr = ( (int(etc_20150101_inlatehour[i][1][14:16]) * 60 + int(etc_20150101_inlatehour[i][1][17:19]))/ 3600) - ( int(etc_20150101_inlatehour[g][1][14:16]) * 60 + int(etc_20150101_inlatehour[g][1][17:19]))/ 3600
                                    if hr != 0:
                                        vel = km / hr
                                        
                                        Q.append(str(vel))
                                    else:
                                        strange.append(etc_20150101_inlatehour[i])
                                        strange.append(etc_20150101_inlatehour[g])
                                         
                        if etc_20150101_inlatehour[i][2][-1] == 'S':
                            for g in range(len(etc_20150101_inlatehour)):
                                if etc_20150101_inlatehour[i][0] == etc_20150101_inlatehour[g][0] and etc_20150101_inlatehour[g][2] != etc_20150101_inlatehour[i][2]:
                                    km = int(etc_20150101_inlatehour[g][2][3:7])/10 - int(etc_20150101_inlatehour[i][2][3:7])/10
                                    hr =( int(etc_20150101_inlatehour[g][1][14:16]) * 60 + int(etc_20150101_inlatehour[g][1][17:19]))/ 3600 - ( (int(etc_20150101_inlatehour[i][1][14:16]) * 60 + int(etc_20150101_inlatehour[i][1][17:19]))/ 3600)
                                    if hr != 0:
                                        vel = km / hr

                                        Q.append(str(vel))
                                    else:
                                        strange.append(etc_20150101_inlatehour[i])
                                        strange.append(etc_20150101_inlatehour[g])
                            
                            

                
            
                if int(etc_20150101_inlatehour[i][1][8:10]) ==int(etc201501_A1A2[j+1][0][2]) and etc_20150101_inlatehour[i][2][0:2] !='05'and etc_20150101_inlatehour[i][0]!= 'QFno2BwkH+XltGIwUrsNQn+9DLVXcmIbxVI7BYKvUO0=':

                    if  int(etc_20150101_inlatehour[i][1][11:13]) == (int(etc201501_A1A2[j+1][1]) - 1): #hr<happen
                        if etc_20150101_inlatehour[i][2][-1] == 'N':
                            for g in range(len(etc_20150101_inlatehour)):
                                if etc_20150101_inlatehour[i][0] == etc_20150101_inlatehour[g][0] and etc_20150101_inlatehour[g][2] != etc_20150101_inlatehour[i][2]:
                                    km = int(etc_20150101_inlatehour[g][2][3:7])/10 - int(etc_20150101_inlatehour[i][2][3:7])/10
                                    hr = ( (int(etc_20150101_inlatehour[i][1][14:16]) * 60 + int(etc_20150101_inlatehour[i][1][17:19]))/ 3600) - ( int(etc_20150101_inlatehour[g][1][14:16]) * 60 + int(etc_20150101_inlatehour[g][1][17:19]))/ 3600
                                    if hr != 0:
                                        vel = km / hr

                                        Q.append(str(vel))
                                    else:
                                        strange.append(etc_20150101_inlatehour[i])
                                        strange.append(etc_20150101_inlatehour[g])
                        if etc_20150101_inlatehour[i][2][-1] == 'S':
                            for g in range(len(etc_20150101_inlatehour)):
                                if etc_20150101_inlatehour[i][0] == etc_20150101_inlatehour[g][0] and etc_20150101_inlatehour[g][2] != etc_20150101_inlatehour[i][2]:
                                    km = int(etc_20150101_inlatehour[g][2][3:7])/10 - int(etc_20150101_inlatehour[i][2][3:7])/10
                                    hr =( int(etc_20150101_inlatehour[g][1][14:16]) * 60 + int(etc_20150101_inlatehour[g][1][17:19]))/ 3600 - ( (int(etc_20150101_inlatehour[i][1][14:16]) * 60 + int(etc_20150101_inlatehour[i][1][17:19]))/ 3600)
                                    if hr != 0:
                                        vel = km / hr

                                        Q.append(str(vel))
                                    else:
                                        strange.append(etc_20150101_inlatehour[i])
                                        strange.append(etc_20150101_inlatehour[g])
                            

                                
                    if int(etc_20150101_inlatehour[i][1][11:13]) == int(etc201501_A1A2[j+1][1]) and int(etc_20150101_inlatehour[i][1][14:16]) < int(etc201501_A1A2[j+1][2]): 
                        if etc_20150101_inlatehour[i][2][-1] == 'N':
                            for g in range(len(etc_20150101_inlatehour)):
                                if etc_20150101_inlatehour[i][0] == etc_20150101_inlatehour[g][0] and etc_20150101_inlatehour[g][2] != etc_20150101_inlatehour[i][2]:
                                    km = int(etc_20150101_inlatehour[g][2][3:7])/10 - int(etc_20150101_inlatehour[i][2][3:7])/10
                                    hr = ( (int(etc_20150101_inlatehour[i][1][14:16]) * 60 + int(etc_20150101_inlatehour[i][1][17:19]))/ 3600) - ( int(etc_20150101_inlatehour[g][1][14:16]) * 60 + int(etc_20150101_inlatehour[g][1][17:19]))/ 3600
                                    if hr != 0:
                                        vel = km / hr

                                        Q.append(str(vel))
                                    else:
                                        strange.append(etc_20150101_inlatehour[i])
                                        strange.append(etc_20150101_inlatehour[g])
                        if etc_20150101_inlatehour[i][2][-1] == 'S':
                            for g in range(len(etc_20150101_inlatehour)):
                                if etc_20150101_inlatehour[i][0] == etc_20150101_inlatehour[g][0] and etc_20150101_inlatehour[g][2] != etc_20150101_inlatehour[i][2]:
                                    km = int(etc_20150101_inlatehour[g][2][3:7])/10 - int(etc_20150101_inlatehour[i][2][3:7])/10
                                    hr =( int(etc_20150101_inlatehour[g][1][14:16]) * 60 + int(etc_20150101_inlatehour[g][1][17:19]))/ 3600 - ( (int(etc_20150101_inlatehour[i][1][14:16]) * 60 + int(etc_20150101_inlatehour[i][1][17:19]))/ 3600)
                                    if hr != 0:
                                        vel = km / hr

                                        Q.append(str(vel))
                                    else:
                                        strange.append(etc_20150101_inlatehour[i])
                                        strange.append(etc_20150101_inlatehour[g])                         
        avr_Q = avr(Q)
        print(avr_Q)
        etc201501_A1A2[j+1].append(str(avr_Q))
                                
with open('13_speed_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(etc201501_A1A2)










