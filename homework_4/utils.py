import pandas as pd


def fill_missing_values(row, year_cols, increase_percentage):
    #github check
    last_valid_value = None
    second_last_valid_value = None
    for i in range(len(year_cols)):
        if pd.isna(row[year_cols[i]]):
            if last_valid_value is None:
                row[year_cols[i]] = 0
            else:
                if second_last_valid_value is None:
                    row[year_cols[i]] = last_valid_value * (1 + increase_percentage)
                    second_last_valid_value = last_valid_value
                    last_valid_value = row[year_cols[i]]
                else:
                    diff = last_valid_value - second_last_valid_value
                    row[year_cols[i]] = last_valid_value + diff
                    second_last_valid_value = last_valid_value
                    last_valid_value = row[year_cols[i]]
        else:
            second_last_valid_value = last_valid_value
            last_valid_value = row[year_cols[i]]
    return row

