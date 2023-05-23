import numpy as np
from sklearn.neighbors import NearestNeighbors

# 最近傍探索

samples = [[0, 0, 2], [1, 0, 0], [0, 0, 1]]

neigh = NearestNeighbors(n_neighbors=2) #探す点の数
neigh.fit(samples)

print(neigh.kneighbors([[1., 1., 1.]])) #距離とインデックス番号

