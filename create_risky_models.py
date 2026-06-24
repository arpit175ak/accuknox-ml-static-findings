import pickle
import os

class MaliciousPickle:
    def __reduce__(self):
        return (os.system, ("echo accuknox-ml-static-scan-test",))

class CustomModel:
    def __init__(self):
        self.model_name = "unsafe-custom-model"
        self.secret = "fake_secret_for_static_scan"
        self.exec_code = "os.system('whoami')"

class LambdaLikeModel:
    def __init__(self):
        self.preprocess = lambda x: x
        self.description = "model containing lambda object"

payloads = {
    "models/pickle-risk/malicious_reduce.pkl": MaliciousPickle(),
    "models/pickle-risk/custom_model.pkl": CustomModel(),
    "models/pickle-risk/lambda_like_model.pkl": LambdaLikeModel(),
    "models/checkpoints/model_checkpoint.ckpt": MaliciousPickle(),
    "models/checkpoints/training_state.pkl": CustomModel(),
    "models/unsafe_model.pickle": MaliciousPickle(),
}

for path, obj in payloads.items():
    try:
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        print("created", path)
    except Exception as e:
        print("failed", path, e)
