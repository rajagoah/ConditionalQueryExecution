import pandas as pd

#Reading the content of the csv file
df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/Conditional query execution/Test Table.csv")

#displaying the names of the columns in the data frame
print(df[:0])

#declaring and initializing two data frames. One that will store the records that  have 3 in the C3 column
df_3 = pd.DataFrame([])
df_no_3 = pd.DataFrame([])

#iterating through each element in the data frame
for i in range(len(df)):

    #Conditional check to see if the C3 column for the selected row has 3
    if int(df["C3"][i:i+1]) == 3:
        df_3 = df_3.append(df[i:i+1])
    else:
        continue

#Conditional output that decides which data frame to output
if len(df_3) >= 1:
    print(df_3)
elif len(df) >= 1:
    print(df)