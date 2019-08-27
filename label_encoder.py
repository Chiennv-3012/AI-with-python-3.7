import numpy as np
from sklearn import preprocessing

#sample input labels
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

#create label encoder and fit labels
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

#Print the mapping
print("\nLabel mapping: ")
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)

#Encode a set of labels using the encoder
test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)
print ("Endcoded values =", list(encoded_values))

#Decode a set of values using the coder
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("\nDecoded labels =", list(decoded_list))sk


