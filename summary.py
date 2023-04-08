import pandas as pd


def summary():
    # Load the cleaned EV data into a Pandas dataframe
    ev_data = pd.read_csv('cleaned_ev_data.csv')

    # Group the data by State and Make, and calculate the count and percentage
    state_make_counts = ev_data.groupby(['State', 'Make'])['Make'].agg(['count', 'size'])
    state_make_counts.rename(columns={'count': 'Count', 'size': 'Total'}, inplace=True)
    state_make_counts['Percentage'] = state_make_counts['Count'] / state_make_counts['Total']

    # Print the top 10 most common vehicle makes for each state
    for state, group in state_make_counts.groupby('State'):
        print(f"State: {state}")
        print(group.sort_values(by='Count', ascending=False).head(10))
        print("\n")
