from unittest import TestCase
from Cluster import *
from Document import *

class TestCluster(TestCase):
    def test_calculate_centroid(self):
       # Creates a new Document
        # each tokens are all its members with the count averaged
        doc = Document()
        tokens = defaultdict(int)
        self.assertTrue(True, True)



    def test_kmeans(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        print(k_means(2, ['pos', 'neg'], [d,d2,d3]))


