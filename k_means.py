from sklearn.cluster import KMeans
import sklearn.datasets
import numpy as np
from itertools import groupby


def k_means(data, no_of_clusters):
    print("Running k-means")
    data = np.array(data);
    kmeans = KMeans(no_of_clusters, random_state=0).fit_predict(data)
    for i in range(0,150):
        print(str(i) + " " + str(kmeans[i]));
    l1=kmeans[:50];
    l1.sort();
    
    l = [len(list(group)) for key, group in groupby(l1)]
    print (l);
    max1 = max(l);
    l1=kmeans[50:100];
    l1.sort();
    
    l = [len(list(group)) for key, group in groupby(l1)]
    print (l);
    max2 = max(l);
    l1=kmeans[100:150];
    l1.sort();
    
    l = [len(list(group)) for key, group in groupby(l1)]
    print (l);
    max3 = max(l);
    print("Clustering Accuracy = "+str(((max1+max2+max3)/150*100))+ " % ")
    

