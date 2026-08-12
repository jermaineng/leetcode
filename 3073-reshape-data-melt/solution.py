import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars='product', var_name='quarter', value_name='sales')

    # melt makes a wide dataframe long (turning columns into rows), 
    # while pivot makes a long dataframe wide
