import random
import math
import numpy as np;
import sklearn.datasets;
from sklearn.metrics import confusion_matrix;


# function returns the updated neighbourhood function for each of the output neurons as a list
def neighbourhood(no_of_iterations,winning_index,alpha0,sigma0,T1,T2,no_of_clusters):
    nh=[0]*no_of_clusters;
    learning_rate = alpha0*math.exp((-no_of_iterations)*1.0/(T1));
    sigma = sigma0*math.exp((-no_of_iterations)*1.0/(T2));
    for h in range(0,no_of_clusters):
        nh[h]=learning_rate*math.exp((-(pow(abs(winning_index-h),2)))/(2*pow(sigma,2)));
    return nh;

# function returns the index of the input neuron for one datapoint
def distance(weight,input_array,input_no,input_dim,no_of_clusters):
    distance_sum=[0]*no_of_clusters;
    for i in range(0,no_of_clusters):
        for j in range(0,input_dim):
            distance_sum[i]=distance_sum[i]+pow(abs(input_array[input_no][j]-weight[j][i]),1);
    [c**0.5 for c in distance_sum]
    return distance_sum.index(min(distance_sum));

def weight_adaptation(weight,nh,input_array,no_of_iterations,input_no,input_dim,no_of_clusters):
   
    for i in range(0,no_of_clusters):
        for j in range(0,input_dim):
            weight[j][i]=weight[j][i]+nh[i]*(input_array[input_no][j]-weight[j][i]);


def SelfOrganizingMaps(input_array, alpha0, no_of_clusters,N):
    input_dim=len(input_array[0]);
    # No of Clusters
    no_of_clusters=3;
    sigma0 = (no_of_clusters)*1.0/2;
    T1=N;
    T2=N/math.log(sigma0);
    
    input_array = np.array(input_array);
    input_array = input_array.T;
    no_of_inputs = len(input_array[0]);
    input_array = input_array.T;

    # Generating the random weight matrix
    weight=[[random.uniform(0,1) for i in range(no_of_clusters)] for j in range(input_dim) ]
    # As the confusion matrix is static I have initialized a particular weight matrix generated randomly


    k=0;
    min_index2=[0]*no_of_inputs;
    #confusion_matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(0,N):
    
        if(k==no_of_inputs):
            k=0;
    
        z=distance(weight,input_array,k,input_dim,no_of_clusters);
        #print("Winning Neuron");
        #print(z);
        nh=neighbourhood(i,z,alpha0,sigma0,T1,T2,no_of_clusters);
        weight_adaptation(weight,nh,input_array,i,k,input_dim,no_of_clusters);
        k=k+1;
    
    for i in range(0,150):
        min_index2[i]=distance(weight,input_array,i,input_dim,no_of_clusters);
        print(str(i+1)+"="+"Cluster"+str(min_index2[i]));

    actual = [[0 for i in range(0,1)] for j in range(0,150)];
    for i in range(0,50):
        actual[i] = 0;
    for i in range(50,100):
        actual[i] = 1;
    for i in range(100,150):
        actual[i] = 2;
    print confusion_matrix(actual,min_index2);



# Main SOM Program

iris = sklearn.datasets.load_iris()
input_array = iris.data[:, :4];
SelfOrganizingMaps(input_array,0.02,3,100000);
