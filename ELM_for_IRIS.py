import numpy as np;
from scipy import stats;
from sklearn import preprocessing
import random;
import math;
import sklearn.datasets
import AIC as ai;
import k_means as k;




def regression_matrix(input_array,input_hidden_weights,bias):
    input_array = np.array(input_array);
    input_hidden_weights = np.array(input_hidden_weights);
    bias = np.array(bias);
    regression_matrix = np.add(np.dot(input_array,input_hidden_weights),bias);
    return regression_matrix;

# Finding hidden layer activations
def hidden_layer_matrix(regression_matrix):
    sigmoidal = [[0.0 for i in range(0,no_of_hidden_neurons)]for j in range(0,no_of_inputs)];
    for i in range(0,no_of_inputs):
        for j in range(0,no_of_hidden_neurons):
            sigmoidal[i][j] = (1.0)/(1+math.exp(-(regression_matrix[i][j])))    
    return sigmoidal

# Calculating the similarity matrix (S)
def similarity_matrix():
    dist_array = [[0.0 for i in range(0,no_of_inputs)]for j in range(0,no_of_inputs)]
    for i in range(0,no_of_inputs):
        for j in range(0,no_of_inputs):
            for k in range(0,input_dim):
                dist_array[i][j] +=  pow((input_array[i][k] - input_array[j][k]),2);
    
    for i in range(0, no_of_inputs):
        for j in range(0, no_of_inputs):
            dist_array[i][j] = math.exp((-(dist_array[i][j]))/(2*pow(sigma,2.0)));
    return dist_array;

# Calculation of Graph Laplacian (L)
def laplacian_matrix(similarity_matrix):
    diagonal_matrix = [[0.0 for i in range(0,no_of_inputs)]for j in range(0,no_of_inputs)];
    diagonal_matrix = np.array(diagonal_matrix);
    similarity_matrix = np.array(similarity_matrix);
    for i in range(0,no_of_inputs):
       for j in range(0,no_of_inputs):
           diagonal_matrix[i][i] += similarity_matrix[i][j];
    
    return np.subtract(diagonal_matrix,similarity_matrix);

    
print("Running ELM")
input_dim=4;
# Loading Iris Dataset
iris = sklearn.datasets.load_iris()
data = iris.data[:, :4];
# Min-Max Normalization 
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0.1,0.9))
input_array = min_max_scaler.fit_transform(data);

input_array = np.array(input_array);
no_of_inputs = 150;
no_of_input_neurons = input_dim;
no_of_hidden_neurons = 120;
no_of_output_neurons = 100;
sigma = 1000
input_hidden_weights = [[random.uniform(0,1) for i in range(0,no_of_hidden_neurons)]for j in range(0,no_of_input_neurons)];

bias = [[1.0 for i in range(0,no_of_hidden_neurons)]for j in range(0,no_of_inputs)];
trade_off_parameter = 0.000000000000000000000000000001


hidden_matrix  = np.array(hidden_layer_matrix(regression_matrix(input_array,input_hidden_weights,bias)));

laplacian_matrix=np.array(laplacian_matrix(similarity_matrix()));
intermediate = np.dot(np.dot(hidden_matrix.T,laplacian_matrix),hidden_matrix);


a = [[0.0 for i in range(0,no_of_hidden_neurons)]for j in range(0,no_of_hidden_neurons)];
for i in range(0,no_of_hidden_neurons):
    for j in range(0,no_of_hidden_neurons):
        a[i][i] = 1.0;
a = np.array(a);
a = np.add(a,trade_off_parameter*intermediate);

eig_value , eig_vector = np.linalg.eig(a);

eig_vector = eig_vector.T;
req_eigen_vectors = [[0.0 for i in range(0,no_of_hidden_neurons)] for j in range(0,no_of_output_neurons)];
req_eigen_vectors = np.array(req_eigen_vectors);

# Sorting the eigen vectors using the eigen values
for i in range(0,len(eig_value)-1):
     for j in range(0,len(eig_value)-i-1):
         if(eig_value[j]>eig_value[j+1]):
             eig_value[j],eig_value[j+1]=eig_value[j+1],eig_value[j];
             eig_vector[j],eig_vector[j+1]=eig_vector[j+1],eig_vector[j];
             
# Finding n0 smallest eigen values
for i in range(0,no_of_output_neurons):
    req_eigen_vectors[i] = eig_vector[i];
    
    req_eigen_vectors[i] = np.divide(req_eigen_vectors[i],np.linalg.norm(np.dot(hidden_matrix,req_eigen_vectors[i].T)))

hidden_matrix = np.array(hidden_matrix);
req_eigen_vectors = np.array(req_eigen_vectors);

output_matrix = np.dot(hidden_matrix,(req_eigen_vectors.T));

i=0;
print("Final Weights")
print(req_eigen_vectors)

k.k_means(output_matrix,no_of_clusters);




    
