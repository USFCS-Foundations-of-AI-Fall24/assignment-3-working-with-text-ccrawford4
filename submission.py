from Classifier import run_classifier
from Loader import compute_homogeneity, compute_completeness, create_easy_documents, not_stopword, \
    remove_trailing_punct, convert_to_lowercase
from make_dataset import create_docs
from pandasExercise import run_pandas
from plot import plot_k_means
from test_Cluster import populate_documents
from Cluster import k_means


def main() :
    print("----------Pandas Exercise----------")
    run_pandas()
    print("-----------Documents--------------")
    pos_docs, neg_docs = create_docs(5, 5, use_random=True, length=100)
    documents = []
    print("Testing with 5 pos docs and 5 neg docs containing 100 words each")
    populate_documents(pos_docs, 'pos', documents)
    populate_documents(neg_docs, 'neg', documents)
    cluster_list = k_means(2, ['pos', 'neg'], documents)
    print("Cluster homogeneity: ", compute_homogeneity(cluster_list, ['pos', 'neg']))
    print("Cluster completeness: ", compute_completeness(cluster_list, ['pos', 'neg']))
    print("-------Plotting K-Means Accuracy Across Cluster Sizes----")
    plot_k_means()
    print("-----Filters and Transformers------")
    pos_reviews, neg_reviews = create_docs(10, 10, use_random=True, length=25)
    print("Pos Reviews before cleaning: ", [word for group in pos_reviews for word in group])
    print("Neg Reviews before cleaning: ", [word for group in neg_reviews for word in group])
    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                          filters=[not_stopword],
                                          transforms=[remove_trailing_punct, convert_to_lowercase])

    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                          filters=[not_stopword],
                                          transforms=[remove_trailing_punct, convert_to_lowercase])

    print("Positive Docs after cleaning: ", [w for doc in positive_docs for w in doc.tokens])
    print("Negative Docs after cleaning: ", [w for doc in negative_docs for w in doc.tokens])
    print("-------Classifier--------")
    run_classifier()
    return

if __name__ == "__main__" :
    main()