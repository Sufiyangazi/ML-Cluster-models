# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore') 
# %%
file_path = 'C:\\Users\\Admin\\Downloads\\Mall_Customers.csv'
data= pd.read_csv(file_path)
data
# %%
X = data.iloc[:,[3,4]].values
# %%
X
# %%
data.columns
# %%
# K-Means

# - we need to decide the number of clusters
# - Elbow method
# - Within sum of squares
# - we randomly gives 10 clusters , for each cluster will calculate 
# - Within sum of squares
#  first we check for one cluster to understand within sum of squares concept
# %%
from sklearn.cluster import KMeans 

# %%
KMeans_1 = KMeans(n_clusters=1,
                  max_iter=300,
                  random_state=1234)
KMeans_1
# %%
KMeans_1.fit(X)
# %%
KMeans_1.inertia_ # Variance
# %%
KMeans_1.cluster_centers_
# %%
wss = []
for i in range(1,10):
    Kmeans = KMeans(n_clusters=i,max_iter=300,random_state=1234)
    Kmeans.fit(X)
    wss.append(round(Kmeans.inertia_,2))
# %%
wss
# %%
plt.plot(range(1,10),wss)
plt.title('The Elbow Method')
plt.xlabel('Clusters')
plt.ylabel('wss')
plt.show()
# %%
# read
# x
#
kmeans =KMeans(n_clusters=5,max_iter=300,random_state=1234)
y_clusters = Kmeans.fit_predict(X)
y_clusters
#- here 0 = 
# %%
