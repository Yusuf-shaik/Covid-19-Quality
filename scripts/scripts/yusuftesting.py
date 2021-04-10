from hosp import download_data, week_to_date
import unittest
from megafile import get_reprod

df = download_data()
print(df)
df = week_to_date(df)
print(df)


