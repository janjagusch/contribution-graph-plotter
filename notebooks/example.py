# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # How to plot a contribution graph

from collections import Counter

from imageio import imread
from sklearn.cluster import KMeans
import numpy as np

from contribution_graph_plotter import plot

img = imread("../examples/python.png", format="png")

# +
# Grouping all existing colors in the image into 5 clusters,
# since we can only use 5 colors in the contribution graph.

colors = img.reshape(-1, img.shape[2])
clusterer = KMeans(n_clusters=5)
clusters = clusterer.fit_predict(colors)

# +
# Personal taste: the smaller the cluster, the brighter the color.
# Set `reverse=False` for opposite effect.

cluster_map = Counter(clusters)
cluster_map = {
    item[0]: i
    for i, item in enumerate(
        sorted(cluster_map.items(), key=lambda item: item[1], reverse=True)
    )
}
clusters = [cluster_map[val] for val in clusters]
# -

contribution_graph = np.array(clusters).reshape(img.shape[:2])
plot(contribution_graph, "../examples/python.svg")
