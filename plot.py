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
        result = k_means(2, ['pos', 'neg'], documents)
        accuracy = 0
        for cluster in result :
            if accuracy == 0 :
                accuracy += compute_homogeneity(cluster)
            else :
                accuracy = (accuracy + compute_homogeneity(cluster) / 2)
        y_axis.append(accuracy)

    plt.title("Homogeneity of Clusters")
    plt.xlabel("Document Size")
    plt.ylabel("Accuracy")
    plt.plot(x_axis, y_axis)
    plt.show()

if __name__ == '__main__':
    # plot_k_means()
    documents = []
    pos_docs, neg_docs = create_docs(100, 100, True)
    populate_documents(pos_docs, 'pos', documents)
    populate_documents(neg_docs, 'neg', documents)
    result = k_means(2, ['pos', 'neg'], documents)
    accuracy = 0
    for cluster in result :
        if accuracy == 0 :
            accuracy += compute_homogeneity(cluster)
        else :
            accuracy = (accuracy + compute_homogeneity(cluster) / 2)

    print("Accuracy: ", accuracy)