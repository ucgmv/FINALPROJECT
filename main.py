# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import scipy.io as sc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import openpyxl as op

### import all the libraries

a = pd.read_excel(r'2010+Census+Population+By+Zipcode+(ZCTA).xlsx')
#b = pd.read_excel(r"BACM Annex A.xlsx")
c = pd.read_excel(r"BACM Disposed.xlsx", skiprows = 1, usecols="B:AK")
#d = pd.read_excel(r"CS Annex A.xlsx")
e = pd.read_excel(r"CS Disposed.xlsx", skiprows = 1, usecols="B:AK")
#f = pd.read_excel(r"JPM Annex A(1).xlsx")
g = pd.read_excel(r"JPM Disposed.xlsx", skiprows = 1, usecols="B:AK")
#h = pd.read_excel(r"ML Annex A.xlsx")
i = pd.read_excel(r"ML Disposed.xlsx", skiprows = 1, usecols="B:AK")
#j = pd.read_excel(r"SBM Annex A.xlsx")
k = pd.read_excel(r"SBM Disposed.xlsx", skiprows = 1, usecols="B:AK")
### Read excels


lossaux = np.array(sc.loadmat('LOSS.mat')['LOSS'])
payaux = np.array(sc.loadmat('PAY.mat')['PAY'])

                  
loss = pd.DataFrame(lossaux)
loss.insert(len(loss.columns), 'Loss', 1)
pay = pd.DataFrame(payaux, index =range(969,4793))
pay.insert(len(pay.columns), 'Loss', 0)
columns = ['NOI','DSCR','LTV','Balance','Rate','Fee','Net Mortgage Rate','Year Built','Renovation','Occupancy','ZipPop','CR','CS','CS Ratio','NOI Ratio','PV Ratio','IR', 'Loss']
frame = [loss, pay]
dataset = pd.concat(frame)
dataset.columns = columns
print(dataset)

corr = dataset.corr()
ax = sns.heatmap(corr, linewidth=0.5)
plt.show()

### Read Matlab files
