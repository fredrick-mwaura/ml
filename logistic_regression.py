import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataset import dataset
import io


z = 2.0
prob = 1/(1 + np.exp(-z))

# print(prob)

"""
up next - DATA
"""

pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format # print floating points to  1dp

training_df = pd.read_csv('https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv')

#Return a statistically description of the data in the dataframe
"""
count, mean, std, min, 25%, 50%, 75%, max"""
training_df.describe()

def plot_the_dataset(feature, label, number_of_points_to_plot):
  """
  plot n random points in a dataset
  """
  
  plt.xlabel(feature)
  plt.ylabel(label)
  
  random_ex = training_df.sample(n=number_of_points_to_plot)
  plt.scatter(random_ex[feature], random_ex[label])
  plt.show()
  
  print("define the following function to plot the dataset")

# plot_the_dataset('median_income', 'median_house_value', 100) # creating scatter points

#reading the dataset.py as csv
training_df = pd.read_csv(io.StringIO(dataset), on_bad_lines='warn')
training_df.describe()
print(training_df.head())

def plot_a_contiguous_portion_of_dataset(feature, label, start, end):
  #labeling axes
  plt.xlabel(feature + "Day")
  plt.ylabel(label)
  
  plt.scatter(training_df[feature][start:end], training_df[label][start:end])
  plt.show()
  
##visualizing by Day
for i in range(0, 7):
  start = i * 50
  end = start + 49
  print("\nDay %d" % i)
  plot_a_contiguous_portion_of_dataset("calories", "test_score", start, end)
  
  
# confirming the suspicions

thursday_calories = 0
non_thursday_calories = 0
count = 0
for week in range(0, 4):
  for day in range(0, 7):
    for subject in range(0, 50):
      position = (week * 350) + (day * 50) + subject
      if (day == 4):
        thursday_calories += training_df['calories'][position]
      else:
        count += 1
        non_thursday_calories += training_df['calories'][position]

mean_thursday_calories = thursday_calories / 200
mean_non_thursday_calories = non_thursday_calories / 200
print("Mean calories on Thursday: %.2f" % mean_thursday_calories)
print("Mean calories on non-Thursday: %.2f" % mean_non_thursday_calories)