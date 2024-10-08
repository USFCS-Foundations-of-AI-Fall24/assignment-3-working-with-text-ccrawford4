from Loader import compute_homogeneity
from make_dataset import create_docs
from test_Cluster import populate_documents
from Cluster import *
from matplotlib import pyplot as plt

def plot_k_means():
    x_axis = []
    y_axis = []
    documents = []
    sizes = [25, 50, 100, 500, 1000]
    for size in sizes :
        pos_docs, neg_docs = create_docs(size, size, True)
        populate_documents(pos_docs, 'pos', documents)
        populate_documents(neg_docs, 'neg', documents)
        x_axis.append(size)
        clusters = k_means(2, ['pos', 'neg'], documents)
        accuracy = compute_accuracy(clusters)
        y_axis.append(accuracy)

    plt.title("Homogeneity of Clusters")
    plt.xlabel("Document Size")
    plt.ylabel("Accuracy")
    plt.plot(x_axis, y_axis)
    plt.show()

def compute_accuracy(cluster_list) :
    h_list = compute_homogeneity(cluster_list, ['pos', 'neg'])
    accuracy = sum(h_list) / len(h_list)
    return accuracy