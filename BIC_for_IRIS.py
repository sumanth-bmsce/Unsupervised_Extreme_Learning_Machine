from sklearn import mixture
import sklearn.datasets
import matplotlib.pyplot as plt
import numpy as np


def bic(X):
  # Varying number of clusters from k=1 to k=10
  range_n_clusters = range(1, 10)
  bic_list = []
  for n_clusters in range_n_clusters:
     model = sklearn.mixture.GaussianMixture(n_components=n_clusters,covariance_type='diag')
     model.fit(X)
     bic_list.append(model.bic(X))

  plt.plot(range_n_clusters, bic_list, marker='o')
  plt.xlabel("No of clusters");
  plt.ylabel("BIC Value");
  plt.title("BIC");
  # The optimal no of clusters is the corresponding x-axis value for which the bic curve drifts from a higher value to a lower value.(Elbow Method)
  plt.show()

# IRIS DATA
iris = sklearn.datasets.load_iris()
X = iris.data[:, :4];
bic(X);
