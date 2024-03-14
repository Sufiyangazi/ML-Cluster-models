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
X = data.iloc[:,[3,4]]
X
# %%
from sklearn.cluster import KMeans
km = KMeans(n_clusters=5 ,
            max_iter=300,
            random_state=1234)
km
# %%
km.fit_predict(X)
# %%
km.inertia_
# %%
data['Cluster_group']=y_clusters
# %%
data.head()
# %%
data['Cluster_group'].value_counts()
# %%
data[data['Cluster_group']==0].iloc[:,[3,4]]
# %%
# Group the data points
cs_1=data[data['Cluster_group']==0].iloc[:,[3,4]]
cs_2=data[data['Cluster_group']==1].iloc[:,[3,4]]
cs_3=data[data['Cluster_group']==2].iloc[:,[3,4]]
cs_4=data[data['Cluster_group']==3].iloc[:,[3,4]]
cs_5=data[data['Cluster_group']==4].iloc[:,[3,4]]
# %%
d1=pd.DataFrame(dict(cs_1.mean()),index=['Cluster-1'])
d2=pd.DataFrame(dict(cs_2.mean()),index=['Cluster-2'])
d3=pd.DataFrame(dict(cs_3.mean()),index=['Cluster-3'])
d4=pd.DataFrame(dict(cs_4.mean()),index=['Cluster-4'])
d5=pd.DataFrame(dict(cs_5.mean()),index=['Cluster-5'])
pd.concat([d1,d2,d3,d4,d5])
# %%
plt.hist(cs_1['Spending Score (1-100)'])
# %%
try:
    plt.figure(figsize=(12,8))
    plt.scatter(X[y_clusters==0,0],X[y_clusters==0,1],s=100,c='red',label="Cluster1")
    plt.scatter(X[y_clusters==1,0],X[y_clusters==1,1],s=100,c='blue',label="Cluster2")
    plt.scatter(X[y_clusters==2,0],X[y_clusters==2,1],s=100,c='green',label="Cluster3")
    plt.scatter(X[y_clusters==3,0],X[y_clusters==3,1],s=100,c='cyan',label="Cluster4")
    plt.scatter(X[y_clusters==4,0],X[y_clusters==4,1],s=100,c='magenta',label="Cluster5")
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centriods')
    plt.title("Clusters using K-means")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending score")
    plt.legend()
    plt.show()
except Exception as e:
    print(f'An error occured')
# %%
