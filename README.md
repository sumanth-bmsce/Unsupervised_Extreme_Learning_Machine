# Unsupervised Extreme Learning Machine with Automated Clustering 
Unsupervised Extreme Learning Machine(ELM) is a non-iterative algorithm used for feature extraction. This method is applied on the IRIS Dataset for non-linear feature extraction, cluster prediction and finally clustering is carried out using k-means.

<h3> Objective </h3>

To perform non-linear feature learning using Unsuoervised Extreme Learning Machine, predicting the number of clusters in the dataset using Bayesian Information Criterion (BIC) and finally clustering using k-means

<h3> Modules </h3>

1. **Unsupervised Extreme Learning Machine** : In this module, feature extraction of the dataset is performed using Unsupervised Extreme Learning Machine. It is a **non-iterative** algorithm with a single hidden layer where the weights between the input layer and the hidden layer are randomly initialized and the weights between the hidden layer and the output layer are computed using the objective function. Hence, it is guaranteed to converge at a global minima.

2. **Bayesian Information Criterion** : Bayesian Information Criterion is a statistical method use dto find out the number of clusters in the dataset. It uses the Expectation Maximization(EM) ALgorithm to find the number of clusters in the dataset. This module is added to automate the process of cluster prediction as for k-means clustering we need to specify priorly the number of clusters.

3.**Techniques used for clustering feature learning information obtained from Unsupervised ELM**

i. **K-means Clustering** : Linearly clustering where input is the feature learning information from Unsupervised ELM and the number of clusters from BIC. Finally, we display the confusion matrix and clustering accuracy.

ii. **Self Organizing Maps / Kohonen Network** : It is a clustering technique developed by Kohonen visualized as a neural network. It has only 2 layers : the input layer and the output layer. The number of input layer neurons is the no of features in the dataset and the number of output neurons is the desired number of clusters.  It updates the weights between the layers based on the neighbourhood concept and the minimum distance criteria. In this implementation a Gaussian neighbourhood is used.

iii. **Clustering using Expectation Maximization (EM Algorithm)** : EM clustering is a soft clustering technique whereas the above two mentioned methods are hard clustering methods. In soft clustering, instead of putting each data point into a separate cluster, a probability or likelihood of that data point to be in those clusters is assigned. For whichever cluster, the likelihood of that sample is high, the sample is assigned to that particular cluster. 

<h3> Results Screenshots </h3>

1. **Clustering Accuracy** : The clustering accuracy achieved for IRIS dataset is 96.67% which was the highest. The number of hidden neurons set was 120.

![res1](https://github.com/sumanth-bmsce/Unsupervised_Extreme_Learning_Machine/blob/master/ELM_kmeans_ClusteringResult.png)</br>

2. **Cluster Prediction using BIC** : The number of clusters predicted by BIC is 3 which matches the original number of clusters in the Iris Dataset. The number of clusters is found out using the Elbow Criterion from BIC value vs no of clusters graph.

![res2](https://github.com/sumanth-bmsce/Unsupervised_Extreme_Learning_Machine/blob/master/BIC_Iris.png)</br>

<h3> References </h3>

[1] Senthilnath, J.; Simha C, S.; G, N.; Thapa, M.; M, I.	BELMKN: Bayesian Extreme Learning Machines Kohonen Network. Algorithms 2018, 11, 56. </br>
Link : http://www.mdpi.com/1999-4893/11/5/56</br>
[2] Huang, G.; Song, S.; Gupta, J.N.; Wu, C. Semi-supervised and unsupervised extreme learning machines. IEEE Trans. Cybern. 2014, 44, 2405–2417. 


