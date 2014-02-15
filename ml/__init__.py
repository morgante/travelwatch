# that should get the analyze function
import predict
import make_model
import train

#make the model
cities=make_model.model_from_all()
mname=train.make_model(cities)

#load model
mod=predict.load(mname)

##data format: 
#data=[datum1,datum2,..]
#datum:=[w1,w2,w3,...,cNum]
def predict(newData):
    return predict.analyze(mod,newData)



