import pandas as pd
import openpyxl
# Creating 2 data frames for each excel file.
df = pd.read_excel("Husband.xlsx")
df1 = pd.read_excel("Wife.xlsx")
column_H_husband = df['Gene']
column_H_wife = df1['Gene']
# Created a set to check if the output is correct.
shared_genes = set()
# New 2 data frames to move the data after detecting the common gene to 2 new excel files.
new_df = pd.DataFrame()
new_df1 = pd.DataFrame()
# 2 for loops checking the genes.
for i in range(len(column_H_wife)):
    for j in range(len(column_H_husband)):
        if column_H_wife[i] == column_H_husband[j]:
                shared_genes.add(column_H_wife[i])
                row_wife = df1.loc[df1['Gene'] == column_H_wife[i]]
                new_df = pd.concat([new_df, row_wife])
                row_husband = df.loc[df['Gene'] == column_H_husband[j]]
                new_df1 = pd.concat([new_df1, row_husband])
shared_genes = sorted(shared_genes)
print(shared_genes)
print(len(shared_genes))
# Writing the new 2 data frames to new 2 data excel files.
new_df.to_excel("MatchingWife.xlsx")
new_df1.to_excel("MatchingHusband.xlsx")

