import pandas as pd
from datetime import datetime

def find_matching_addresses(file_paths, output_file, threshold_balance=10000):
    # Read the CSV files into pandas dataframes
    dfs = [pd.read_csv(file_path, header=None, skiprows=1) for file_path in file_paths]

    # Assuming the addresses are in the first column of each dataframe
    addresses_sets = [set(df.iloc[:, 0].astype(str)) for df in dfs]

    # Find the common addresses among all sets
    common_addresses = set.intersection(*addresses_sets)

    # Filter dataframes to keep only rows with matching addresses
    df_filtered = pd.concat([df[
            (df.iloc[:, 0].astype(str).isin(common_addresses)) & 
            (df.iloc[:, 1].str.replace(',', '').astype(float) > threshold_balance)
        ] for df in dfs])
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = f'{output_file}\\Crypto_Files_{timestamp}.xlsx'

    



    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        df_filtered.to_excel(writer, sheet_name='Sheet1', index=False, header=False)

if __name__ == "__main__":
    # Provide the file paths for your CSV files
    file_paths = [
        "C:\\Users\\sarte\\Downloads\\BEAMexport-tokenholders-for-contract-0x62D0A8458eD7719FDAF978fe5929C6D342B0bFcE.csv",
        'C:\\Users\\sarte\\Downloads\\DERCexport-tokenholders-for-contract-0x9fa69536d1cda4a04cfb50688294de75b505a9ae.csv',
        'C:\\Users\\sarte\\Downloads\\BCBexport-tokenholders-for-contract-0x2d886570a0da04885bfd6eb48ed8b8ff01a0eb7e.csv',
        'C:\\Users\\sarte\\Downloads\\export-tokenholders-for-contract-0xe53ec727dbdeb9e2d5456c3be40cff031ab40a55.csv'

    ]

    # Specify the output file path
    output_file_path = 'C:\\Users\\sarte\\OneDrive\\Desktop\\Crypto Checker\\'

    # Call the function to find and store matching addresses
    find_matching_addresses(file_paths, output_file_path)

    print("Matching addresses saved to", output_file_path)