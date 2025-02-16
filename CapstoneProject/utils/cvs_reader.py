"""
cvs_reader.py
"""

import csv

def read_csv(file_path):
    """
    Read data from a CSV file and return it as a list of dictionaries.
    :param file_path: Path to the CSV file.
    :return: List of dictionaries containing the CSV data.
    """
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data
