from unittest import TestCase
from Loader import *


class Test(TestCase):
    def test_apply_filters(self):
        self.assertTrue(not_cat("bat"))
        self.assertFalse(not_cat("cat"))
        self.assertFalse(not_stopword("a"))
        self.assertFalse(not_stopword("an"))
        self.assertFalse(not_stopword("the"))
        self.assertTrue(not_stopword("and"))

    def test_apply_transforms(self):
        self.assertEquals(remove_trailing_punct("hello!"), "hello")
        self.assertEquals(remove_trailing_punct("hello"), "hello")
        self.assertEquals(convert_to_lowercase("HELLO"), "hello")
        self.assertEquals(convert_to_lowercase("Hello"), "hello")
        self.assertEquals(convert_to_lowercase("hello"), "hello")

    def test_workflow(self):
        pos_reviews, neg_reviews = create_docs(10, 10)

        positive_docs = create_easy_documents(pos_reviews, 'pos',
                                              filters=[],
                                              transforms=[])

        negative_docs = create_easy_documents(neg_reviews, 'neg',
                                              filters=[],
                                              transforms=[])



