#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
accuracy_per_file = []
for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #Reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    age_map = {'Young': 1, 'Prepresbyopic': 2, 'Presbyopic': 3}
    spectacle_map = {'Myope': 1, 'Hypermetrope': 2}
    astig_map = {'Yes': 1, 'No': 2}
    tear_map = {'Reduced': 1, 'Normal': 2}
    class_map = {'Yes': 1, 'No': 2}

    #Transform the original categorical training features to numbers and add to the 4D array X.
    #For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for row in dbTraining:
        X.append(
            [age_map.get(row[0]),
            spectacle_map.get(row[1]),
            astig_map.get(row[2]),
            tear_map.get(row[3])])
        #Transform the original categorical training classes to numbers and add to the vector Y.
    #For instance Yes = 1 and No = 2, Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
        Y.append(class_map.get(row[4]))
    #Loop your training and test tasks 10 times here


    accuracy_per_test = []
    for i in range (10):
       truePos = 0;
       falsePos = 0;

       trueNeg = 0;
       falseNeg = 0;
       #Fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=5)
       clf = clf.fit(X, Y)

       #Read the test data and add this data to dbTest
       #--> add your Python code here

       with open('contact_lens_test.csv', 'r') as csvfile:
           dbTest = []
           reader = csv.reader(csvfile)
           for j, row in enumerate(reader):
               if j > 0:  # Skipping the header
                   dbTest.append(row)

       for data in dbTest:
               accuracy = 0;
               test = [age_map.get(data[0]),
               spectacle_map.get(data[1]),
               astig_map.get(data[2]),
               tear_map.get(data[3])]

               prediction = clf.predict([test])[0]

               true_class = class_map.get(data[4])

               if(true_class == prediction and true_class == 1):
                   truePos += 1
               elif(true_class == prediction and true_class == 0):
                   trueNeg += 1
               elif(true_class != prediction and true_class == 0):
                   falsePos += 1
               else:
                   falseNeg += 1
       accuracy =  (truePos+ trueNeg) / (truePos + falsePos+falseNeg+trueNeg)
       accuracy_per_test.append(accuracy)
       print("Test "+str(i)+" Accuracy: "+str(accuracy))
           #Transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
    avg_acc = 0;
    for i in accuracy_per_test:
        avg_acc+= i/len(accuracy_per_test)

    print("Overall Accuracy for current training file: " + str(avg_acc))
           #Compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here

    #Find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #Print the average accuracy of this model during the 10 runs (training and test set).
    #Your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here




