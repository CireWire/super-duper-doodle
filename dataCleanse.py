import csv


def datacleanse():
    # specify the input and output file paths
    input_file = 'Electric_Vehicle_Population_Data.csv'
    output_file = 'cleaned_ev_data.csv'

    # specify the columns to filter
    columns_to_keep = ['VIN (1-10)', 'State', 'Model Year', 'Make', 'Model', 'Electric Vehicle Type',
                       'Vehicle Location']

    # read in the input file and open the output file for writing
    with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as output_csv_file:
        # create a CSV reader and writer objects
        reader = csv.DictReader(csv_file)
        writer = csv.DictWriter(output_csv_file, fieldnames=columns_to_keep)

        # write the header row to the output file
        writer.writeheader()

        # iterate through each row in the input file and write the desired columns to the output file
        for row in reader:
            filtered_row = {col: row[col] for col in columns_to_keep}
            writer.writerow(filtered_row)
