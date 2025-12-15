import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # drop duplicates from employee and sort by descending reset index dropping what 
    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    # base case if there are less than n distinct salaries return null
    #pd.DataFrame takes dictionary f-string, and None array 
    if(len(salaries) < N or N <=0 ) : return pd.DataFrame({f"getNthHighestSalary({N})" : [None]})

    print(salaries)
    #pass f-string and iloc as dictionary as new dataframe pass salaries.iloc as array
    return pd.DataFrame({f"getNthHighestSalary({N})" : [salaries.iloc[N-1]]})