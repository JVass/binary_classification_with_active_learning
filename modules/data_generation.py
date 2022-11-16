import numpy as np
import matplotlib.pyplot as plt

class data_generator():
    def __init__(self, number_of_samples, seed):
        self.number_of_samples = number_of_samples
        np.random.seed(seed)

    def gaussian(self, mu, covariance_matrix):
        points = np.random.multivariate_normal(mean = mu, cov = covariance_matrix, size = self.number_of_samples)
        self.data = points

        return points

    def laplace_distribution(self, mu, lamda):
        pass

    def gamma(self, gamma):
        pass

class visualizer():
    def visualize_classes(self, first_class, second_class):
        plt.scatter(x = first_class[:,0], y = first_class[:,1], label = "First class")
        plt.scatter(x = second_class[:,0], y = second_class[:,1], label = "Second class")
        plt.show()
        plt.close()

    def visualize_classes_with_separation_line(self, first_class, second_class, theta):
        plt.scatter(x = first_class[:,0], y = first_class[:,1], label = "First class")
        plt.scatter(x = second_class[:,0], y = second_class[:,1], label = "Second class")

        x_min = first_class[:,0].min()
        x_max = second_class[:,0].max()

        x_values = np.expand_dims(np.linspace(x_min, x_max, 100), axis = 1)
        x_values = np.concatenate((x_values, np.ones_like(x_values)), axis = 1)
        
        y_values = np.dot(theta, x_values.T)

        plt.plot(x_values[:,0], y_values[0,:], 'r')

        plt.show()
        plt.close()