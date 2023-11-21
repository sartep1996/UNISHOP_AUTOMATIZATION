import pandas as pd


df1 = pd.read_excel("C:\\Users\\PetrasAnksaitis\\Downloads\\COMBINING TWO DATABASES\\Rekvizitai 1 bandymas 231009 Unishop.xlsx", sheet_name='Įmonės (2)', names=['Kompanija', 'Rekvizitai URL'])

df2 = pd.read_excel("C:\\Users\\PetrasAnksaitis\\Downloads\\COMBINING TWO DATABASES\\ClientList_Petro_not_finished.xlsx", sheet_name='Short List')


merged_df = pd.merge(df1, df2[['Įmonė', 'Hyperlink_Column']], left_on='Kompanija', right_on='Įmonė', how='left')

merged_df.to_excel("C:\\Users\\PetrasAnksaitis\\Downloads\\COMBINING TWO DATABASES\\NEW_COMBINED_DATABASE.xlsx", index=False)
