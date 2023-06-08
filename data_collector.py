import os
import pandas as pd

for root, dirs, files in os.walk('raw_data_tue_wen'):
    df_list_for_files = []
    for file in files:
        symbols = list(file)
        with open(os.path.join(root, file), "rt", encoding="latin-1") as f:
            text = f.read()
            strings = text.splitlines()
            times, currents, voltages = [], [], []
            for string in strings:
                one_string = string.split(' ')
                norm_string = ' '.join(one_string).split()
                if len(norm_string) == 4:
                    times.append(norm_string[1])
                    currents.append(norm_string[2])
                    voltages.append(norm_string[3])
        df = pd.DataFrame(list(zip(times, currents, voltages)), columns=['Time', 'Current', 'Voltage'])
        new_filename = file.split('.')[0] + '.csv'
        print(new_filename)
        df.to_csv(os.path.join('correct_data', new_filename))
