#A. We downloaded the data from the World Development Indicators in .csv file.
#B. We use open() to read the data.
#C. We use plot() in matplotlib to plot the data in linechart.
#D. 1)The defination of gross enrollment ratio is
#total enrolment in primary education, 
#regardless of age, 
#expressed as a percentage of the eligible official primary school-age population 
#in a given school-year.
#   2)Some‘strange’ phenomenon in the data may be the result of the goverment's policy, 
#some events happened in the year (such as in 1989) and so on.
#E. According to the data, we can find that the gross enrollment ratio of China
#have been increasing in the 10 years, while the one of Republic of Korea is decreasing.
import matplotlib.pyplot as plt
import numpy as np


fp=open("Data.csv");
for i in fp:
    a=[];
    b=i.rstrip("\n").split(",");
    k=0;
    s=0;t=0;
    for j in range(0,len(b)):
        if(b[j]==".."): continue;
        if(s==0): s=j;
        a.append(float(int(float(b[j])*100))/100);
        k=k+1;
        t=j;
    print(a);

    x=np.arange(2010+s-1,2010+t+1,int(10/k));
    plt.plot(x,a);
    plt.grid(True,color='g',linestyle='--',linewidth='1')
    plt.show();






    
