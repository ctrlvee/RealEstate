import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,
        'Python':35}
courses = ['C','C++','Java','Python']
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()