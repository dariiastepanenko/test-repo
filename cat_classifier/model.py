def predict(data):
    print("Running fake model prediction...")
    return "cat" if "cat" in data["image"] else "not a cat"
