from sklearn.cluster import KMeans
from numpy import genfromtxt
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

base_path = 'input/assingment-1-data/'
dirfiles = os.listdir(base_path+'data/')
dirfiles.sort(key=lambda f: int(re.sub('\D','',f)))


s = np.zeros((56, 9))
for file in dirfiles:
    data = genfromtxt( file, delimiter=',')
    for j in range(2, 11):
        kmeans = KMeans(n_clusters= j , random_state=0).fit( file[:,0:-1])
        s[i-1, j-2] = silhouette_score(file[:,0:-1], kmeans.labels_, metric='euclidean');
        plt.boxplot(data)

data.to_excel(r'/File Name.xlsx', index = False)
