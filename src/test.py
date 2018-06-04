import nibabel as nib


# Open file and extract data
("../files/OAS30001_MR_d0129/anat4/test.nii")


# Preprocess data for sklearn


# Split dataset into testing and training

#random ML algorithms provided by sk learn and code, most likely not going to use this below,
#but it does kinda help to see how it should/sorta work.


names = ["Nearest Neighbors", "Linear SVM", "RBF SVM",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes"]

classifiers = [
    KNeighborsClassifier(8, weights='distance'),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=0.0001, C=1),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB()]

bin_classifiers = [
    KNeighborsClassifier(41, weights='distance'),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=0.0001, C=1),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB()]

results = []

for i in range(len(classifiers)):
	print(names[i])
	results.append(train_and_test(classifiers[i]))
	bin_train_and_test(bin_classifiers[i])
	print()

for i in range(len(names)):
	print(names[i], results[i])

plt.bar(names, results)
plt.ylim((0, 100))
plt.xlabel("ML Algorithm")
plt.ylabel("Accuracy")
plt.title("ML Algorithm Accuracy")

for i,j in zip(np.arange(len(names)), results):
    plt.annotate("{:4.2f}%".format(j), xy=(i-0.3,j))

plt.show()