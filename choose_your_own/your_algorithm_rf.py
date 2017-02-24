#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import RandomForestClassifier
from time import time

'''
# 1000 best at ~0.9192
for n in [1, 10, 50, 100, 500, 1000]:
    sum = 0
    for x in range(0, 10):
        clf = RandomForestClassifier(n_estimators=n)
        clf.fit(features_train, labels_train)
        sum += clf.score(features_test, labels_test)
    print "RandomForest n:", str(n), ", accuracy:", str(sum / 10)
'''
'''
# 10 best at ~0.92
for mss in [2, 3, 5, 7, 10]:
    sum = 0
    for x in range(0, 10):
        clf = RandomForestClassifier(n_estimators=1000, min_samples_split=mss)
        clf.fit(features_train, labels_train)
        sum += clf.score(features_test, labels_test)
    print "RandomForest n: 1000, min sample split:", str(mss), ", accuracy:", str(sum / 10)
'''

# Very random results (of course), 1000 & 10 probably isn't better than default

clf = RandomForestClassifier(n_estimators=1000, min_samples_split=10)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s" #~2.0s

t1 = time()
clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s" #~0.45s

print "accuracy:", clf.score(features_test, labels_test) #.92


try:
    prettyPicture(clf, features_test, labels_test)
    plt.show()
except NameError:
    pass
