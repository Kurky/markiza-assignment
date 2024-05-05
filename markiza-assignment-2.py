import pandas as pd
import glob

if __name__ == '__main__':
    filenames = glob.glob('csv_files/*.csv')  # get all filenames
    for filename in filenames:  # iterate over filenames
        print(filename)
        dataFrame = pd.read_csv(filename, sep=',')  # reading csv
        males = dataFrame[dataFrame['gender'] == 'Male']  # filtering just males
        sum_of_male_age = males['vek'].sum()  # counting sum of ages
        print('Sum of age for this file is:', int(sum_of_male_age))
