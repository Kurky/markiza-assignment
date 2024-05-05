import pandas as pd
import glob

if __name__ == '__main__':
    filenames = glob.glob('csv_files/*.csv')
    for filename in filenames:
        print(filename)
        dataFrame = pd.read_csv(filename, sep=',')
        males = dataFrame[dataFrame['gender'] == 'Male']
        sum_of_male_age = males['vek'].sum()
        print('Sum of age for this file is:', int(sum_of_male_age))
