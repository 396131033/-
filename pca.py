#-*-  coding = utf-8 -*-  
#@Time : 2020/8/14 20:27
#@Author : 贾先圆
#@File: pca.py
#@Software: PyCharm

from sklearn import datasets
from sklearn.decomposition import PCA

# Load the data
digits_data = datasets.load_digits()
n = len(digits_data.images)

# Each image is represented as an 8-by-8 array.
# Flatten this array as input to PCA.
image_data = digits_data.images.reshape((n, -1))
image_data.shape(1797, 64)

# Groundtruth label of the number appearing in each image
labels = digits_data.target
# labels
# array([0, 1, 2, ..., 8, 9, 8])
# Fit a PCA transformer to the dataset.
# The number of components is automatically chosen to account for
# at least 80% of the total variance.
pca_transformer = PCA(n_components=0.8)
pca_images = pca_transformer.fit_transform(image_data)
pca_transformer.explained_variance_ratio_
# array([ 0.14890594, 0.13618771, 0.11794594, 0.08409979, 0.05782415,
#         0.0491691 , 0.04315987, 0.03661373, 0.03353248, 0.03078806
# ,
#         0.02372341, 0.02272697, 0.01821863])
pca_transformer.explained_variance_ratio_[:3].sum()
# 0.40303958587675121

# Visualize the results
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# >>> %matplotlib notebook
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(100):
    ax.scatter(pca_images[i,0], pca_images[i,1], pca_images[i,2],
    marker=r'![{}](../images/tex-99914b932bd37a50b983c5e7c90ae93b.gif)'.format(labels[i]), s=64)

    ax.set_xlabel('Principal component 1')
    ax.set_ylabel('Principal component 2')
    ax.set_zlabel('Principal component 3')