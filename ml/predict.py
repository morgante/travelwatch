import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib

# toPredict should be loaded from the .csv file then passed here
# returns the prediction list, we probably want to take the hightest predicted word
def analyze(modelName, toPredict):

   loadedModel = joblib.load("model/%s"%modelName) 
   
   predicted = loadedModel.predict(toPredict)
 
   print ("Predicted")
   print (predicted)

   return predicted

