import numpy as np
from sklearn.externals import joblib

def train(data,mode=1):
    features = data[:, 1:-1]
    outputs = data[:, -1].astype(np.int)

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

if __name__ == "__main__":
    data = np.loadtxt(open("train.csv","rb"),delimiter=",",skiprows=0)
    train(data,1)
    train(data,2)

