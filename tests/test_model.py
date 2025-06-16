from cat_classifier.model import predict

def test_predict_cat():
    data = {"image": "this_is_a_cat"}
    assert predict(data) == "cat"

def test_predict_not_cat():
    data = {"image": "this_is_a_dog"}
    assert predict(data) == "not a cat"
