from sklearn import mixture
import sklearn.datasets
import matplotlib.pyplot as plt
import numpy as np
import generator as g;
from sklearn import preprocessing

def em(input_array,no_of_clusters):
    
    model = sklearn.mixture.GaussianMixture(n_components=no_of_clusters,covariance_type='diag')
    a = model.fit(X)
    print a.means_
    print a.weights_
    em = model.predict(X)
    
    l1=em[:59];
    l1.sort();
    print l1;
    l = [len(list(group)) for key, group in groupby(l1)]
    print l;
    l1=em[59:130];
    l1.sort();
    print l1;
    l = [len(list(group)) for key, group in groupby(l1)]
    print l;
    l1=em[130:178];
    l1.sort();
    print l1;
    l = [len(list(group)) for key, group in groupby(l1)]
    print l;



try:
    input_data = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv",delimiter=',');
except:
    print("Could not open file");
input_data = input_data[:,:13];
print input_data.shape;
em(input_data,3);
print("Completed");

