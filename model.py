# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:49:59 2019

@author: rahul
"""
#Importing libraries
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score


#Importing preprocessing file 
from preprocessfinale11 import preprocessing
x_train,x_test,y_train,y_test=preprocessing()        

#MODEL Training and Testing
print("...training model...")        
classifier1=RandomForestClassifier(n_jobs=-1)
classifier1.fit(x_train,y_train)
y_pred=classifier1.predict(x_test)
    
#Saving the model(Pickle File)
filename = 'RF_model.sav'
pickle.dump(classifier1, open(filename, 'wb'))

#Train-Validation-Test
accuracies=cross_val_score(estimator=classifier1,X=x_train,y=y_train,cv=10) 

#INSIGHTS & INFERENCES
print("Accuracy of the model: ",metrics.accuracy_score(y_test, y_pred))
print("Mean Accuracy: ",accuracies.mean())
print("Standard Deviation: ",accuracies.std())


#Confusion matrix

print(metrics.confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1)))
        
        
















