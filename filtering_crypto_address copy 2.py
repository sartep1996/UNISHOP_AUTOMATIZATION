import pandas as pd
from datetime import datetime
import openpyxl

def find_matching_addresses(file_paths, output_file_path):
    # Read the CSV files into pandas dataframes
    dfs = [pd.read_csv(file_path, header=None) for file_path in file_paths]

    # Assuming the addresses are in the first column of each dataframe
    addresses_sets = [set(df.iloc[:, 0].astype(str)) for df in dfs]

    # Find the common addresses among all sets
    common_addresses = set.intersection(*addresses_sets)

    common_addresses_df = pd.DataFrame(list(common_addresses), columns=['Crypto Wallet Addresses'])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_directory = "C:\\Users\\sarte\\OneDrive\\Desktop\\Crypto Checker"
    output_file_path = f'{output_directory}\\Crypto_Files_{timestamp}.xlsx'
    
    common_addresses_df.to_excel(output_file_path, index=False, startrow=1, startcol=0, )



if __name__ == "__main__":
    # Provide the file paths for your CSV files
    file_paths = [
        "C:\\Users\\sarte\\Downloads\\BEAMexport-tokenholders-for-contract-0x62D0A8458eD7719FDAF978fe5929C6D342B0bFcE.csv",
        'C:\\Users\\sarte\\Downloads\\DERCexport-tokenholders-for-contract-0x9fa69536d1cda4a04cfb50688294de75b505a9ae.csv',
        'C:\\Users\\sarte\\Downloads\\BCBexport-tokenholders-for-contract-0x2d886570a0da04885bfd6eb48ed8b8ff01a0eb7e.csv',
        'C:\\Users\\sarte\\Downloads\\export-tokenholders-for-contract-0xe53ec727dbdeb9e2d5456c3be40cff031ab40a55.csv'

    ]

    # Specify the output file path
    output_file_path = 'C:\\Users\\sarte\\OneDrive\\Desktop\\Crypto Checker\\Crypto Files.xlsx'

    # Call the function to find and store matching addresses
    find_matching_addresses(file_paths, output_file_path)

    print("Matching addresses saved to", output_file_path)

       