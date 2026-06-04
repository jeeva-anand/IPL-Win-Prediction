import pickle

model = pickle.load(open('models/pipe.pkl', 'rb'))


def predict_probability(input_df):

    result = model.predict_proba(input_df)

    return result
