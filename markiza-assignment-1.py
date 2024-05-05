import random
import re


def generator(string_len=random.randint(1, 100)):
    random_string = ''
    for j in range(string_len):
        random_string += chr(random.randint(33, 126))  # 33 and 126 is range of chars in ascii table
    return random_string


if __name__ == '__main__':
    string_list = ['18115', 'file.json', 'csvfile.csv', '2019-05-27']  # adding some examples to see function of lambdas
    for i in range(1000):
        string_list.append(generator(9))  # 9 is length of string
    print(string_list)
    only_inegers = lambda lst: [s for s in lst if re.match(r'^\d+$', s) is not None]  # filtering integers with regex
    print('Only integers list:', only_inegers(string_list))
    ending_csv_json = lambda lst: [s for s in lst if s.endswith('.csv') or s.endswith(
        '.json')]  # filtering ending .json and .csv with endswith
    print('Ending with ".json" or ".csv" list:', ending_csv_json(string_list))
    filter_iso_dates = lambda lst: [s for s in lst if
                                    re.match(r'\d{4}-\d{2}-\d{2}', s) is not None]  # filtering iso dates with regex
    print('Dates in ISO format list:', filter_iso_dates(string_list))
