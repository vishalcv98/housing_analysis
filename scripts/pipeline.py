from clean_data import *
from feature_engineering import *
from load_data import *

from pathlib import Path

DATA_DIR = Path(r"c:\Users\swath\OneDrive\Desktop\housing_analysis\data")

df_a = load_dataframes(DATA_DIR / "houses_a.csv")
df_b = load_dataframes(DATA_DIR / "houses_b.csv")
df_c = load_dataframes(DATA_DIR / "houses_c.csv")
df_d = load_dataframes(DATA_DIR / "houses_d.csv")

houses = combine_dataframes(df_a, df_b, df_c, df_d)

houses = replace_with_na(houses, ["PoolQC", "MiscFeature"])
houses = replace_nulls_with_median(houses, ["MasVnrArea"])
houses = drop_duplicates(houses, ["Id"])


houses = create_features(houses)

houses.to_csv(DATA_DIR / "processed_houses.csv", index=False)
