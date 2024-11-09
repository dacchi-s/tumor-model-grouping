# Tumor Model Grouping Tool

This Python script helps researchers divide tumor model animals into groups based on their tumor volumes. It ensures that the total tumor volume is distributed evenly across groups, which is important for experimental design in cancer research.

## Features

- Reads mouse data from CSV files
- Sorts mice by tumor volume
- Creates balanced groups by distributing tumor volumes evenly
- Calculates statistics for each group (average tumor volume and standard deviation)
- Saves results in new CSV files
- Supports flexible number of groups

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - pandas
  - numpy
  - argparse

You can install the required packages using pip:

```bash
pip install pandas numpy
```

If you prefer to use a conda environment:

```
conda install pandas numpy
```

## Input CSV Format

Your input CSV file should have at least these columns:
- `mouse`: Mouse identifier
- `tumor_volume`: Tumor volume measurement

Example:
```csv
mouse,tumor_volume
M1,100.5
M2,85.3
M3,120.7
```

## How to Use

1. Run the script:
```bash
python tumor_grouping.py "path/to/your/data.csv" --num_groups 3
```

### Command Line Arguments

- `file_path`: Path to your input CSV file (required)
- `--num_groups`: Number of groups to create (optional, default: 3)

## Output Files

The script creates two output files:

1. `*_grouped.csv`: Contains the original data with an additional 'Group' column
2. `*_grouped_results_with_variability.csv`: Contains summary statistics for each group, including:
   - Group number
   - List of mice in the group
   - List of tumor volumes
   - Average tumor volume
   - Standard deviation of tumor volumes

## Example Usage

```bash
python group_mice.py mouse_data.csv --num_groups 4
```

This command will:
1. Read mouse_data.csv
2. Create 4 balanced groups
3. Save results in:
   - mouse_data_grouped.csv
   - mouse_data_grouped_results_with_variability.csv

## How It Works

1. The script reads the input CSV file
2. Sorts mice by tumor volume (largest to smallest)
3. Assigns each mouse to the group with the lowest total tumor volume
4. Calculates statistics for each group
5. Saves the results

This approach ensures that the total tumor volume is distributed as evenly as possible across all groups.
