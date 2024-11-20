import numpy as np
import cond_color
import pprint
from matplotlib import pyplot as plt
import seaborn as sns
import random
import tools
sns.set_theme()



def plot_neurons(X,times,num_neurons,num_conditions):

    colours = tools.gen_colors(num_neurons)

    fig, axs = plt.subplots(num_conditions,1,sharex=True,sharey=True)

    for neuron_index, neuron in enumerate(X[:num_neurons]):
        print(f'neuron shape:{np.shape(neuron)}')
        for condition_index,activations in enumerate(neuron[:num_conditions]):
            ax = axs[condition_index]
            ax.plot(times,activations,color = colours[neuron_index])
            ax.set_ylabel('average firing rate (Hz)')
            ax.set_title(f'condition {condition_index}')
    


    fig.legend([f'neuron {i}' for i in range(num_neurons)])

    plt.xlabel('time (ms)')
    plt.ylabel('average firing rate (Hz)')
    plt.show()

if __name__ == "__main__":
    data = np.load('psths.npz')
    X = data['X']
    
    times = data['times']

    avg = np.mean(X, axis=(0, 1))

    plt.title('Average firing rate across all neurons and conditions with time')
    plt.plot(times,avg)
    plt.xlabel('time (ms)')
    plt.ylabel('average firing rate (Hz)')
    plt.ylim(0,5)

    plt.show()