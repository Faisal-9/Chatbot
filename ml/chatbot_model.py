import sys
import pickle
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(script_dir, 'chatbot_model.pkl')

# Loading the trained model and vectorizer
with open(model_path, 'rb') as f:
    model, vectorizer = pickle.load(f)

# Prediction 
user_input = sys.argv[1]
X = vectorizer.transform([user_input])
prediction = model.predict(X)

print(prediction[0], flush=True)
