import pickle
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from preprocess import preprocess_data


df = preprocess_data()

print(df.head())

X = df.drop('result', axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

trf = ColumnTransformer([
    (
        'trf',
        OneHotEncoder(sparse_output=False, drop='first'),
        ['batting_team', 'bowling_team', 'city']
    )
], remainder='passthrough')

pipe = Pipeline([
    ('step1', trf),
    ('step2', LogisticRegression(solver='liblinear'))
])

pipe.fit(X_train, y_train)

pickle.dump(pipe, open('../models/model.pkl', 'wb'))

print("Model saved successfully")
