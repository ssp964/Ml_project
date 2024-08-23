import numpy as np
import pandas as pd
import os
import sys
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.logger import logging
from src.exception import CustomException

def save_object(file_path, obj):
    '''
    Saves results into a pickle file
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved successfully at {file_path}")
    except Exception as e:
        logging.error(f"Failed to save object at {file_path}: {str(e)}")
        CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    '''
    evaluates models using grid search
    '''
    try:
        report = {} # to store the test R² scores for each model

        for i in range(len(list(models))):
            model = list(models.values())[i] # retrieves the model instance
            para=param[list(models.keys())[i]] # retrieves the corresponding hyperparameters for GridSearchCV

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
