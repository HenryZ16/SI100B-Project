import numpy as np
import matplotlib.pyplot as plt

def proportion_biodiversity(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        data_np = np.loadtxt(f, str, delimiter=",", skiprows=1)
    data = data_np.tolist()
    l = len(data)
    year = []
    s_a = []
    ger = []
    for i in range(0, l):
        year.append(float(data[i][0]))
        s_a.append(float(data[i][2]))
        ger.append(float(data[i][4]))
    plt.plot(year, s_a,label="South Africa",color='b',linewidth=2)
    plt.plot(year, ger,label="Germany",color='r',linewidth=2)
    plt.xlabel("year")
    plt.ylabel("percent")
    plt.title("proportion biodiversity")
    plt.legend(framealpha=1, frameon=True)
    plt.show()


def fol_con(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        data_np = np.loadtxt(f, str, delimiter=",", skiprows=1)
    data = data_np.tolist()
    year=list(range(1971,2015))
    ban=data[0][15:59:1]
    s_a=data[1][15:59:1]
    qa=data[2][15:59:1]
    ger=data[3][15:59:1]
    for i in range (0,len(ban)):
        ban[i]=round(float(ban[i]),2)
        s_a[i] = round(float(s_a[i]), 2)
        if qa[i]=='':
            qa[i]=str(qa[i-1])
        qa[i] = round(float(qa[i]), 2)
        ger[i] = round(float(ger[i]), 2)

    plt.plot(year,ban,label="Bangladesh",color='g',linewidth=2)
    plt.plot(year,s_a,label="South Africa",color='b',linewidth=2)
    plt.plot(year,qa,label="Qatar",color='m',linewidth=2)
    plt.plot(year,ger,label="Germany",color='r',linewidth=2)
    plt.xlabel("year")
    plt.ylabel("percent")
    plt.title("Fossil fuel energy consumption (% of total)")
    plt.legend(framealpha=1, frameon=True)
    plt.show()


def outpol_por(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        data_np = np.loadtxt(f, str, delimiter=",", skiprows=1)
    data = data_np.tolist()
    l = len(data)
    year = []
    ban=[]
    s_a = []
    qa=[]
    ger = []
    for i in range(0, l):
        year.append(float(data[i][0]))
        ban.append(float(data[i][1]))
        s_a.append(float(data[i][2]))
        qa.append(float(data[i][3]))
        ger.append(float(data[i][4]))
    plt.plot(year,ban,label="Bangladesh",color='g',linewidth=2)
    plt.plot(year, s_a,label="South Africa",color='b',linewidth=2)
    plt.plot(year,qa,label="Qatar",color='m',linewidth=2)
    plt.plot(year, ger,label="Germany",color='r',linewidth=2)
    plt.xlabel("year")
    plt.ylabel("person")
    plt.title("outdoor pollution deathrate per 100k")
    plt.legend(framealpha=1, frameon=True)
    plt.show()




proportion_biodiversity("data_proportion_biodiversity.csv")
fol_con("data_fol_con.csv")
outpol_por("data_outpol_por.csv")
