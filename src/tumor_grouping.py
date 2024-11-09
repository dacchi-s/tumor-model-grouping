import pandas as pd
import numpy as np
import argparse

# Function to load CSV file
def load_csv(file_path):
    # Load CSV file using pandas
    data = pd.read_csv(file_path)
    return data

# Function to group mice by tumor volume
def group_by_tumor_volume(data, num_groups):
    # Sort by tumor_volume (descending order)
    sorted_data = data.sort_values(by='tumor_volume', ascending=False).reset_index(drop=True)
    
    # Create a new column to store group assignments
    sorted_data['Group'] = np.nan
    
    # Initialize groups
    group_sums = [0] * num_groups  # Holds total tumor size for each group
    
    # Assign mice to groups, starting with largest tumors, adding to group with smallest total
    for index, row in sorted_data.iterrows():
        size = row['tumor_volume']
        # Find the group with smallest total tumor volume
        min_group_index = np.argmin(group_sums)
        # Set group number (starting from 1)
        sorted_data.at[index, 'Group'] = min_group_index + 1
    
        # Update group's total size
        group_sums[min_group_index] += size
    
    return sorted_data

# Display and save group results as a DataFrame
def display_and_save_groups(data, file_path):
    grouped_data = data.groupby('Group')
    results = []

    for group, df in grouped_data:
        mice = df['mouse'].tolist()
        tumor_volumes = df['tumor_volume'].tolist()
        average_volume = df['tumor_volume'].mean()
        std_dev_volume = df['tumor_volume'].std()  # Calculate standard deviation
        result_entry = {
            'Group': int(group),
            'Mice': mice,
            'Tumor Volumes': tumor_volumes,
            'Average Tumor Volume': round(average_volume, 2),
            'Standard Deviation': round(std_dev_volume, 2)  # Add standard deviation
        }
        results.append(result_entry)

    # Save as DataFrame
    results_df = pd.DataFrame(results)

    # Save results to CSV
    output_file_path = file_path.replace('.csv', '_grouped_results_with_variability.csv')
    results_df.to_csv(output_file_path, index=False)
    
    # Display in console
    print(results_df)
    
    return results_df

# Main processing
def main(file_path, num_groups):
    # Load CSV file
    data = load_csv(file_path)
    
    # Perform grouping
    grouped_data = group_by_tumor_volume(data, num_groups)
    
    # Display and save group results
    display_and_save_groups(grouped_data, file_path)
    
    # Save grouping results to new CSV file
    output_file_path = file_path.replace('.csv', '_grouped.csv')
    grouped_data.to_csv(output_file_path, index=False)
    print(f"Grouping results saved to {output_file_path}")

# Entry point
if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Group mice by tumor volume and save results to a new CSV.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file containing tumor_volume and mouse data.')
    parser.add_argument('--num_groups', type=int, default=3, help='Number of groups to divide the data into (default: 3).')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute main processing
    main(args.file_path, args.num_groups)