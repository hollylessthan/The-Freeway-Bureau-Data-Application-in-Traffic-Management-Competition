import csv
import pandas as pd
from csv import reader, writer
A1A2_data1 = []
highway_traffic_data = []
highway_traffic_data_first = []
highway_traffic_next = []
highway_traffic_pre = []
def read_csv_file(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        for row in file:
            highway_traffic_data.append(row)
        return csv.reader(file)
def read_csv_file1(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        for row in file:
            A1A2_data1.append(row)
        return csv.reader(file)

      
df = read_csv_file('/Users/lofangyu/Documents/highway＿data analytics/highway_traffic_data_104.csv')      
df1 = read_csv_file1('/Users/lofangyu/Documents/highway＿data analytics/A1A2Table1.csv')
for i in range (len(highway_traffic_data)):
    highway_traffic_data[i] = highway_traffic_data[i].split(',')
for i in range (len(A1A2_data1)):
    A1A2_data1[i] = A1A2_data1[i].split(',')
#print(A1A2_data1[0][25:29])
#print(A1A2_data1[1083][25:29])
#print(A1A2_data1[1083][6:9])
#print(int(A1A2_data1[1083][26]+A1A2_data1[1083][27]))
#print(A1A2_data1[1083][6][7:])
#print(A1A2_data1[1][6][5])
#print(A1A2_data1[123][28])

print(A1A2_data1[0][54])
print(A1A2_data1[0][55])
#2015/1事故
day = []
for i in range(31):
    day.append(str(i+1))
etc_20150101 = []
# 17 22/18 20/ 19 25/ 20 28/ 21 28/ 22 28/ 23 24/24 19/ 25 18/ 26 20/ 27 22/ 28 22 
day = '28'
last_day = '24'
next_day = '30'
month = '03'
last_month = '01'
last_day_len = 20
day_len = 23
next_day_len = 19 
for i in range(len(A1A2_data1)-1):
    if A1A2_data1[i+1][6][2:4] == '15' and A1A2_data1[i+1][6][5] == str(int(month)) and A1A2_data1[i+1][6][7:] == str(int(day)) and A1A2_data1[i+1][28] != '西' and A1A2_data1[i+1][28] != '東': 
        etc_20150101.append(A1A2_data1[i+1][6:9] + A1A2_data1[i+1][25:29] + A1A2_data1[i+1][54:56])


for i in range(len(etc_20150101)):
    if etc_20150101[i][6] == '南':
      etc_20150101[i][6] = 'S'
    if etc_20150101[i][6] == '北':
      etc_20150101[i][6] = 'N'
    if etc_20150101[i][3][2] == '3':
      etc_20150101[i][3] = '國道三號'
    if etc_20150101[i][3][2] == '1':
      etc_20150101[i][3] = '國道一號'
#for i in range(len(etc_20150101)):
 #   print(etc_20150101[i])
#########
print(etc_20150101)
#單一事故去找發生的門架（國道/向南向北）
for j in range(len(etc_20150101)):
    highway_traffic_data_first = []
    highway_traffic_next = []
    highway_traffic_pre = []

    for i in range(len(highway_traffic_data)):
        if highway_traffic_data[i][0] == etc_20150101[j][3] and highway_traffic_data[i][1] == etc_20150101[j][6]:
            highway_traffic_data_first.append(highway_traffic_data[i])

#pre 門架
    for i in range(len(highway_traffic_data_first)):
        #print(int(highway_traffic_data_first[i][3][3:7]))
        if etc_20150101[j][3] != '國道五號':
            if int(highway_traffic_data_first[i][3][3:7]) < int(etc_20150101[j][4]+etc_20150101[j][5][0]):
                highway_traffic_pre.append(highway_traffic_data_first[i][3][3:7]) 
        else:
            if int(highway_traffic_data_first[i][3][4:7]) < int(etc_20150101[j][4]+etc_20150101[j][5][0]):
                highway_traffic_pre.append(highway_traffic_data_first[i][3][4:7])
    for i in range(len(highway_traffic_data_first)):
        if etc_20150101[j][3] != '國道五號':
            if highway_traffic_pre !=[]:
                if highway_traffic_data_first[i][3][3:7] == max(highway_traffic_pre):
                #print(highway_traffic_data_first[i])
                    etc_20150101[j].append(highway_traffic_data_first[i][3])
            else:
                etc_20150101[j].append('NO')
                break
        else:
            if highway_traffic_pre !=[]:
                if highway_traffic_data_first[i][3][4:7] == max(highway_traffic_pre):
                #print(highway_traffic_data_first[i])
                    etc_20150101[j].append(highway_traffic_data_first[i][3])
            else:
                etc_20150101[j].append('NO')
                break
#next 門架
    for i in range(len(highway_traffic_data_first)):
        if etc_20150101[j][3] != '國道五號':
            if int(highway_traffic_data_first[i][3][3:7]) >= int(etc_20150101[j][4]+etc_20150101[j][5][0]):
                highway_traffic_next.append(highway_traffic_data_first[i][3][3:7])
        else:
            if int(highway_traffic_data_first[i][3][4:7]) >= int(etc_20150101[j][4]+etc_20150101[j][5][0]):
                highway_traffic_next.append(highway_traffic_data_first[i][3][4:7])
    for i in range(len(highway_traffic_data_first)):
        if etc_20150101[j][3] != '國道五號':
            if highway_traffic_next != []:
                if highway_traffic_data_first[i][3][3:7] == min(highway_traffic_next):
                #print(highway_traffic_data_first[i])
                    etc_20150101[j].append(highway_traffic_data_first[i][3])
            else:
                etc_20150101[j].append('NO')
                break
        else:
            if highway_traffic_next != []:
                if highway_traffic_data_first[i][3][4:7] == min(highway_traffic_next):
                #print(highway_traffic_data_first[i])
                    etc_20150101[j].append(highway_traffic_data_first[i][3])
            else:
                etc_20150101[j].append('NO')
                break

for i in range(len(etc_20150101)):
    if len(etc_20150101[i][1]) == 1:
        etc_20150101[i][1] = '0' + etc_20150101[i][1]
    print(etc_20150101[i])



etc_len = []
for i in range(len(etc_20150101)):
    etc_len.append(str(i))

#open ets text

def open_txt_split(filename):
    f = open(r'/Users/lofangyu/Documents/highway＿data analytics/2015ETC/201503/'+filename+'.txt')
    file1 = []
    for line in f:
        file1.append(line)
    for i in range (len(file1)):
        file1[i] =file1[i].split(',')
    return file1

ad = 0
if ad != 1:
    with open('etc201502_A1A2.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(etc_20150101)


for b in range(day_len):
    df = open_txt_split('2015'+ month + day + '-'+ str(b+1))


    def Average(lst): 
        return sum(lst) / len(lst) 
    for j in range(len(etc_20150101)):
        total_time = []
        enter_car = []
        out_car = []
        for i in range(len(df)):
            
            if df[i][2] == etc_20150101[j][9]:
                
                if int(etc_20150101[j][1]) == 0:
                    if int(df[i][1][8:10]) == int(last_day) and int(df[i][1][11:13]) == 23 and int(df[i][1][14:16]) >= int(etc_20150101[j][2]):
                    
                        enter_car.append(df[i])  
                if int(df[i][1][8:10]) ==int(day) and int(df[i][1][11:13]) == (int(etc_20150101[j][1]) - 1) and int(df[i][1][14:16]) >= int(etc_20150101[j][2]):
                    
                    enter_car.append(df[i])  
                if int(df[i][1][8:10]) ==int(day) and int(df[i][1][11:13]) == (int(etc_20150101[j][1]) + 1) and int(df[i][1][14:16]) <= int(etc_20150101[j][2]):
                    #print(int(df[i][1][11:13]))
                    enter_car.append(df[i])

                if int(etc_20150101[j][1]) == 23:
                    if int(df[i][1][8:10]) == int(next_day) and int(df[i][1][11:13]) == 0 and int(df[i][1][14:16]) <= int(etc_20150101[j][2]):
                    
                        enter_car.append(df[i]) 
                  
                    
                if int(df[i][1][8:10]) ==int(day) and int(df[i][1][11:13]) == int(etc_20150101[j][1]): 
                    enter_car.append(df[i])
                
                    
            if df[i][2] == etc_20150101[j][10]:
                if int(etc_20150101[j][1]) == 0:
                    if int(df[i][1][8:10]) == int(last_day) and int(df[i][1][11:13]) == 23 and int(df[i][1][14:16]) >= int(etc_20150101[j][2]):
                    
                        out_car.append(df[i]) 
                if int(df[i][1][8:10]) ==int(day) and int(df[i][1][11:13]) == (int(etc_20150101[j][1]) - 1) and int(df[i][1][14:16]) >= int(etc_20150101[j][2]):
                    
                    out_car.append(df[i])  
                if int(df[i][1][8:10]) ==int(day) and int(df[i][1][11:13]) == (int(etc_20150101[j][1]) + 1) and int(df[i][1][14:16]) <= int(etc_20150101[j][2]):
                    
                    out_car.append(df[i])

                if int(df[i][1][8:10]) ==int(day) and int(df[i][1][11:13]) == int(etc_20150101[j][1]): 
                    out_car.append(df[i])

                if int(etc_20150101[j][1]) == 23:
                    if int(df[i][1][8:10]) == int(next_day) and int(df[i][1][11:13]) == 0 and int(df[i][1][14:16]) <= int(etc_20150101[j][2]):
                    
                        out_car.append(df[i])
        
        with open('etc_2015'+month+day+'_inlatehour'+ etc_len[j] + '.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerows(enter_car)
            writer.writerows(out_car)
    print(str(b+1) + "done") 
#print(etc_20150101)
#with open('etc_20150101_output.csv', 'a', newline='') as csvfile:
#        writer = csv.writer(csvfile)
#        writer.writerows(etc_20150101)

