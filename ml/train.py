import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib

data = np.loadtxt(open("train.csv","rb"),delimiter=",",skiprows=0)

features = data[:, 1:-1]
outputs = data[:, -1].astype(np.int)

print features
print outputs

# clf = ExtraTreesClassifier(n_estimators=100).fit(features[:1], outputs[:1])

model = linear_model.LinearRegression()

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
