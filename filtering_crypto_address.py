import pandas as pd
import os

def find_matching_addresses(file1, file2, file3, output_file):
    # Read the CSV files into pandas dataframes
    df1 = pd.read_csv(file1, header=None)  # Assuming the addresses are in the first column
    df2 = pd.read_csv(file2, header=None)
    df3 = pd.read_csv(file3, header=None)

    # Extract crypto wallet addresses from the first column of each dataframe
    addresses1 = set(df1.iloc[:, 0].astype(str))
    addresses2 = set(df2.iloc[:, 0].astype(str))
    addresses3 = set(df3.iloc[:, 0].astype(str))

    # Find the common addresses among all three sets
    common_addresses = addresses1.intersection(addresses2, addresses3)

    # Filter dataframes to keep only rows with matching addresses
    df1_filtered = df1[df1.iloc[:, 0].astype(str).isin(common_addresses)]
    df2_filtered = df2[df2.iloc[:, 0].astype(str).isin(common_addresses)]
    df3_filtered = df3[df3.iloc[:, 0].astype(str).isin(common_addresses)]

    # Create a new Excel file with the filtered data
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df1_filtered.to_excel(writer, sheet_name='Sheet1', index=False, header=False)  # Avoid writing headers
        df2_filtered.to_excel(writer, sheet_name='Sheet2', index=False, header=False)
        df3_filtered.to_excel(writer, sheet_name='Sheet3', index=False, header=False)

if __name__ == "__main__":
    # Provide the file paths for your CSV files
    file1_path = 'C:\\Users\\sarte\\Downloads\\BEAMexport-tokenholders-for-contract-0x62D0A8458eD7719FDAF978fe5929C6D342B0bFcE.csv'
    file2_path = 'C:\\Users\\sarte\\Downloads\\DERCexport-tokenholders-for-contract-0x9fa69536d1cda4a04cfb50688294de75b505a9ae.csv'
    file3_path = 'C:\\Users\\sarte\\Downloads\\BCBexport-tokenholders-for-contract-0x2d886570a0da04885bfd6eb48ed8b8ff01a0eb7e.csv'

    # Specify the output file path
    output_file_path = 'C:\\Users\\sarte\\OneDrive\\Desktop\\Crypto Checker\\Crypto Files.xlsx'

    # Call the function to find and store matching addresses
    find_matching_addresses(file1_path, file2_path, file3_path, output_file_path)

    print("Matching addresses saved to", output_file_path)
