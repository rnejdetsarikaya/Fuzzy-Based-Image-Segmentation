import numpy as np
import math
from matplotlib import pyplot as plt

def gaussmf(x, mean, sigma):
    
    return np.exp(-((x - mean)**2.) / (2 * sigma**2.))


def mean_mf(value,label):
    if label=="low":
        return gaussmf(value, 0, 50)
    elif label=="medium":
        return gaussmf(value, 127, 50)
    return gaussmf(value, 255, 50)


def std_mf(value,label,max_,min_):
    if label=="low":
        return gaussmf(value, min_, 3)
    elif label=="high":
        return gaussmf(value,max_, 20)
    return gaussmf(value, (max_ + min_)/2, 3)


def output_mf(value,label):
    if label=="E":#E->Edge NE-> Not Edge
        return gaussmf(value,0,50)
    return gaussmf(value,255,50)


def draw_mean_mf():
    x_values = np.linspace(0, 255, 127)
    plt.plot(x_values, mean_mf(x_values,'low'),color="blue")
    y_values = np.linspace(0, 255, 127)
    plt.plot(y_values, mean_mf(y_values,'medium'),color="red")
    z_values = np.linspace(0, 255, 127)
    plt.plot(z_values, mean_mf(z_values,'high'),color="black")
    plt.savefig('mean.png')
    plt.show()


def draw_std_mf(max_,min_):
    x_values = np.linspace(max_, min_, 100)
    plt.plot(x_values, std_mf(x_values,"low",max_,min_),color="blue")
    y_values = np.linspace(min_, max_, 100)
    plt.plot(y_values, std_mf(y_values,"medium",max_,min_),color="red")
    z_values = np.linspace(min_, max_, 100)
    plt.plot(z_values, std_mf(z_values,"high",max_,min_),color="black")
#     plt.show()
    plt.savefig('std.png')
    plt.show()


def draw_output_mf():
    x_values = np.linspace(0, 255, 127)
    plt.plot(x_values, output_mf(x_values,"E"),color="blue")
    y_values = np.linspace(0, 255, 127)
    plt.plot(y_values, output_mf(y_values,"NE"),color="red")
#     plt.show()
    plt.savefig('output.png')
    plt.show()
