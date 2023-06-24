import pandas as pd
import openpyxl
df = pd.read_excel("Husband.xlsx")
df1 = pd.read_excel("Wife.xlsx")
column_H_husband = df['Gene']
column_H_wife = df1['Gene']
shared_genes = set()
new_df = pd.DataFrame()
new_df1 = pd.DataFrame()
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
new_df.to_excel("MatchingWife.xlsx")
new_df1.to_excel("MatchingHusband.xlsx")

