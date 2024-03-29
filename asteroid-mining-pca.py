import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# relevant asteroid characteristics from nasa jpl small-body database query
 features = ["q", "diameter", "albedo", "e", "a", "rot_per"]

# pca function

def pca(df, features):
  lst = df[features[0]].values[1::] # asteroid dataset in list form

  for feature in features:
    if (feature != feature[0]): # avoid double counting
      lst = np.vstack((lst, asteroids[feature].values[1::]))

  lst = lst.astype(np.float64)
  lst = lst.T # transposes the list to horizontal instead of vertical

  mean1 = np.mean(lst, axis = 0)

  zero_lst = np.zeros(lst.shape[0]) # make a list with the same dimensions as lst but with 0s
  mean2 = np.meshgrid(mean1, zero_lst)[0] # make a list with the same dimensions as lst but with the mean of that row
  mean_lst = lst - mean2

  upper_sum = np.sum((np.abs(mean_lst))**2, axis=0)
  std_dev = np.sqrt(upper_sum/mean_lst.shape[0])

  lst_scaled = mean_lst / std_dev

  covariance_lst = (1/(lst.shape[1]-1))*np.matmul(np.transpose(lst_scaled), lst_scaled)
  eigenvalues, eigenvectors = np.linalg.eig(covariance_lst)
  eigenvectors = eigenvectors.T

  index = eigenvalues.argsort()
  print(eigenvalues[np.flip(index)]/np.sum(eigenvalues))
  pca_x = np.matmul(lst_scaled, eigenvectors[index[-1]])
  pca_y = np.matmul(lst_scaled, eigenvectors[index[-2]])
  pca_z = np.matmul(lst_scaled, eigenvectors[index[-3]])

  return lst, pca_x, pca_y, pca_z, eigenvalues, eigenvectors, index

# graphing

# replace if necessary with your file path
asteroids = pd.read_csv('asteroids.csv')

# data cleaning through dropna
asteroids.dropna()

y = asteroids[features[0]].values[1::]
label_feature = features[0]

lst, pca_x, pca_y, pca_z, eigenvalues, eigenvectors, index = pca(asteroids, features)

y_min = np.min(y)
y_max = np.max(y)
y_range = y_max - y_min
split_num = 4
color_list = ["#88bbff", "#88ff91", "#ffcc88", "#ff88f7"]

split_increment = y_range / split_num 
print(split_increment)

split_indeces = []
label_list = []
label_text = "{minimum:.3f} <= {feature} < {maximum:.3f}"

for i in range(split_num):
    split_min = y_min + (split_increment * i)
    split_max = y_min + (split_increment * (i+1))
    split = np.where(np.logical_and(y >= split_min, y < split_max))
    split_indeces.append(split)
    label_list.append(label_text.format(minimum=split_min, feature=label_feature, maximum=split_max))

plt.close()
plt.title(str(np.round(np.sum(eigenvalues[np.flip(index)[0:2]]/np.sum(eigenvalues))*100, 1)) + '% of observed variation')
plt.scatter(pca_x, pca_y, color = '#a2a2a2', label = 'all data') 

# conduct quartile split on the graph
for i in range(split_num):
    plt.scatter(pca_x[split_indeces[i]], pca_y[split_indeces[i]], color=color_list[i], label = label_list[i])

plt.legend()
plt.show()
