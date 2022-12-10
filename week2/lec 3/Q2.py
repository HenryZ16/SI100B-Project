import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x_axis_data=[]
y_axis_data=[]

def predict_by_previous_day(csv_file_path, day_before_election):
    #Your code here
    with open(csv_file_path,'r',encoding='utf-8') as f:
        data_np = np.loadtxt(f, str, delimiter=",", skiprows=1)
    data=data_np.tolist()
    R=0
    D=0

    for i in range(0,len(data)):
        if data[i][1]==day_before_election:
            if data[i][3] == "NA" or data[i][5] == "NA":
                D += 1
                continue
            if data[i][3]>data[i][5]:
                D+=1
            else:
                R+=1

    if D>R:
        return "Democratic"
    else:
        return "Republican"


winner = predict_by_previous_day('intrade08.csv', day_before_election='2008-11-03')
print('Predicted winner of 2008:', winner)
winner = predict_by_previous_day('intrade12.csv', day_before_election='2012-11-05')
print('Predicted winner of 2012:', winner)


def predict_by_ninety_days(csv_file_path, election_date):
    #Your code here
    x_axis_data=[]
    y_axis_data=[]
    for i in range(0,91):
        x_axis_data.append(i+1)
        y_axis_data.append(0)

    with open(csv_file_path,'r',encoding='utf-8') as f:
        data_np = np.loadtxt(f, str, delimiter=",", skiprows=1)
    data=data_np.tolist()
    date=len(data)-1
    flag=0
    while(True):
        if data[date][1]==election_date:
            break
        date-=1

    De=[0 for _ in range(91)]
    for i in range(0,91):
        for j in range(0,51):
            if data[date][3] == "NA" or data[date][5] == "NA":
                De[i] += 1
                date-=1
                continue
            if data[date][3]>data[date][5]:
                De[i]+=1
            date-=1

        y_axis_data[i]=De[i]*365//De[0]
        if De[i]>=26:
            flag+=1

    #De[0]->365
    #y=De[i]*365/De[0]

    temp_data=y_axis_data[::-1]
    y_axis_data=temp_data

    temp_De=De[::-1]
    temp_De.pop()
    De=temp_De
    #De: the votes of Democratic in the last 90 days

    N=90
    s=0
    ro=0
    xba=0
    yba=0
    for i in range(1,N+1):
        s+=i*i
        ro+=i*De[i-1]
        xba+=i
        yba+=De[i-1]
    s=s/N
    ro=ro/N
    xba=xba/N
    yba=yba/N
    m=(ro-xba*yba)/(s-xba*xba)
    b=yba-xba*m
    pre_vote=m*91+b
    #print(pre_vote)
    if(pre_vote>=26):
        return "Democratic"
    else:
        return "Republican"

    #plot_ninety_days(x=x_axis_data,y=y_axis_data)

    #if flag>45:
     #   return "Democratic"
    #else:
     #   return "Republican"
    # it's the wrong algorithm but another way to predict so i don't delete it
    #return

def plot_ninety_days(x,y):
    #we suppose that Obama won 365 votes in 2012
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(x, y, 'ro-', alpha=0.8, linewidth=1, label='votes for Democratic')
    plt.legend(loc="upper right")
    plt.xlabel('time(day)')
    plt.ylabel('votes')
    plt.show()
    pass

winner = predict_by_ninety_days('intrade08.csv', election_date='2008-11-04')
print('Predicted winner of 2008:', winner)
winner = predict_by_ninety_days('intrade12.csv', election_date='2012-11-06')
print('Predicted winner of 2012:', winner)

