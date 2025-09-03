import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

def extract_features(processes):
    return np.array([[p.arrival_time, p.burst_time, p.priority] for p in processes]).flatten()

def train_ml_algo(X, y):
    clf = RandomForestClassifier()
    clf.fit(X, y)
    with open('ml_model.pkl', 'wb') as f:
        pickle.dump(clf, f)

def predict_algorithm(processes):
    with open('ml_model.pkl', 'rb') as f:
        clf = pickle.load(f)
    features = extract_features(processes).reshape(1, -1)
    return clf.predict(features)
