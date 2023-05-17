import matplotlib.pyplot as plt
import numpy as np
x_data = [5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
y_data = [4.2, 5, 5.2, 5.9, 6, 6.2, 6.1, 6.9, 7.2, 8, 8.3, 7.4, 8.4, 7.8, 8.5, 9.5]
x_data2 = []
y_data2 = []
#plt.xlim([0, 30])
#plt.ylim([0, 20])
#plt.scatter(x = x_data, y = y_data)
x_array = np.array(x_data)
y_array = np.array(y_data)
coefficient = np.corrcoef(x_array, y_array)
print(coefficient)
for x in x_data:
    x *= 2
    x_data2.append(x)
for y in y_data:
    y *= 2
    y_data2.append(y)
print(x_data2)
print(y_data2)
#plt.scatter(x = x_data2, y = y_data2)
x_array2 = np.array(x_data2)
y_array2 = np.array(y_data2)
coefficient2 = np.corrcoef(x_array2, y_array2)
print(coefficient2)
lyme_disease = [3, 2, 2, 4, 5, 15, 22, 13, 6, 5, 4, 1]
drowning_deaths = [0, 1, 2, 1, 2, 9, 16, 5, 3, 3, 1, 0]
#plt.scatter(x = lyme_disease, y = drowning_deaths)
lyme_array = np.array(lyme_disease)
drowning_array = np.array(drowning_deaths)
coefficient3 = np.corrcoef(lyme_array, drowning_array)
print(coefficient3)
iq = [133, 137, 138, 132, 140, 132, 135, 130, 133, 133, 140, 140, 139, 133, 133, 141, 135, 139, 141, 144]
mri_count = [816932, 951545, 991305, 833868, 856472, 852244, 790619, 866662, 857782, 948066, 949395, 1001121, 1038437, 965353, 955466, 1079549, 924059, 955003, 935494, 949589]
male_mri = [949395, 1001121, 1038437, 965353, 955466, 1079549, 924059, 955003, 935494, 949589]
male_iq = [140, 140, 139, 133, 133, 141, 135, 139, 141, 144]
female_mri = [816932, 951545, 991305, 833868, 856472, 852244, 790619, 866662, 857782, 948066]
female_iq = [133, 137, 138, 132, 140, 132, 135, 130, 133, 133]
#plt.scatter(x = male_mri, y = male_iq)
#plt.scatter(x = female_mri, y = female_iq)
iq_array = np.array(iq)
mri_array = np.array(mri_count)
coefficient4 = np.corrcoef(mri_array, iq_array)
print(coefficient4)
male_iq_array = np.array(male_iq)
male_mri_array = np.array(male_mri)
female_iq_array = np.array(female_iq)
female_mri_array = np.array(female_mri)
male_coefficient = np.corrcoef(male_mri_array, male_iq_array)
female_coefficient = np.corrcoef(female_mri_array, female_iq_array)
print(male_coefficient)
print(female_coefficient)
male_drivers = [12, 6424, 6941, 18068, 20406, 19898, 14340, 8194, 4803]
male_crashes = [227, 5180, 5016, 8595, 7990, 7119, 4527, 2274, 2022]
female_drivers = [12, 6139, 6819, 17664, 20063, 19984, 14441, 8400, 5375]
female_crashes = [77, 2113, 1531, 2780, 2742, 2285, 1514, 938, 980]
plt.scatter(x = male_drivers, y = male_crashes)
plt.scatter(x = female_drivers, y = female_crashes)
male_drivers_array = np.array(male_drivers)
male_crashes_array = np.array(male_crashes)
female_drivers_array = np.array(female_drivers)
female_crashes_array = np.array(female_crashes)
male_coefficient2 = np.corrcoef(male_drivers_array, male_crashes_array)
female_coefficient2 = np.corrcoef(female_drivers_array, female_crashes_array)
print(male_coefficient2)
print(female_coefficient2)