import numpy as np
import matplotlib.pyplot as plt

colors = ["blue", "green", "orange", "purple", "pink", "black", "brown"]
centroids = []
points = []
cluster_points = dict()


def display_scatter_plot(plt_save_count, cluster_count):
    cen_x, cen_y = [], []
    for i in range(cluster_count):
        cen_x.append(centroids[i][0])
        cen_y.append(centroids[i][1])
    plt.scatter(cen_x, cen_y, marker='X', s=60, c='red')

    for centroid in range(cluster_count):
        cen_x, cen_y = [], []
        for i in range(len(cluster_points[centroid])):
            cen_x.append(cluster_points[centroid][i][0][0])
            cen_y.append(cluster_points[centroid][i][1][0])
        plt.scatter(cen_x, cen_y, marker='o', c=colors[centroid])
    plt.savefig("plt%d.png" % plt_save_count)
    plt.show()

def inital_scatter_plot(points):
    cen_x, cen_y = [], []
    for i in range(len(points)):
        cen_x.append(points[i][0][0])
        cen_y.append(points[i][1][0])
    plt.scatter(cen_x, cen_y, marker='o')
    plt.savefig("initial_plt.png")


# Will be implemented in the near future.
def silhouette_coefficient():
    pass


def KMeansCluster(cluster_count, point_count, iterations):
    plt_save_count = 0

    for i in range(cluster_count):
        cluster_points[i] = []
    for i in range(point_count):
        points.append((np.random.randn(1), np.random.randn(1)))
    for i in range(cluster_count):
        centroids.append((np.random.randn(1), np.random.randn(1)))

    inital_scatter_plot(points)

    for iteration in range(iterations):
        for i in range(point_count):
            euc_dist = np.sqrt(((points[i][1][0] - centroids[0][1][0]) ** 2) + ((points[i][0][0] - centroids[0][0][0]) ** 2))
            adding_to = 0
            for j in range(cluster_count):
                new_dist = np.sqrt(((points[i][1][0] - centroids[j][1][0]) ** 2) + ((points[i][0][0] - centroids[j][0][0]) ** 2))
                if new_dist < euc_dist:
                    euc_dist = new_dist
                    adding_to = j
                else:
                    pass
            cluster_points[adding_to].append(points[i])

        if iteration == 0:
            display_scatter_plot(plt_save_count, cluster_count)
            plt_save_count = plt_save_count + 1
        elif iteration == (iterations - 1):
            display_scatter_plot(plt_save_count, cluster_count)
            plt_save_count = plt_save_count + 1
        else:
            pass

        for i in range(cluster_count):
            x_change, y_change = [], []
            for j in range(len(cluster_points[i])):
                x_change.append(cluster_points[i][j][0][0] - centroids[i][0][0])
                y_change.append(cluster_points[i][j][1][0] - centroids[i][1][0])
            centroids[i][0][0] = centroids[i][0][0] + np.average(x_change)
            centroids[i][1][0] = centroids[i][1][0] + np.average(y_change)

        for i in range(cluster_count):
            cluster_points[i] = []


# Example KMeansClustering with 5 clusters, 100 points, at 500 iterations.
KMeansCluster(5, 100, 500)