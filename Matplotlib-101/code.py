# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here

data =pd.read_csv(path)
#print(data)
loan_status = data['Loan_Status'].value_counts()
#print(loan_status)

plt.figure(figsize=[14,8])
plt.xlabel("Type 2 Pokemon Variants")
plt.ylabel("No of Pokemons")


plt.bar(loan_status.index,loan_status)



# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status'])
print(property_and_loan)
property_and_loan = property_and_loan.size().unstack();
print(property_and_loan)


# --------------
#Code starts here

education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()


# --------------
#Code starts here


graduate = data[data['Education'] == 'Graduate']

not_graduate = data[data['Education'] == 'Not Graduate']


graduate.plot(kind='density',label='Graduate' )





#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(3,1, figsize=(30,10))


data.plot.scatter(x='ApplicantIncome', y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome', y='LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome']+ data['CoapplicantIncome']

data.plot.scatter(x='TotalIncome', y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')



