# that should get the analyze function
import predict as prediction
import make_model
import train

# #load model
#model = predict.load("lin_regression")

def predict(data):
	return prediction.analyze(model, data)
