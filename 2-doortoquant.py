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

df = read_csv_file('/Users/lofangyu/Documents/data_analytics/etc03/etc201503_A1A2.csv')      
for i in range (len(etc201501_A1A2)):
                etc201501_A1A2[i] = etc201501_A1A2[i].split(',')

etc201501_A1A2 = etc201501_A1A2[:1] + etc201501_A1A2[2:]
for r in range(len(etc201501_A1A2)):
    if len(etc201501_A1A2[r][1]) == 1:
        etc201501_A1A2[r][1] = '0' + (etc201501_A1A2[r][1])
#print(etc201501_A1A2[:7])

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




for l in range(2):
    #print(l)    
    a = 0
    for j in range(len(etc201501_A1A2)-1):        
        
        if etc201501_A1A2[j+1][0] == etc201501_A1A2[j][0]:
            a +=1
        else:
            a = 0
        df1 = read_csv_file1('/Users/lofangyu/Documents/data_analytics/etc03/etc_201503' + etc201501_A1A2[j+1][0][-1] + '_inlatehour' + str(a) + '.csv')    
        etc_20150101_inlatehour = []
        for i in range (len(etc_20150101_inlatehour0)):
            #print(etc_20150101_inlatehour0[i])
            
            if type(etc_20150101_inlatehour0[i]) == str:
                if etc_20150101_inlatehour0[i][0] !='"':
                    #print(etc_20150101_inlatehour0[i])
                    etc_20150101_inlatehour0[i] = etc_20150101_inlatehour0[i].split(',')
                    etc_20150101_inlatehour.append(etc_20150101_inlatehour0[i])
            #pre_door
           
            #print(etc201501_A1A2[j+1][l+7])
        for i in range (len(etc_20150101_inlatehour)):
            
            #print(etc_20150101_inlatehour[i])

            #print(etc201501_A1A2[j+1][l+7][:8])
            if etc_20150101_inlatehour[i][2] == etc201501_A1A2[j+1][l+9][:8]:
                #print(etc_20150101_inlatehour[i][2])
                
                if int(etc201501_A1A2[j+1][1]) == 0:     
                    if  int(etc_20150101_inlatehour[i][1][11:13]) == 23: #hr<happen
                            
                            aa =  str(l+1) + '1' + etc_20150101_inlatehour[i][3]  
                            
                            no = 0
                            for g in range(len(etc201501_A1A2[j+1])-11):
                                
                                if etc201501_A1A2[j+1][g+11][:3] == aa:
                                    etc201501_A1A2[j+1][g+11] = etc201501_A1A2[j+1][g+11][:3] + str(int(etc201501_A1A2[j+1][g+11][3:]) + 1)
                                    no += 1
                            if no == 0:
                                aa =  str(l+1)  + '1' +etc_20150101_inlatehour[i][3]  +str(1)
                                etc201501_A1A2[j+1].append(aa)

                if int(etc201501_A1A2[j+1][1]) == 23:
                    
                    if int(etc_20150101_inlatehour[i][1][11:13]) == 0 :#hr after happen    
                            aa =  str(l+1)  + '2' + etc_20150101_inlatehour[i][3]  
                            no = 0
                            for g in range(len(etc201501_A1A2[j+1])-11):
                                
                                if etc201501_A1A2[j+1][g+11][:3] == aa:
                                    etc201501_A1A2[j+1][g+11] = etc201501_A1A2[j+1][g+11][:3] + str(int(etc201501_A1A2[j+1][g+11][3:]) + 1)
                                    no += 1
                            if no == 0:
                                aa =  str(l+1)  + '2' +etc_20150101_inlatehour[i][3]  +str(1)
                                etc201501_A1A2[j+1].append(aa)
            
                if int(etc_20150101_inlatehour[i][1][8:10]) ==int(etc201501_A1A2[j+1][0][2]):
                    #print(int(etc_20150101_inlatehour[i][1][8:10]))
                    if  int(etc_20150101_inlatehour[i][1][11:13]) == (int(etc201501_A1A2[j+1][1]) - 1): #hr<happen
                        aa =  str(l+1)  + '1' + etc_20150101_inlatehour[i][3]  
                        
                        no = 0
                        for g in range(len(etc201501_A1A2[j+1])-11):
                            if etc201501_A1A2[j+1][g+11][:3] == aa:
                                
                                #print(etc201501_A1A2[j+1][g])
                                etc201501_A1A2[j+1][g+11] = etc201501_A1A2[j+1][g+11][:3] + str(int(etc201501_A1A2[j+1][g+11][3:]) + 1)
                                no +=1
                        if no == 0:
                            aa =  str(l+1)  + '1' +etc_20150101_inlatehour[i][3]  +str(1)
                            
                            etc201501_A1A2[j+1].append(aa)
                            
                            
                            
                                
                       
                    if int(etc_20150101_inlatehour[i][1][11:13]) == (int(etc201501_A1A2[j+1][1]) + 1) :#hr after happen
                            
                        aa =  str(l+1)  + '2' + etc_20150101_inlatehour[i][3]  
                        
                        no = 0
                        for g in range(len(etc201501_A1A2[j+1])-11):
                            if etc201501_A1A2[j+1][g+11][:3] == aa:
                                
                                #print(etc201501_A1A2[j+1][g])
                                etc201501_A1A2[j+1][g+11] = etc201501_A1A2[j+1][g+11][:3] + str(int(etc201501_A1A2[j+1][g+11][3:]) + 1)
                                no +=1
                        if no == 0:
                            aa =  str(l+1)  + '2' +etc_20150101_inlatehour[i][3]  +str(1)
                            
                            etc201501_A1A2[j+1].append(aa)
                                
                    if int(etc_20150101_inlatehour[i][1][11:13]) == int(etc201501_A1A2[j+1][1]) and int(etc_20150101_inlatehour[i][1][14:16]) < int(etc201501_A1A2[j+1][2]): 
                            
                        aa =  str(l+1)  + '1' + etc_20150101_inlatehour[i][3]  
                        
                        no = 0
                        for g in range(len(etc201501_A1A2[j+1])-11):
                            if etc201501_A1A2[j+1][g+11][:3] == aa:
                                
                                #print(etc201501_A1A2[j+1][g])
                                etc201501_A1A2[j+1][g+11] = etc201501_A1A2[j+1][g+11][:3] + str(int(etc201501_A1A2[j+1][g+11][3:]) + 1)
                                no +=1
                        if no == 0:
                            aa =  str(l+1)  + '1' +etc_20150101_inlatehour[i][3]  +str(1)
                            
                            etc201501_A1A2[j+1].append(aa)
                                
                    if  int(etc_20150101_inlatehour[i][1][11:13]) == int(etc201501_A1A2[j+1][1]) and int(etc_20150101_inlatehour[i][1][14:16]) >= int(etc201501_A1A2[j+1][2]): 
                        aa =  str(l+1)  + '2' + etc_20150101_inlatehour[i][3]  
                        
                        no = 0
                        for g in range(len(etc201501_A1A2[j+1])-11):
                            if etc201501_A1A2[j+1][g+11][:3] == aa:
                                
                                #print(etc201501_A1A2[j+1][g])
                                etc201501_A1A2[j+1][g+11] = etc201501_A1A2[j+1][g+11][:3] + str(int(etc201501_A1A2[j+1][g+11][3:]) + 1)
                                no +=1
                        if no == 0:
                            aa =  str(l+1)  + '2' +etc_20150101_inlatehour[i][3]  +str(1)
                            
                            etc201501_A1A2[j+1].append(aa)
                
        #print(len(etc_20150101_inlatehour))
        #print(ki)
    #print(len(etc_20150101_inlatehour0))

 
Pre_door_1 =[]
Pre_door_2 =[]
Post_door_1=[]
Post_door_2= [] 
for j in range(len(etc201501_A1A2)-1):
    pre_door_1 =[]
    pre_door_2 =[]
    post_door_1=[]
    post_door_2= []  
    k = len(etc201501_A1A2[j+1])-11
    for i in range(k):
        b = i + 11
        if etc201501_A1A2[j+1][i+11][0] == '1' and etc201501_A1A2[j+1][i+11][1] == '1':
            
            pre_door_1.append(etc201501_A1A2[j+1][i+11][3:])
        if etc201501_A1A2[j+1][i+11][0] == '1' and etc201501_A1A2[j+1][i+11][1] == '2':
            pre_door_2.append(etc201501_A1A2[j+1][i+11][3:])    
        if etc201501_A1A2[j+1][i+11][0] == '2' and etc201501_A1A2[j+1][i+11][1] == '1':
            post_door_1.append(etc201501_A1A2[j+1][i+11][3:])
        if etc201501_A1A2[j+1][i+11][0] == '2' and etc201501_A1A2[j+1][i+11][1] == '2':
            post_door_2.append(etc201501_A1A2[j+1][i+11][3:])
    Pre_door_1.append(pre_door_1)
    Pre_door_2.append(pre_door_2)
    Post_door_1.append(post_door_1)
    Post_door_2.append(post_door_2)
#print(etc201501_A1A2[1])
ad = 0
    
if ad != 1:
    with open('etc201503_A1A2_carr.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(etc201501_A1A2)
    with open('etc201503_A1A2_pre1.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(Pre_door_1) 
    with open('etc201503_A1A2_pre2.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(Pre_door_2)
    with open('etc201503_A1A2_post1.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(Post_door_1)
    with open('etc201503_A1A2_post2.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(Post_door_2)

print(Pre_door_1)
print(etc201501_A1A2[2])