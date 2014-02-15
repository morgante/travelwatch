import numpy as np
from sklearn.externals import joblib

def train(data,mode=1):
    features = data[:, 1:-1]
    outputs = data[:, -1].astype(np.int)

    if mode==1:
        from sklearn import linear_model
	print "linear regression"
        model = linear_model.LinearRegression()
    elif mode==2:
        from sklearn import svm
	print "svm"
	model = svm.SVC()

    train_ft = features[:-5]
    train_out = outputs[:-5]
    test_ft = features[-5:]
    test_out = outputs[-5:]
    
    model.fit(train_ft, train_out)
    
    print('Variance score: %.2f' % model.score(test_ft, test_out))

    # make prediction on test data
    print('Prediction:')
    print(model.predict(test_ft))

    print('Actual:')
    print test_out

    # Save to disk
    filename = 'model/store.pkl'
    joblib.dump(model, filename)

    print('Saved model to ' + filename)

if __name__ == "__main__":
    data = np.loadtxt(open("train.csv","rb"),delimiter=",",skiprows=0)
    train(data,1)
    train(data,2)

