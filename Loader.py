## Code for loading training sets and creating documents.
import operator
import string

from Document import *
from Cluster import *
from make_dataset import create_docs


# you should be able to call this like:
# positive_docs = create_easy_documents(pos_reviews, 'pos',
#                                  filters=[not_stopword],
#                                  transforms=[convert_to_lowercase, remove_trailing_punct])
def create_easy_documents(list_of_docs, true_class, filters=None, transforms=None) :
    document_list = []
    for item in list_of_docs :
        d = Document(true_class=true_class)
        words = item
        ## deal with filters here
        for f in filters:
            words = [word for word in words if f(word)]

        ## deal with transforms here
        cleaned_words = []
        for word in words:
            for transformer in transforms:
                word = transformer(word)
            cleaned_words.append(word)
        d.add_tokens(cleaned_words)
        document_list.append(d)
    return document_list

## filters - return true if the token meets the criterion

def not_stopword(token) :
    return token not in ['a', 'an', 'the']

def not_cat(token) :
    return token != 'cat'

# transforms - convert a token into a new format

# you do this.
def remove_trailing_punct(token) :
    return token.rstrip(string.punctuation)

# and this
def convert_to_lowercase(token) :
    return token.lower()



## homogeneity: for each cluster, what fraction of the cluster is comprised of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_homogeneity(result, ['pos','neg'])
def compute_homogeneity(list_of_clusters, list_of_classes):
    # hlist will be the homogeneity for each cluster.
    hlist = []

    for cluster in list_of_clusters :
        class_ratio = defaultdict(lambda: 0.0)
        for doc in cluster.members :
            if doc.true_class in list_of_classes :
                class_ratio[doc.true_class] += 1.0
        sorted_class = sorted(class_ratio.items(), key=operator.itemgetter(1), reverse=True)
        hlist.append(class_ratio[sorted_class[0][0]] / len(cluster.members))
    return hlist


## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])
def compute_completeness(list_of_clusters, list_of_classes):
    clist = []

    for _class in list_of_classes:
        class_docs = [doc for cluster in list_of_clusters for doc in cluster.members if doc.true_class == _class]
        class_count = len(class_docs)

        if class_count > 0:
            max_cluster_count = max(
                len([doc for doc in cluster.members if doc.true_class == _class]) for cluster in list_of_clusters)
            completeness = max_cluster_count / class_count
        else:
            completeness = 0

        clist.append(completeness)
    return clist

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_docs(10,10)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                 filters=[],
                                 transforms=[])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                    filters=[],
                                 transforms=[])





