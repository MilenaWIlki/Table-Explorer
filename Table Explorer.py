import pandas as pd

def explore_periodic_table():
    periodic_table = pd.read_csv('periodic_table.csv')  # Assuming periodic_table.csv contains element data
    print(periodic_table)

explore_periodic_table()
