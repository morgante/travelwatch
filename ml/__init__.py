# that should get the analyze function
import predict
import make_model

#make the model
mname=make_model.main()
#load model
mod=predict.load(mname)


def predict(newData):
    return predict.analyze(mod,newData)



