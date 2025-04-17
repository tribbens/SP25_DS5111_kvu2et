import pandas as pd
import subprocess

path1 = "collected_data/"
path2 = "temp/"

fname_df = pd.read_csv("scripts/fnames_list.csv")
fname_list = list(fname_df['Name'])

for fname in fname_list:
    new_fname = fname.strip('-')

    src = path1 + fname
    dst = path2 + new_fname

    subprocess.run(["cp", src, dst], check=True)

