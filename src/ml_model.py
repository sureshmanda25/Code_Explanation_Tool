from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

class CodeExplanationModel:
    def __init__(self):
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save_model(self, filepath):
        joblib.dump(self.model, filepath)

    @classmethod
    def load_model(cls, filepath):
        instance = cls()
        instance.model = joblib.load(filepath)
        return instance