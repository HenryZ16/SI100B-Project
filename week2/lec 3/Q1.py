#Ans:
#1. Points classified by Kmeans tend to form groups 
#   based on their distance to the center points,
#   so there is an invisible line to seperate
#   the two point groups;
#   And points classified by DBSCAN tend to form groups
#   based on their density, so the blank seperate
#   the two point groups;
#2. Some points gather into several solid circle.
#   See the example as follow.


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

def Kmeans(data: np.ndarray, k: int, centers: np.ndarray = None):
    #将各个点划分至不同的点集
    set=[[] for i in range(k)];
    cnt=[0]*k;
    for i in range(0,np.size(data)//2):
        min_d=10000000000;
        id=0;
        for j in range(0,k):
            if(dist(centers[j],data[i])<min_d):
                min_d=dist(centers[j],data[i]);
                id=j;
        set[id].append(data[i]);
        cnt[id]+=1;
    #计算新点集的质心
    centroid=[[]]*k;
    for i in range(0,k):
        sum=[0,0];
        if(cnt[i]==0): centroid[i]=centers[i];continue;
        centroid[i]=[np.sum(np.array(set[i]).T[0])/cnt[i],np.sum(np.array(set[i]).T[1])/cnt[i]];
    #比较新点集与原点集质心的误差
    err=0;
    for i in range(0,k):
        err+=dist(centroid[i],centers[i]);
    if(err>=0.05):
        return Kmeans(data,k,centroid);
    return [centroid,set];

def dist(X: np.ndarray,Y: np.ndarray):
    return np.sqrt((X[0]-Y[0])**2+(X[1]-Y[1])**2);

def nearest(X: np.ndarray,C: np.ndarray):
    #Your code here
    return

def main():
    toy1=np.load("toy1.npy");
    toy2=np.load("toy2.npy");
    
    [center,set]=Kmeans(toy1,2,np.array([toy1[0],toy1[-1]]));
    plt.subplot(3,2,1);
    plt.scatter(np.array(set[0]).T[0],np.array(set[0]).T[1],s=1,c="red");
    plt.scatter(np.array(set[1]).T[0],np.array(set[1]).T[1],s=1,c="green");
    plt.scatter(center[0][0],center[0][1],s=10,c="red",marker='x');
    plt.scatter(center[1][0],center[1][1],s=10,c="green",marker='x');
    plt.title("toy1 Kmeans");
    #----------------------------------------------------------------------
    [center,set]=Kmeans(toy2,2,np.array([toy2[0],toy2[-1]]));
    plt.subplot(3,2,2);
    plt.scatter(np.array(set[0]).T[0],np.array(set[0]).T[1],s=1,c="red");
    plt.scatter(np.array(set[1]).T[0],np.array(set[1]).T[1],s=1,c="green");
    plt.scatter(center[0][0],center[0][1],s=10,c="red",marker='x');
    plt.scatter(center[1][0],center[1][1],s=10,c="green",marker='x');
    plt.title("toy2 Kmeans");
    
    #----------------------------------------------------------------------
    db=DBSCAN(eps=0.5,min_samples=5).fit(toy1);
    _label=db.labels_;
    set=[[] for i in range(max(_label)+2)];
    for i in range(0,np.size(toy1)//2):
        set[_label[i]+1].append(toy1[i]);

    plt.subplot(3,2,3);
    if(len(set[0])!=0):
        plt.scatter(np.array(set[0]).T[0],np.array(set[0]).T[1],s=1,c="black");
    for i in range(1,max(_label)+2):
        plt.scatter(np.array(set[i]).T[0],np.array(set[i]).T[1],s=1);
    plt.title("toy1 DBSCAN");
    #----------------------------------------------------------------------
    db=DBSCAN(eps=0.5,min_samples=5).fit(toy2);
    _label=db.labels_;
    set=[[] for i in range(max(_label)+2)];
    for i in range(0,np.size(toy2)//2):
        set[_label[i]+1].append(toy2[i]);

    plt.subplot(3,2,4);
    if(len(set[0])!=0):
        plt.scatter(np.array(set[0]).T[0],np.array(set[0]).T[1],s=1,c="black");
    for i in range(1,max(_label)+2):
        plt.scatter(np.array(set[i]).T[0],np.array(set[i]).T[1],s=1);
    plt.title("toy2 DBSCAN");

    #----------------------------------------------------------------------
    test1=np.random.normal(10,0.5,1000);
    test1=np.append(test1,np.random.normal(3,0.5,1000));
    test2=np.random.normal(10,0.5,1000);
    test2=np.append(test2,np.random.normal(3,0.5,1000));
    test=np.array([test1,test2]).T;

    [center,set]=Kmeans(test,2,np.array([test[0],test[-1]]));
    plt.subplot(3,2,5);
    plt.scatter(np.array(set[0]).T[0],np.array(set[0]).T[1],s=1,c="red");
    plt.scatter(np.array(set[1]).T[0],np.array(set[1]).T[1],s=1,c="green");
    plt.scatter(center[0][0],center[0][1],s=10,c="red",marker='x');
    plt.scatter(center[1][0],center[1][1],s=10,c="green",marker='x');
    plt.title("test Kmeans");

    db=DBSCAN(eps=0.5,min_samples=5).fit(test);
    _label=db.labels_;
    set=[[] for i in range(max(_label)+2)];
    for i in range(0,np.size(test)//2):
        set[_label[i]+1].append(test[i]);

    plt.subplot(3,2,6);
    if(len(set[0])!=0):
        plt.scatter(np.array(set[0]).T[0],np.array(set[0]).T[1],s=1,c="black");
    for i in range(1,max(_label)+2):
        plt.scatter(np.array(set[i]).T[0],np.array(set[i]).T[1],s=1);
    plt.title("test DBSCAN");
    
    plt.show();

if(__name__ == '__main__'):
    main()
