import scipy
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.svm import SVR

data = np.genfromtxt('FYPpreprocessed11mar.csv', delimiter=',')

trainingdata = data[0:2000,]
valdata = data[2000:2500,]
testdata = data[2500:3000,]
trainlen = 2000
#starting base line model

blprediction = [np.mean(trainingdata[:,1])]*valdata.shape[0]

plt.figure(1)#,figsize=(10, 20))
#sp1 = plt.subplot(411)
plt.plot(valdata[:,1],blprediction,'o')
#sp1.set_xlabel('Actual Value')
#sp1.set_ylabel('Predicted Value')
#sp1.set_title('Base line Model')
plt.show()

blerror = np.sqrt(np.mean(np.square(valdata[:,1]-blprediction)))
print "bl corr " , np.correlate(valdata[:,1],blprediction)
print "bl error " , blerror


#end of base line model

#start linear regression

lm = linear_model.LinearRegression()

lm.fit(trainingdata[:,0].reshape(trainlen,1),trainingdata[:,1].reshape(trainlen,1))
lmprediction = lm.predict(valdata[:,0].reshape(500,1))

lmerror = np.sqrt(np.mean(np.square(valdata[:,1]-lmprediction)))
#print "lm corr " , np.correlate(valdata[:,1],lmprediction)
print lmerror
#sp1 = plt.subplot(412)
plt.plot(valdata[:,1],lmprediction,'o')
#sp1.set_xlabel('Actual Value')
#sp1.set_ylabel('Predicted Value')
#sp1.set_title('Linear Regression Model')
plt.show()


#end linear regression


#start svmr

svrmodel = SVR(C=1.0, epsilon=0.02)

svrmodel.fit(trainingdata[:,0].reshape(trainlen,1),trainingdata[:,1].reshape(trainlen,1))

svrprediction = svrmodel.predict(valdata[:,0].reshape(500,1))

svrerror = np.sqrt(np.mean(np.square(valdata[:,1]-svrprediction)))

print "svr error" , svrerror
#sp1 = plt.subplot(413)
plt.plot(valdata[:,1],svrprediction,'o')
#sp1.set_xlabel('Actual Value')
#sp1.set_ylabel('Predicted Value')
#sp1.set_title('Support Vector Machine Model')
plt.savefig('testgraph.png')

#sp1 = plt.subplot(414)
#plt.plot(valdata[:,1],valdata[:,1],'o')
#sp1.set_xlabel('Actual Value')
#sp1.set_ylabel('Predicted Value')
#sp1.set_title('Ideal Model (100% accurate)')
#plt.savefig('testgraph.png')

plt.show()

plt.plot(valdata[:,1],valdata[:,1],'o')
plt.show()

print "svr corr " , np.correlate(valdata[:,1],svrprediction)

#end svmr
