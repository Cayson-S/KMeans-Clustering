KMeans_Clustering
==============================

    This project uses the K-means clustering algorithm to classify data. K-means clustering is 
an unsupervised algorithm. This means that it does not make any assumptions about how the 
data is structured. This is contrasted by a supervised algorithm which assumes the data forms a 
straight line (linear), is curved (quadratic), or another shape. Because of this, K-means 
clustering relies on the data to determine the structure of the data (Phillips, 2022). The result of 
the algorithm is a series of k centers. The number of centers, k, is chosen by the user. These 
centers are in n dimensions, where n is the number of dimensions where the data is located. 
This project finds those k centers and then tests the result to elucidate the mean accuracy when 
using different amounts of clusters.
    K-means clustering, as implemented in the project, follows several steps. First, two 
datasets are input into the program: the training and test sets. The training set is used to build 
the model, and the test set determines how accurately the model can generalize to new data. 
The program also takes in the number of clusters (k) the user would like created. The clusters 
are initialized by taking the first k rows from the training dataset and making those the 
locations of the clusters. It is assumed that the training set is randomly shuffled before running 
the program to ensure the clusters are located randomly throughout the state space. Following 
the initialization of the clusters, the program calculates the distance from every point to each 
cluster. Each point is assigned to the cluster to which it is closest. The points are then averaged 
across assigned clusters, and these values are designated as the new location for each cluster. 
The points closest to the new clusters are then assigned to those clusters and so on until the 
points closest to each cluster do not change. This means that the clusters will no longer change 
location, and the algorithm has converged. 
    An example of the K-means algorithm is shown in Figure 1. In this example, the clusters 
were randomly generated somewhere in the state space instead of being initialized on a 
random data point. Cluster one is given by C1, and cluster two by C2. The three points directly 
above C2 are the points closest to C2, and the rest are closest to C1. The three points above C2 
are averaged, and C2 is moved to that location ([-1.0, -0.1]). The same process is done for C1 
(moved to [0.125, 0.375]) with its corresponding points. We determine the new cluster 
membership and find that there is no change. Thus, the algorithm has converged

Figure 1
K-Means Clustering Example

    Once the algorithm has converged, a class label is assigned to each cluster. These labels 
are the predicted classes for data closest to each cluster. For example, if we wanted to predict 
an Iris type from data on its sepal length, width, etc., then an Iris type would be given as a class 
label to the clusters by majority vote. That is, if most of the data close to cluster zero 
correspond to a specific Iris type, then that cluster would be assigned that class. For this 
project, classes will be represented as integers starting from zero. Given this, cluster zero from 
the Iris example might be assigned a class label of “2.” If there is not a majority vote for a 
specific class (e.g. there is a tie in class occurrence), then the lower class label would be 
assigned. These class labels allow us to predict a class from new data by determining to which 
cluster the new data is closest.
    Upon running the program, I came across an issue with clusters that did not have any 
data points associated with them. There were two reasons why that happened, and I fixed both 
separately. First, points may exist that are equidistant from several clusters. This results in one 
cluster being given all the nodes and the other left empty. I fixed this by having the algorithm 
prefer to place data into an empty cluster, given that they are all equidistant from the point. 
The second issue I found was that some clusters were not representative of any data when the 
algorithm converged. This meant that no class could logically be chosen to assign to that 
cluster. I solved this by randomly assigning those clusters with one of the possible class values. I 
made both of these decisions because I am testing accuracy at specific numbers of clusters. It 
might be a better fit to remove extraneous clusters, but that would cause inaccuracies when 
trying to determine accuracies for specific clusters.
    Two datasets will be used to test the accuracy of K-means clustering in generalizing to 
new data. The first dataset is the Iris classification dataset that was discussed earlier in the 
report (University of California Irvine, 1988). The second dataset looks at data from breast 
tissue to predict breast cancer or one of several types of benign growths (University of 
California Irvine, 2010). Both datasets are shuffled and then split, with ten rows of data being 
used to test the model and the rest used to train it (a form of cross-validation). Different 
numbers of clusters are used to determine which had the best accuracy. The number of clusters 
ranged from one to the total number of data points in the training dataset. K-means clustering 
was run 100 times for each number of clusters. This data was compiled, and the means and 
standard errors were graphed in Figure 2 and Figure 3.

Figure 2
Iris Test Prediction Accuracy

Figure 3
Cancer Test Prediction Accuracy

    Figure 2 shows the mean accuracy of the clustering for each number of clusters. The accuracy starts low when there is only one cluster. This quickly increases to where it maxes out at around seven through ten clusters. From there, the mean accuracy slowly decreases, indicating that the training data is overfit.A model overfits the training data when it models the training data too closely and is unable to generalize well to new data. The black lines above the bars represent 1.96 standard errors above and below the mean. They are much wider at a low and high number of clusters indicating a larger amount of variance in the accuracy. This further proves that very small numbers of clusters (up to around seven) are not very good fits for the  data. The same is true for increasingly large numbers of clusters.
    Figure 3 shows the mean accuracy using the cancer dataset. There is a marked decrease 
in mean accuracy compared to the Iris dataset. Nonetheless, the model still peaks at around ten 
clusters. There does not seem to be much variation in standard errors in this graph, but they do 
appear to be larger than in Figure 2. This indicates greater variation in the accuracy of cancer 
prediction.
    K-means clustering can be seen to very accurately model data that is clearly grouped as 
in Figure 2. The cancer dataset does not have clear groups between classes. This is likely why Kmeans clustering is unable to accurately model the data. While both datasets were modeled 
better at smaller numbers of clusters, I do not expect this to be the rule. Instead, I expect the 
number of clusters necessary to best model the data would increase as the number of classes 
increases.
    To conclude, K-means clustering is very good at finding meaning from unclassified data 
(Phillips, 2022). I found that the model does well when considering the Iris dataset but that 
accuracy declines in the cancer dataset. This is likely due to a lack of clear clusters in the data. 
Some methods seek to compensate for this issue, such as spectral clustering. This algorithm 
builds off the K-means algorithm but projects the data into higher dimensions to make groups 
easier to partition (Phillips, 2022). Nonetheless, K-means clustering Is a powerful tool for 
modeling using unclassified data.

References

Phillips, J. (2022). Unsupervised Learning. 
https://jupyterhub.cs.mtsu.edu/azuread/services/csci4350-materials/private/2022-11-
09_Chapter_18b.pdf
Sakkaf, Y. (2020). Decision Trees: ID3 Algorithm Explained. 
https://towardsdatascience.com/decision-trees-for-classification-id3-algorithm-explained89df76e72df1
University of California Irvine (1988). Iris Data Set. https://archive.ics.uci.edu/ml/datasets/Iris 
University of California Irvine (2010). Breast Tissue Data Set. 
https://archive.ics.uci.edu/ml/datasets/Breast+Tissue

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
