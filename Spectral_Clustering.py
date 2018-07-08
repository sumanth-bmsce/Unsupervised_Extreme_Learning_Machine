from sklearn.cluster import KMeans
import sklearn.datasets
import numpy as np
import csv;
from itertools import groupby
from sklearn.cluster import SpectralClustering




def spectral_clustering(data, no_of_clusters):
    data = np.array(data);
    spectral= SpectralClustering(n_clusters=no_of_clusters,eigen_solver='arpack', affinity="nearest_neighbors").fit_predict(data)
    l1=spectral[:59];
    l1.sort();
    print l1;
    l = [len(list(group)) for key, group in groupby(l1)]
    print l;
    l1=spectral[59:130];
    l1.sort();
    print l1;
    l = [len(list(group)) for key, group in groupby(l1)]
    print l;
    l1=spectral[130:178];
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
#iris = sklearn.datasets.load_iris()
#X = iris.data[:, :4];
spectral_clustering(input_data,3);
print("Completed");

