import pandas as pd

df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/Conditional query execution/Test Table.csv")
print(df[:0])
df_3 = pd.DataFrame([])
df_no_3 = pd.DataFrame([])
for i in range(len(df)):
    if int(df["C3"][i:i+1]) == 3:
        df_3 = df_3.append(df[i:i+1])
    else:
        df_no_3 = df_no_3.append(df[i:i+1])

#Conditional output
if len(df_3) >= 1:
    print(df_3)
elif len(df_no_3) >= 1:
    print(df_no_3)