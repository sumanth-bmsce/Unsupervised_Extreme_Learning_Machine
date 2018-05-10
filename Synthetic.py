import random
import math
import numpy as np;
import matplotlib.pyplot as plt;


# Flame Shaped Dataset

def generator1():
   
    rad = 2
    num = 300

    t = np.random.uniform(0.0, 2.0*np.pi, num)
    r = rad * np.sqrt(np.random.uniform(0.0, 1.0, num))
    x1 = r * np.cos(t)+ np.random.uniform(0.0,0.6,300)
    y1 = r * np.sin(t)+ np.random.uniform(0.0,0.6,300)
    size = 4;
    dom = 0.125*3.14 + np.random.uniform(0.0,0.6,300)*1.25*3.14;
    x2= size*np.sin(dom) + np.random.uniform(0,2,300)*0.4;
    y2= size*np.cos(dom.T) + np.random.uniform(0,2,300)*0.4;
    cluster1 =[[0.0 for i in range(0,300)]for j in range(0,2)];
    cluster1[0] = x1;
    cluster1[1] = y1;
    cluster2 =[[0.0 for i in range(0,300)]for j in range(0,2)];
    cluster2[0] = x2;
    cluster2[1] = y2;
    cluster1 = np.array(cluster1);
    
    cluster2 = np.array(cluster2);
    cluster1 = cluster1.T;
    
    cluster2 = cluster2.T;
    
    input_array = np.concatenate((cluster1,cluster2),axis=0);
    
    return input_array;

def gen_res_1(input_array,result1,result2):
    
    cluster1 = [[0 for i in range(0,2)]for j in range(0,300)];
    cluster2 = [[0 for i in range(0,2)]for j in range(0,300)];
    result1 = np.array(result1);
    result2 = np.array(result2);
    result1 = result1.T;
    result2 = result2.T;
    f1= plt.figure(1);
    for i in range(0,300):
        cluster1[i] = input_array[i];
    j=0;
    for i in range(300,600):
        cluster2[j] = input_array[i];
        j=j+1;
    print (input_array.shape);   

    plt.title("Result 1");
    plt.scatter(result1[0],result1[1],marker='^');
    plt.scatter(result2[0],result2[1],marker='+');
    cluster1 = np.array(cluster1);
    cluster2= np.array(cluster2);
    cluster1=cluster1.T;
    cluster2=cluster2.T
    f2=plt.figure(2);
    plt.title("Original 1");
    plt.scatter(cluster1[0],cluster1[1],marker='^');
    plt.scatter(cluster2[0],cluster2[1],marker='+');
    plt.show();


# Four class Linearly Separable Dataset

def generator2():
    
    
    cluster1 = [[random.randint(0,30) for i in range(0,2)]for j in range(0,100)];
    cluster2 = [[random.randint(60,90) for i in range(0,2)]for j in range(0,100)];
    cluster3= [[0 for i in range(0,2)]for j in range(0,100)];
    cluster4= [[0 for i in range(0,2)]for j in range(0,100)];
    cluster1 = np.array(cluster1);
    cluster1=cluster1.T;
    cluster2 = np.array(cluster2);
    cluster2=cluster2.T;
    cluster3 = np.array(cluster3);
    cluster3=cluster3.T;
    cluster4 = np.array(cluster4);
    cluster4=cluster4.T;

    cluster3[0]=[random.randint(60,90) for i in range(0,100)]
    cluster3[1]=[random.randint(0,30) for i in range(0,100)]
    cluster4[0]=[random.randint(0,30) for i in range(0,100)]
    cluster4[1]=[random.randint(60,90) for i in range(0,100)]
    cluster1=cluster1.T;
    cluster2=cluster2.T;
    cluster3=cluster3.T;
    cluster4=cluster4.T;
    input_array1 = np.concatenate((cluster1,cluster2),axis=0);
    input_array2 = np.concatenate((cluster3,cluster4),axis=0);
    input_array = np.concatenate((input_array1,input_array2),axis=0);
    return input_array;


def gen_res_2(input_array,result1,result2,result3,result4):
    cluster1 = [[0 for i in range(0,2)]for j in range(0,100)];
    cluster2 = [[0 for i in range(0,2)]for j in range(0,100)];
    cluster3 = [[0 for i in range(0,2)]for j in range(0,100)];
    cluster4 = [[0 for i in range(0,2)]for j in range(0,100)];
    j=0;
    for i in range(0,100):
        cluster1[j] = input_array[i];
        j=j+1;
    j=0;
    for i in range(100,200):
        cluster2[j] = input_array[i];
        j=j+1;
    j=0;
    for i in range(200,300):
        cluster3[j] = input_array[i];
        j=j+1;
    j=0;
    for i in range(300,400):
        cluster4[j] = input_array[i];
        j=j+1;
    
    result1 = np.array(result1);
    result2 = np.array(result2);
    result3 = np.array(result3);
    result4 = np.array(result4);
    result1 = result1.T;
    result2 = result2.T;
    result3 = result3.T;
    result4 = result4.T;
    f= plt.figure(1);

    plt.title("Result 2");
    plt.scatter(result1[0],result1[1],marker='^');
    plt.scatter(result2[0],result2[1],marker='+');
    plt.scatter(result3[0],result3[1],marker='.');
    plt.scatter(result4[0],result4[1],marker='*');
    cluster1 = np.array(cluster1);
    cluster2= np.array(cluster2);
    cluster3= np.array(cluster3);
    cluster4= np.array(cluster4);
    cluster1=cluster1.T;
    cluster2=cluster2.T
    cluster3 = cluster3.T;
    cluster4 = cluster4.T;
    g=plt.figure(2);
    plt.title("Original 2");
    plt.scatter(cluster1[0],cluster1[1],marker='^');
    plt.scatter(cluster2[0],cluster2[1],marker='+');
    plt.scatter(cluster3[0],cluster3[1],marker='.');
    plt.scatter(cluster4[0],cluster4[1],marker='*');
    plt.show();

# Face Shaped Dataset

def generator3():
    
    #eye
    cluster1 = [[0.0 for i in range(0,2)]for j in range(0,500)];
    cluster1 = np.array(cluster1);
    cluster1 = cluster1.T;
    cluster1[0] = [random.uniform(0.5,2.5) for i in range(0,500)];
    cluster1[1] = [random.uniform(11,14) for i in range(0,500)];

    #eye
    cluster2 = [[0.0 for i in range(0,2)]for j in range(0,500)];
    cluster2= np.array(cluster2);
    cluster2 = cluster2.T;
    cluster2[0] = [random.uniform(4.5,6.5) for i in range(0,500)]
    cluster2[1] = [random.uniform(11,14) for i in range(0,500)];

    #lips
    cluster3 = [[0.0 for i in range(0,2)]for j in range(0,200)];
    cluster3 = np.array(cluster3);
    cluster3 = cluster3.T;
    cluster3[0] = [random.uniform(2.35,4.35) for i in range(0,200)];
    cluster3[1] = [random.uniform(4,5) for i in range(0,200)];

    #neck
    cluster4 = [[0.0 for i in range(0,2)]for j in range(0,500)];
    cluster4 = np.array(cluster4);
    cluster4 = cluster4.T;
    x1 = np.random.uniform(0.5,6,500);
    y1 = 0.8*(x1-3.2)**2+np.random.uniform(0,1,500);
    cluster4[0] = x1;
    cluster4[1] = y1;

    #nose
    cluster5 = [[0.0 for i in range(0,2)]for j in range(0,500)];
    cluster5 = np.array(cluster5);
    cluster5 = cluster5.T;
    x2 = np.random.uniform(2.5,4.5,500);
    y2 = (3*(x2-3.5)**2+6)+np.random.uniform(0,1,500);
    cluster5[0] = x2;
    cluster5[1] = y2;


    cluster1 = np.array(cluster1);
    cluster2 = np.array(cluster2);
    cluster3 = np.array(cluster3);
    cluster4 = np.array(cluster4);
    cluster5 = np.array(cluster5);
    cluster1=cluster1.T;
    cluster2=cluster2.T;
    cluster3=cluster3.T;
    cluster4=cluster4.T;
    cluster5=cluster5.T;
    input_array = np.concatenate((cluster1,cluster2,cluster3,cluster4,cluster5),axis=0);
    return input_array;


def gen_res_6(input_array,result1,result2,result3,result4,result5):
    
    cluster1 = [[0 for i in range(0,2)]for j in range(0,500)];
    cluster2 = [[0 for i in range(0,2)]for j in range(0,500)];
    cluster3 = [[0 for i in range(0,2)]for j in range(0,200)];
    cluster4 = [[0 for i in range(0,2)]for j in range(0,500)];
    cluster5 = [[0 for i in range(0,2)]for j in range(0,500)];
    j=0;
    for i in range(0,500):
        cluster1[j] = input_array[i];
        j=j+1;
    j=0;
    for i in range(500,1000):
        cluster2[j] = input_array[i];
        j=j+1;
    j=0;
    for i in range(1000,1200):
        cluster3[j] = input_array[i];
        j=j+1;
    j=0;
    for i in range(1200,1700):
        cluster4[j] = input_array[i];
        j=j+1;
    j=0;
    for i in range(1700,2200):
        cluster5[j] = input_array[i];
        j=j+1;
    
    result1 = np.array(result1);
    result2 = np.array(result2);
    result3 = np.array(result3);
    result4 = np.array(result4);
    result5 = np.array(result5);
    result1 = result1.T;
    result2 = result2.T;
    result3 = result3.T;
    result4 = result4.T;
    result5 = result5.T;
    f= plt.figure(1);

    plt.title("Result 3");
    plt.scatter(result1[0],result1[1],marker='^');
    plt.scatter(result2[0],result2[1],marker='+');
    plt.scatter(result3[0],result3[1],marker='.');
    plt.scatter(result4[0],result4[1],marker='*');
    plt.scatter(result5[0],result5[1],marker='p');
    cluster1 = np.array(cluster1);
    cluster2= np.array(cluster2);
    cluster3= np.array(cluster3);
    cluster4= np.array(cluster4);
    cluster5= np.array(cluster5);
    cluster1=cluster1.T;
    cluster2=cluster2.T
    cluster3 = cluster3.T;
    cluster4 = cluster4.T;
    cluster5 = cluster5.T;
    g=plt.figure(2);
    plt.title("Original 3");
    plt.scatter(cluster1[0],cluster1[1],marker='^');
    plt.scatter(cluster2[0],cluster2[1],marker='+');
    plt.scatter(cluster3[0],cluster3[1],marker='.');
    plt.scatter(cluster4[0],cluster4[1],marker='*');
    plt.scatter(cluster5[0],cluster5[1],marker='p');
    plt.show();


