import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib

# toPredict should be loaded from the .csv file then passed here
# returns the prediction list, we probably want to take the hightest predicted word
def load(modelName):
    return joblib.load("model/%s"%modelName) 

def get_alert_data_for_country(country):
	return {
		"level": level
		"keywords": {
			"murder": 10,
		}
	}

def analyze(lm,newData):
   
   predicted = lm.predict(newData)
 
   print ("Predicted")
   print (predicted)

   return predicted

