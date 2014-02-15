import numpy as np
from sklearn.externals import joblib
import listWords as listofWords

def train(data,mode=1):
    features = data[:,:-1]
    outputs = data[:,-1]
	
    if mode==1:
        from sklearn import linear_model
	name="lin_regression"
        model = linear_model.LinearRegression()
    elif mode==2:
        from sklearn import svm
	name="svm"
	model = svm.SVC()
    print name

    train_ft = features[:-5]
    train_out = outputs[:-5]
    test_ft = features[-5:]
    test_out = outputs[-5:]
    
    model.fit(train_ft, train_out)
    


    # make prediction on test data
    filename = 'model/'+name+'.pkl'
    joblib.dump(model, filename)

    print('Saved model to ' + filename)
    return name

def make_model(cities,mode=1):
    data = []
    words = listofWords.listofWords()
    
    
    #generating articles data array 
    for city in cities.keys():
        #datum:=[w1,w2,w3,...,cNum] 
	datum = []
        for word in words:
            if (word in city.keys()):
                datum.append(city[word])
            else:
                datum.append(0)
	datum.append(city["c_Num"])
        data.append(datum)

    data=np.array(data)
    # training the data and generating the model
    return train(data, mode)


