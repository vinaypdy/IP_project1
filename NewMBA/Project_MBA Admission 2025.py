'''
This project is....................
...................................
...................................
application_id
gender
international
gpa
major
race
gmat
work_exp
work_industry
admission

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    print('Reading csv file')
    print('----------------')
    '''..................Important copy following file:  IN_youtube_trending_data_New.csv 
    in the csnip folder of your compurer to run the project successfully............. '''
    df=pd.read_csv('MBA.csv')
except:
    print('Something went wrong')
    
while True:
    print('======================================================')
    print('1 for displayiny first 5 rows')
    print('2 for displaying last 5 rows')
    print('3 for displaying all the columns of csv file')
    print('4 for displaying information of gender,international,race,work_exp')
    print('5 for Statistical Analysis')
    print('6 for displaying the channel title more than 5 Crorers View Count')
    print('7 for displaying Line Graph')
    print('8 for displaying Bar Graph2')
    print('10 to quit')
    choice=int(input('Enter the choice...'))
    print('------------------------------------------------------')
    if choice==1:
        #Displaying First five rows of csv file
        try:    
            print('Displayiny first 5 rows')
            print(df.head())
        except:
            print('Something went wrong')            
    elif choice==2:
        try:
            print('Displaying last 5 rows')
            print(df.tail())
        except:
            print('Something went wrong')
    elif choice==3:
        try:
            ls=df.columns
            print('Columns in the csv file')
            print('-----------------------')
            for i in range(len(ls)):
                print(ls[i])
        except:
            print('Something went wrong')
    elif choice==4:
        try:
            print(df[['gender','international','race','work_exp']])
        except:
            print('Something went wrong')
    elif choice==5:
        try:
            print(df.describe())
        except:
            print('Something went wrong')
    elif choice==6:
        try:
            print('Displaying the Work Experience for MBA Students having work experience = 5 Years ')
            newdf=df.query('work_exp ==5')[['gender','international','race','work_exp']]
            print(newdf.to_string(index=False))
            #df.to_string(index=False)
        except:
            print('Something went wrong')       
    elif choice==7:
        try:
            print()
            df1=df.describe()
            ls=df1.values.tolist()
            colm=list(df1.columns)
            indx=list(df1.index)
            no_of_rows=len(indx)
            no_of_columns=len(colm)
            for i in range(no_of_rows):
                plt.title('Line Graph No. '+str(i+1)+' for '+indx[i])
                plt.xlabel('MBA Students')
                plt.ylabel(indx[i])
                plt.plot(colm,ls[i])
                plt.show()
        except:
            print('Something went wrong')
    elif choice==8:
        try:
            print()
            df1=df.describe()
            ls=df1.values.tolist()
            colm=list(df1.columns)
            indx=list(df1.index)
            no_of_rows=len(indx)
            no_of_columns=len(colm)
            for i in range(no_of_rows):
                plt.title('Bar Graph No. '+str(i+1)+' for '+indx[i])
                plt.xlabel('MBA Students')
                plt.ylabel(indx[i])
                plt.bar(colm,ls[i])
                plt.show()
        except:
            print('Something went wrong')
    elif choice==10:
        print('End of Job')
        break
    else:
        print('Wrong Choice...')
    print('======================================================')
    print()
