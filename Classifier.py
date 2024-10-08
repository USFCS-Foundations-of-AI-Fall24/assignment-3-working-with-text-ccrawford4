from Cluster import *
from Document import *
from make_dataset import create_docs
from test_Cluster import populate_documents


def classify(clusters, item) :
    dist = 10000
    best = None
    for c in clusters :
        d = cosine_similarity(c.centroid, item)
        if d < dist :
            dist = d
            best = c
    return best.centroid.true_class

def provide_true_classes(cluster_list) :
    for cluster in cluster_list :
        neg = 0
        npos = 0
        for doc in cluster.members :
            if doc.true_class == 'pos' :
                npos += 1
            else :
                neg += 1
        if npos >= neg :
            cluster.centroid.true_class = 'pos'
        else :
            cluster.centroid.true_class = 'neg'


def five_fold_cross_validation(nwords, nelements):
    documents = []
    ## generate nelements documents of each type (pos and neg), with nwords words in each doc.
    pos_docs, neg_docs = create_docs(nelements, nelements, length=nwords, use_random=True)
    populate_documents(pos_docs,'pos', documents)
    populate_documents(neg_docs,'neg', documents)

    random.shuffle(documents)
    data_size = len(documents)

    bucket_size = nelements // 4
    accuracy = 0
    for i in range(5):
        start_idx = i * bucket_size
        end_idx = (i + 1) * bucket_size if i < 4 else data_size
        test_data = documents[start_idx:end_idx]
        train_data = documents[:start_idx] + documents[end_idx:]

        sub_accuracy = 0
        trained_clusters = k_means(2, ['pos', 'neg'], train_data)
        provide_true_classes(trained_clusters)

        for doc in test_data :
            estimated_class = classify(trained_clusters, doc)
            if estimated_class ==  doc.true_class:
                sub_accuracy += 1
        accuracy += (sub_accuracy / len(test_data))

    return accuracy / 5

def run_classifier() :
    print("Five fold accuracy: ", five_fold_cross_validation(100, 100))