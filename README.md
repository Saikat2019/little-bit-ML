# little-bit ML
first creat a virtualenv by the command- virtualenv nameOfFolder
then install the requirements
if you are getting error in 'pip install scipy' like error[13]:permission denied
then try with 'pip install scipy --user'
 there is no module named cross_validation in scikit-learn 0.20.1 so cross_validation.train_test_split() can't be used... instead use sklearn.model_selection import train_test_split
