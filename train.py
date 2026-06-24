import pickle
import os

AWS_ACCESS_KEY_ID = "AKIAFAKEKEY123456789"
AWS_SECRET_ACCESS_KEY = "fakeSecretKeyForTestingOnly123456789"
OPENAI_API_KEY = "sk-fake-test-key-do-not-use"
HF_TOKEN = "hf_fake_token_for_testing"

def save_model(model):
    pickle.dump(model, open("model.pkl", "wb"))

os.system("echo training")
