#アイテムベースで協調フィルタリングで映画をリコメンドする
# pandasでデータを読み込む
# 疎行列を作成する
# 最近傍探索で近い映画を探索する

import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

df = pd.read_csv('data/ratings.csv')

print(df.head())

# 疎行列（ほとんどの要素が0の行列)を作成する　アイテムユーザー行列
# 行と列を入れ替え
df_rating = df.pivot(index='movieId', columns="userId", values="rating").fillna(0) #fillnaでNaNを0に置き換え
print(df_rating.head())

# 最近傍探索
neigh = NearestNeighbors(metric="cosine") #cosin

#学習する
neigh.fit(df_rating)

# movieId2に近いの映画を探索する
distance, indices = neigh.kneighbors(df_rating[df_rating.index == 2])

print(indices) #movieIDが出力されるわけではない。二次元リスト（インデックス）　indicesはただ何番目のデータかを表している
print(indices.flatten()) #一次元リストに返還

# movieIDを表示する
for i in indices.flatten():
    print(df_rating.index[i]) #i番目のmovieIdを取得する



print('*****************************************************')
print('ユーザーベース')

#アイテムベースとほぼ同じ

import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

df = pd.read_csv('data/ratings.csv')

# indexとcolumnを入れ替え
df_rating = df.pivot(index='userId', columns="movieId", values="rating").fillna(0) #fillnaでNaNを0に置き換え
print(df_rating.head())

# 最近傍探索
neigh = NearestNeighbors(metric="cosine") #cosin

#学習する
neigh.fit(df_rating)

# userId=2に似ているヒトを探索する
distance, indices = neigh.kneighbors(df_rating[df_rating.index == 2])

# userIDを表示する
for i in indices.flatten():
    print(df_rating.index[i]) #i番目のuserIdを取得する

#出力されたユーザーの評価点の高い映画をおススメするなど様々な方法がある

#近い人の評価点が高いものを表示する 今回は、userId=366
movie_list = df[df['userId'] == 366]

#点数の高い順に表示する
print(movie_list.sort_values(by="rating",ascending=False)) #ascending=Falseで高い順





