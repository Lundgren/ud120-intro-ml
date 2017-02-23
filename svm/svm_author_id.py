#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

#clf = svm.SVC(kernel='linear')
'''
for c in [10.0, 100.0, 1000.0, 10000.0]:
    print "kernel: rbf, C:", str(c)
    clf = svm.SVC(kernel='rbf', C=c)

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t1 = time()
    clf.predict(features_test)
    print "prediction time:", round(time()-t1, 3), "s"

    print "accuracy:", clf.score(features_test, labels_test)
'''

clf = svm.SVC(kernel='rbf', C=10000.0)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s" #~80s

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s" #~8s

print "accuracy:", clf.score(features_test, labels_test) #.990

print "mail #10 sent by", pred[10]
print "mail #26 sent by", pred[26]
print "mail #50 sent by", pred[50]

print "mail from Chris predicted in", (pred == 1).sum(), "cases"
#########################################################


