from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        r1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(r1['label'],  "SENT_POSITIVE")

        r2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(r2['label'],  "SENT_NEGATIVE")

        r3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(r3['label'],  "SENT_NEUTRAL")

unittest.main()