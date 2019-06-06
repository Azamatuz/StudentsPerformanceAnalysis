
import pandas as pd

def data_uploader():
    # Upload data from csv file
    # First read with header after creating col list add " header = None, "
    students_data = pd.read_csv("student-mat.csv")
    # it strange but csv file gives only one column so we need to split data of each row

    #creat columns name list and split one long string to 33 columns
    col = str(students_data.head(0)).split(';')

    # To delete trash data like 'Empty DataFrame\nColumns:'. Before I have found index of symbol for cutting columns[-1].rfind(']')

    col[0] = col[0][26:]
    col[-1] = col[-1][:2]

    #Split strang DF to list of separet rows
    rows_list = []
    for row in students_data.iterrows():
        rows_list.append(list(row[1].str.split(';')))

    #creat an empty DF with named columns
    df_students_data = pd.DataFrame(index=range(396), columns=col)

    #add data to each row
    for i in range(395):
        for j in range(33):
            df_students_data.loc[i][j] = rows_list[i][0][j]

    #Remove waste symbol
    df_students_data = df_students_data.replace({'"':''}, regex=True)
    return df_students_data

df = data_uploader()
df = df.drop([395])
df = df.drop(['reason' ], axis=1)

print(df[0:5])