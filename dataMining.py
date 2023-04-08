import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


def datamining():
    # Load the cleaned EV data into a Pandas dataframe
    ev_data = pd.read_csv('cleaned_ev_data.csv')

    # Group the data by State and Make, and calculate the count of each combination
    state_make_counts = ev_data.groupby(['State', 'Make']).size().reset_index(name='Count')

    # Pivot the data to create a matrix with State as rows, Make as columns, and Count as values
    state_make_matrix = state_make_counts.pivot(index='State', columns='Make', values='Count').fillna(0)

    # Scale the matrix using min-max scaling to ensure each feature has the same weight
    state_make_matrix_scaled = (state_make_matrix - state_make_matrix.min()) / (
            state_make_matrix.max() - state_make_matrix.min())

    # Reset the index of the dataframe
    state_make_matrix_scaled = state_make_matrix_scaled.reset_index()

    # Apply KMeans clustering to the scaled matrix, with k=5 clusters
    kmeans = KMeans(n_clusters=5).fit(state_make_matrix_scaled.iloc[:, 1:-1])

    # Add the cluster labels to the scaled matrix dataframe
    state_make_matrix_scaled['Cluster'] = kmeans.labels_

    # Pivot the data back to the original format
    state_make_counts = state_make_matrix_scaled.melt(id_vars=['State', 'Cluster'], var_name='Make', value_name='Count')
    state_make_counts = state_make_counts[state_make_counts['Count'] != 0]

    # Group the data by Cluster and Make, and calculate the total count of each Make within each cluster
    cluster_make_counts = state_make_counts.groupby(['Cluster', 'Make'])['Count'].sum().reset_index(name='Total Count')

    # Create a plot to visualize the clusters
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(state_make_counts['Make'], state_make_counts['State'], c=state_make_counts['Cluster'])
    ax.set_xlabel('Make')
    ax.set_ylabel('State')
    ax.set_title('Vehicle Make Clusters by State')
    ax.legend(*scatter.legend_elements(), title='Cluster')
    plt.xticks(rotation=90)
    plt.show()

    # Print the counts of each Make within each cluster
    print(cluster_make_counts)
