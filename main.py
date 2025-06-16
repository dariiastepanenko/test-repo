from cat_classifier.model import predict
from cat_classifier.data_loader import load_data

if __name__ == "__main__":
    data = load_data()
    result = predict(data)
    print(f"Prediction: {result}")
