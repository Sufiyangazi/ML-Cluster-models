# # %%
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns 
# import warnings
# warnings.filterwarnings('ignore')
# # %%
# file_path = 'C:\\Users\\Admin\\Downloads\\Mall_Customers.csv'
# df = pd.read_csv(file_path)
# df
# # %%
# X = df.iloc[:,[3,4]].values
# X
# # %%
# import scipy.cluster.hierarchy as sch
# # %%
# # - Linkage function
# # - Every observation is a one cluster
# sch.linkage(X,method='single')
# # %%
# # Example
# val = [[2,5],[3,6],[7,10],[12,10],[6,3],[10,20]]
# sch.linkage(val)
# # %%
# dendogram = sch.dendrogram(sch.linkage(val,method='single'))
# plt.title('Dendogram')
# plt.xlabel('Cousomers')
# plt.ylabel('Distance')
# plt.show()
# # %%
# plt.figure(figsize=(10,10))
# plt.title('Dendogram')
# plt.xlabel('Customers')
# plt.ylabel('Distance')
# dendogram_b = sch.dendrogram(sch.linkage(X,method='single'))
# plt.show()
# # %%
# plt.figure(figsize=(10,10))
# plt.title('Dendogram')
# plt.xlabel('Customers')
# plt.ylabel('Distance')
# dendogram_b = sch.dendrogram(sch.linkage(X,method='complete'))
# plt.show()
# # %%
# from sklearn.cluster import AgglomerativeClustering
# hc = AgglomerativeClustering(n_clusters=5,
#                              metric='euclidean',
#                              linkage='ward')
# y_hc = hc.fit_predict(X)
# y_hc
# %%
# Example
val = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
sch.linkage(val)
# %%
dendogram = sch.dendrogram(sch.linkage(val,method='single'))
plt.title('Dendogram')
plt.xlabel('Cousomers')
plt.ylabel('Distance')
plt.show()
# %%
val = [[1,2],[3,4]]
sch.linkage(val)
# %%
dendogram = sch.dendrogram(sch.linkage(val,method='single'))
plt.title('Dendogram')
plt.xlabel('Cousomers')
plt.ylabel('Distance')
plt.show()
# %%
