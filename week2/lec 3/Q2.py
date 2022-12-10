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
        if np.datetime64(data[i][1])==np.datetime64(day_before_election):
            if data[i][3] == "NA" or data[i][5] == "NA":
                D += 1
                continue
            if float(data[i][3])>float(data[i][5]):
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
        if np.datetime64(data[date][1])==np.datetime64(election_date):
            break
        date-=1

    De=[0 for _ in range(91)]
    for i in range(0,91):
        for j in range(0,51):
            if data[date][3] == "NA" or data[date][5] == "NA":
                De[i] += 1
                date-=1
                continue
            if float(data[date][3])>float(data[date][5]):
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


import warnings
warnings.filterwarnings('ignore')

def cal_moving_avg(csv_file_path, election_date, filename):
    day=np.datetime64(election_date);
    with open(csv_file_path,'r',encoding='utf-8') as f:
        data_np = np.loadtxt(f, str, delimiter=",", skiprows=1)
    data=data_np.tolist()

    data[0].append("PriceD_MA");
    data[0].append("PriceR_MA");
    dic={"AL":0,"AK":1,"AZ":2,"AR":3,"CA":4,"CO":5,"CT":6,"DE":7,"DC":8,"FL":9,"GA":10,"HI":11,"ID":12,"IL":13,"IN":14,"IA":15,"KS":16,"KY":17,"LA":18,"ME":19,"MD":20,"MA":21,"MI":22,"MN":23,"MS":24,"MO":25,"MT":26,"NE":27,"NV":28,"NH":29,"NJ":30,"NM":31,"NY":32,"NC":33,"ND":34,"OH":35,"OK":36,"OR":37,"PA":38,"RI":39,"SC":40,"SD":41,"TN":42,"TX":43,"UT":44,"VT":45,"VA":46,"WA":47,"WV":48,"WI":49,"WY":50};
    state=[[[0 for i in range(7)],[0 for j in range(7)]] for k in range(51)];
    date=np.datetime64(data[1][1]);
    buc=[1]*51;
    buf=[];
    cnt=0;
    for i in range(1,len(data)):
        if(np.datetime64(election_date)-np.timedelta64(97,"D")<=np.datetime64(data[i][1])):
            if(date<np.datetime64(data[i][1])):
                for j in range(51):
                    if(buc[j]):
                        state[j][0].pop(0);
                        state[j][1].pop(0);
                        state[j][0].append(state[j][0][-1]);
                        state[j][1].append(state[j][1][-1]);

                buc=[1 for i in range(51)];

            state[dic[data[i][7][1:len(data[i][7])-1]]][0].pop(0);
            state[dic[data[i][7][1:len(data[i][7])-1]]][1].pop(0);
            if(data[i][3]=="NA"):
                state[dic[data[i][7][1:len(data[i][7])-1]]][0].append(state[j][0][-1]);
            else:
                state[dic[data[i][7][1:len(data[i][7])-1]]][0].append(float(data[i][3]));
            if(data[i][5]=="NA"):
                state[dic[data[i][7][1:len(data[i][7])-1]]][1].append(state[j][1][-1]);
            else:
                state[dic[data[i][7][1:len(data[i][7])-1]]][1].append(float(data[i][5]));
            
            buc[dic[data[i][7][1:len(data[i][7])-1]]]=0;

            if(np.datetime64(data[i][1])>=np.datetime64(election_date)-np.timedelta64(90,"D")):
                buf.append(data[i][1:len(data[i])]);
                buf[cnt].append(str(sum(state[dic[data[i][7][1:len(data[i][7])-1]]][0])/7));
                buf[cnt].append(str(sum(state[dic[data[i][7][1:len(data[i][7])-1]]][1])/7));
                cnt+=1;

    fData=pd.DataFrame(buf, index=range(len(buf)), columns=["day","statename","PriceD","VolumeD","PriceR","VolumeR","state","PriceD_MA","PriceR_MA"]);
    fData.to_csv(filename);
    return

def predict_by_moving_avg(csv_file_path, election_date):
    with open(csv_file_path,'r',encoding='utf-8') as f:
        data_np = np.loadtxt(f, str, delimiter=",", skiprows=1)
    data=data_np.tolist()
    R=0
    D=0

    for i in range(0,len(data)):
        if np.datetime64(data[i][1])<=np.datetime64(election_date):
            if data[i][8] == "NA" or data[i][9] == "NA":
                D+=1
                continue
            if float(data[i][8])>float(data[i][9]):
                D+=1
            else:
                R+=1

    if D>R:
        return "Democratic"
    else:
        return "Republican"
    return

#df = cal_moving_avg('intrade08.csv', election_date='2008-11-04', filename='intrade08_MA.csv');
#df = cal_moving_avg('intrade12.csv', election_date='2012-11-06', filename='intrade12_MA.csv');

winner = predict_by_moving_avg('intrade08_MA.csv', election_date='2008-11-04')
print('Predicted winner of 2008:', winner)

winner = predict_by_moving_avg('intrade12_MA.csv', election_date='2012-11-06')
print('Predicted winner of 2012:', winner)
