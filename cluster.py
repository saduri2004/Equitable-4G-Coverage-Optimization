import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Function to assign each data point to the nearest cluster centroid
def assign_to_clusters(data, centroids):
    num_clusters = len(centroids)
    num_points = data.shape[0]
    assignments = np.zeros(num_points, dtype=int)

    for i in range(num_points):
        distances = [euclidean_distance(data[i], centroid) for centroid in centroids]
        assignments[i] = np.argmin(distances)

    return assignments

# Function to update cluster centroids based on the mean of assigned points
def update_centroids(data, assignments, num_clusters):
    new_centroids = np.zeros((num_clusters, data.shape[1]))

    for i in range(num_clusters):
        cluster_points = data[assignments == i]
        if len(cluster_points) > 0:
            new_centroids[i] = np.mean(cluster_points, axis=0)

    return new_centroids

# Generate some random data for clustering (you can replace this with your data)
np.random.seed(0)
num_samples = 300
num_features = 2
data = np.random.randn(num_samples, num_features)

# Number of clusters
num_clusters = 3

# Initialize cluster centroids randomly
initial_centroids = data[np.random.choice(num_samples, num_clusters, replace=False)]

# Perform K-means clustering
max_iterations = 100
tolerance = 1e-4
centroids = initial_centroids

for iteration in range(max_iterations):
    old_centroids = centroids.copy()

    # Assign data points to the nearest cluster
    assignments = assign_to_clusters(data, centroids)

    # Update cluster centroids
    centroids = update_centroids(data, assignments, num_clusters)

    # Check for convergence
    if np.all(np.abs(centroids - old_centroids) < tolerance):
        break

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=assignments, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='red', label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
