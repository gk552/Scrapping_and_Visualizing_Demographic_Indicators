import pandas as pd

def drop_rows(df):
    # Prompt the user for the number of rows to drop from the head
    n = int(input("Enter the number of rows to drop from the head: "))

    # Prompt the user for the number of rows to drop from the tail
    m = int(input("Enter the number of rows to drop from the tail: "))

    # Drop 'n' rows from the beginning
    df = df.drop(df.head(n).index)

    # Drop 'm' rows from the end
    df = df.drop(df.tail(m).index)

    return df


def drop_columns(df):
    # Prompt the user if they want to drop any columns
    drop_columns = input("Do you want to drop any columns?: ")

    if drop_columns == 'yes':
        # Prompt the user for the column names to be dropped
        column_names = input("Enter the names of columns to be dropped (separate by commas): ")
        columns_to_drop = [col.strip() for col in column_names.split(',')]

        # Drop the specified columns
        df = df.drop(columns=columns_to_drop)

    return df


def rename_columns(df):
    # Prompt the user for the columns to rename and their new names
    num_columns = int(input("Enter the number of columns to rename: "))
    rename_dict = {}

    for i in range(num_columns):
        old_name = input("Enter the current name of column {0}: ".format(i+1))
        new_name = input("Enter the new name for column {0}: ".format(i+1))
        rename_dict[old_name] = new_name

    # Rename columns based on the provided dictionary
    df.rename(columns=rename_dict, inplace=True)

    return df


def preprocess_dataset():
    # Prompt the user for the file path
    file_path = input("Enter the path of the file to be modified: ")

    # Read Excel sheet into a DataFrame
    df = pd.read_excel(file_path)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Drop rows
    df = drop_rows(df)

    # Drop columns
    df = drop_columns(df)

    # Display the modified DataFrame
    print("\nModified DataFrame:")
    print(df)

    # Rename columns
    df = rename_columns(df)
    
    df.at[82, 'Year'] = 2017
    df.at[83, 'Year'] = 2018
    df.at[85, 'Year'] = 2020

    print("\nRenamed DataFrame:")
    print(df)

    # Save the modified DataFrame back to the original Excel file
    df.to_excel(file_path, index=False)
    print("Modified DataFrame saved to file:", file_path)


# Call the preprocess_dataset() function
preprocess_dataset()