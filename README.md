# LSTM_DEEP

Dataset of Cryptocurrency

This repository contain datasets required for Index fund.

Please check updated code in Alkon30_v1.R file


https://beta.vu.nl/nl/Images/stageverslag-wetstein_tcm235-851825.pdf

http://www.dfki.de/~sonntag/gridsem04ECAI2.pdf

http://ccis2k.org/iajit/PDF/%20Vol%2013,%20No.%201A%20(Special%20Issue)/348.pdf

https://arxiv.org/pdf/1711.08726.pdf
https://cs224d.stanford.edu/reports/StrohMathur.pdf

https://staff.fnwi.uva.nl/m.derijke/Publications/Files/flexdbist2007.pdf

import pandas as pd

# Sample data for demonstration
data_a = {
    'ID': [1, 2, 3, 4],
    'Age': [25, 30, 35, 40],
    'Income': [50000, 60000, 70000, 80000]
}

data_b = {
    'Age': [30, 35],
    'Income': [60000, 70000]
}

df_a = pd.DataFrame(data_a)
df_b = pd.DataFrame(data_b)

# Merge dataframes on 'Age' and 'Income'
merged_df = pd.merge(df_a, df_b, on=['Age', 'Income'], how='inner')

# Extract the 'ID' column from the merged dataframe
result_ids = merged_df['ID']

print(result_ids)
