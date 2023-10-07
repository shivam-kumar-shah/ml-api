import pickle
from os.path import join

from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

raw_data = read_csv(join("app", "models", "heart_disease", "heart_disease.csv"))

data = raw_data.drop(["target"], axis=1)
target_col = raw_data["target"]

x_train, x_test, y_train, y_test = train_test_split(
    data,
    target_col,
    test_size=0.2,
    stratify=target_col,
    random_state=2,
)

ml_model = LogisticRegression(max_iter=1000)
ml_model.fit(x_train, y_train)

# Pickle export
pkl_filename = join("app", "models", "heart_disease", "heart_disease.pkl")
with open(pkl_filename, "wb") as file:
    pickle.dump(ml_model, file)
