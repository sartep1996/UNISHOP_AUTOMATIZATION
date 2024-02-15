import pandas as pd
from datetime import datetime

def find_matching_addresses(file_paths, output_file, threshold_balance=10000):
    dfs = [pd.read_csv(file_path, header=None, skiprows=1) for file_path in file_paths]

    addresses_sets = [set(df.iloc[:, 0].astype(str)) for df in dfs]

    common_addresses = set.intersection(*addresses_sets)

    num_files = len(file_paths)
    column_names = ["Address"] + [f"Balance_{i+1}" for i in range(num_files)]
    consolidated_df = pd.DataFrame(columns=column_names)

    for address in common_addresses:
        balances = []
        for df in dfs:
            balance = df.loc[df.iloc[:, 0].astype(str) == address, 1].str.replace(',', '').astype(float).values
            if len(balance) > 0: 
                balances.append(balance[0])
            else:
                balances.append(0)

        if all(balance > threshold_balance for balance in balances):
            row_data = [address] + balances
            consolidated_df = pd.concat([consolidated_df, pd.DataFrame([row_data], columns=column_names)], ignore_index=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = f'{output_file}\\Crypto_Files_{timestamp}.xlsx'

    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        consolidated_df.to_excel(writer, sheet_name='Sheet1', index=False, header=True)

if __name__ == "__main__":
    file_paths = [
        "C:\\Users\\sarte\\Downloads\\INSPECTexport-tokenholders-for-contract-0x186eF81fd8E77EEC8BfFC3039e7eC41D5FC0b457.csv",
        "C:\\Users\\sarte\\Downloads\\PAIDNETWORKSexport-tokenholders-for-contract-0x1614F18Fc94f47967A3Fbe5FfcD46d4e7Da3D787.csv",
        "C:\\Users\\sarte\\Downloads\\MYRIAexport-tokenholders-for-contract-0xa0ef786bf476fe0810408caba05e536ac800ff86 (1).csv",
        "C:\\Users\\sarte\\Downloads\\SUPERFARMexport-tokenholders-for-contract-0xe53ec727dbdeb9e2d5456c3be40cff031ab40a55 (1).csv",
        "C:\\Users\\sarte\\Downloads\\BEAMMexport-tokenholders-for-contract-0x62D0A8458eD7719FDAF978fe5929C6D342B0bFcE.csv",
        "C:\\Users\\sarte\\Downloads\\ALTURAexport-tokenholders-for-contract-0x8263CD1601FE73C066bf49cc09841f35348e3be0.csv",
    ]

    output_file_path = 'C:\\Users\\sarte\\OneDrive\\Desktop\\Crypto Checker\\'

    find_matching_addresses(file_paths, output_file_path)

    print("Matching addresses saved to", output_file_path)
