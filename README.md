# MachineLearning
Personal Machine Learning repository for subjects ranging form Neural Networks, clustering, and genetic algorithms.


# Clustering
KMeansClustering implementation for dynamic amount of clusters, points, and iterations. Initializes amount of points specified using np.randn function. Generates 3 .png files in the same folder as the .py file consisting of initial points, first iteration of clusters and points assigned to clusters, and final iteration of clusters and points assigned. In the images, each color corresponds to a different cluster, where each red X is the centroid of a cluster. The initial points image simply shows the inital state of all the points.


# Genetic Algorithms
GeneticAlgIntro is an introductory practice to genetic algorithms using an object oriented process. It initializes a population of 10 lists of 5 numbers randomly assigned 0 or 1. It selects the first and second fittest of the population and perform a crossover between the two, creating two new offspring. A mutation is performed on both offspring on a random gene. Then both offspring are added onto the population list. This is performed until an offspring with all 1's is produced.

EquationMaxing is a genetic algorithm for maximizing the weights of an equation. This genetic algorithm takes half of the initial population and performs a successive crossover of the latter half of the values between them all, and performs a mutation of [-1, 1] on the fourth gene of each new population member. The new population is then made up of the selected parents and the offspring. This is performed a certain number of generations instead of being at a certain point due to not knowing if you have reached a local maxima or global maxima.
