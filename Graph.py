import matplotlib.pyplot as plt

def create_graph_img(array):
    rates = []
    for i in range(len(array)):
        rates.append(array[i][3])
    plt.plot((1, 2, 3, 4, 5), rates)
    plt.savefig("temp.png")