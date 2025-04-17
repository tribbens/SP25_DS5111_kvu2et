import pandas as pd
import subprocess

path = "temp/"

fname_df = pd.read_csv("scripts/fnames_list.csv")
fname_list = list(fname_df['Name'])

for fname in fname_list:
    new_fname = fname.replace('-', '')

    src = path + fname
    dst = path + new_fname

    subprocess.run(["mv", src, dst], check=True)
