from pandas import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold, RepeatedStratifiedKFold

def make_model():
    train = pd.read_csv('clean_train.csv')

    features = train[['Age','Is_female','Pclass','emb_C','emb_Q',
                    'emb_S','Family_size', 'Mr', 'Mrs', 'Master', 'Miss']]

    target = train.Survived

    features_train, features_test, target_train, target_test = \
        train_test_split(features, target, test_size=0.2, random_state=0)

    model = RandomForestClassifier()
    return model

def model_score(model):
    return cross_val_score(model, features, target, cv=RepeatedStratifiedKFold()).mean()

def test_model(model, Age, Is_female, Pclass, emb_C, emb_Q, emb_S, Family_size, Mr, Mrs, Master, Miss):
    d = {
        'Age': [Age],
        'Is_female': [Is_female], 
        'Pclass': [Pclass], 
        'emb_C': [emb_C],
        'emb_Q': [emb_Q],
        'emb_S': [emb_S],
        'Family_size': [Family_size], 
        'Mr': [Mr], 
        'Mrs': [Mrs], 
        'Master': [Master], 
        'Miss': [Miss]
    }
    test = pd.DataFrame(data=d)

    prob_survived = model.predict_proba(test_features)[0][1]
    return prob_survived