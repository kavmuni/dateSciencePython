import pandas as pd
import numpy as np
# read csv is not working as this file is a TAB separated, extension is ".tsv"
chipo = pd.read_table("https://raw.githubusercontent.com/Laxminarayen/Inceptez-batch-25-Classwork/refs/heads/main/Python-Class10-Pandas-Intermediate/chipotle.tsv"
                          )
print(chipo.head(10))

