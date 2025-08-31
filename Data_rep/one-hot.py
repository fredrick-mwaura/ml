# label encoding

from sklearn.preprocessing import LabelEncoder, oneHotEncoder
import numpy as np

# ordinal
streets = ["Murang'a", "Nakuru", " Naivasha", "Mombasa", "Kisumu", "Nairobi"]
le = LabelEncoder()
streets_encoded = le.fit_transform(streets)
print(streets_encoded)

#oneHot encoding
streets_one = np.zeros((len(streets), len(le.classes_)))

for i, street in enumerate(streets):
    index = le.transform([street])[0]
    streets_one[i, index] = 1
print(streets_one)

"""
using oneHotEncoder
"""

streets_array = np.array(streets).reshape(-1, 1)

encoder = oneHotEncoder(sparse=False)
streets_one_hot = encoder.fit_transform(streets_array)
print(streets_one_hot)