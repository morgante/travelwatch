import numpy as np
from sklearn.externals import joblib

def listofWords():
   lst = ["crime", "abuse", "forgery", "kidnapping", "murder", "prostitution", "theft", "trespass", "danger", "federal", "kill", "warning", "death", "attack", "arrest"]
   return lst

def train(data,mode=1):
    features = data[:,1:]
    outputs = data[:,0]
	
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

def make_model(cities):
    data = []
    words = listofWords()
    
    
    #generating articles data array 
    for city in cities.keys():
        #datum:=[city,w1,w2,w3,...] 
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
    train(data, 1)


if __name__ == "__main__":
    articles = [{"keywords": {"murder": 10, "kidnapping": 2}},{"keywords":{"kill": 5, "federal": 2}}, {"keywords": {"murder": 10, "kidnapping": 2}},{"keywords": {"murder": 10, "kidnapping": 2}},{"keywords": {"murder": 10, "kidnapping": 2}},{"keywords": {"murder": 10, "kidnapping": 2}},{"keywords": {"murder": 10, "kidnapping": 2}},{"keywords": {"murder": 10, "kidnapping": 2}},{"keywords": {"murder": 10, "kidnapping": 2}},{"keywords": {"murder": 10, "kidnapping": 2}}]

    #corresponding crime rates
    cRate = [3, 7, 3,3,3,3,3,3,3,3]

    make_model(articles, cRate)


