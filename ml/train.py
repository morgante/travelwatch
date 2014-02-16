import numpy as np
from sklearn.externals import joblib
#import listofWords
# import listWords as listofWords

def train(features,outputs,mode=1):

    print 'TRAIN'
	
    if mode==1:
        from sklearn import linear_model
	name="lin_regression"
        model = linear_model.LinearRegression()
    elif mode==2:
        from sklearn import svm
	name="svm"
	model = svm.SVC()
    print name

    print features
    print outputs

    train_ft = features[:-1]
    train_out = outputs[:-1]
    test_ft = features[-1:]
    test_out = outputs[-1:]
    
    model.fit(train_ft, train_out)

    # make prediction on test data
    filename = 'ml/model/'+name+'.pkl'
    joblib.dump(model, filename)

    print('Saved model to ' + filename)
    return name

# def make_model(cities,mode=1):
#     data = []
#     words = listofWords.listofWords()
    
    
#     #generating articles data array 
#     for city in cities.keys():
#         print city
#         #datum:=[w1,w2,w3,...,cNum] 
# 	datum = []
#         for word in words:
#             if (word in cities[city].keys()):
#                 datum.append(cities[city][word])
#             else:
#                 datum.append(0)
# 	datum.append(cities[city]["c_Num"])
#         data.append(datum)

#     data=np.array(data)
#     # training the data and generating the model
#     return train(data, mode)


