'''
This project is about anlaysis of movie data
movieid
moviename
actorname
yearofrelease
ratingstar
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    print('Reading csv file')
    print('----------------')
    '''..................Important copy following file:  IN_youtube_trending_data_New.csv 
    in the csnip folder of your compurer to run the project successfully............. '''
    df=pd.read_csv('movie.csv')
except:
    print('Something went wrong')
    
while True:
    print('======================================================')
    print('1 for displayiny first 5 rows')
    print('2 for displaying last 5 rows')
    print('3 for displaying all the columns of csv file')
    print('4 for displaying information of movie id,movie name,year of release,actor name,rating star')
    print('5 for Statistical Analysis')
    print('6 for displaying the ratingstar more than 4')
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
            print(df[['movieid','moviename','yearofrelease','actorname','ratingstar']])
        except:
            print('Something went wrong')
    elif choice==5:
        try:
            print(df.describe())
        except:
            print('Something went wrong')
    elif choice==6:
        try:
            print('ratingstar more than 4')
            newdf=df.query('ratingstar >4')[['movieid','moviename','yearofrelease','actorname','ratingstar']]
            #print(newdf[['channelTitle','view_count']])
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
                plt.xlabel('Movie Data')
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
                plt.xlabel('Movie Data')
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
