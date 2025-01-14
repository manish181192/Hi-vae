import pandas as pd
import numpy as np
import config
# import json
datapath = "/home/manish/ML/Rutgers/Project/ML3/ML3/ML3AllSites.csv"

df = pd.read_csv(datapath)
# print(list(df))
col = "Experimenter"
df = df[[col]]
# df[col] = df[col].fillna(-1)
# df[col] = df[col].astype(int)
# df[col] = df[col].astype(str)
# df[col] = df[col].replace('-1', np.nan)

# print(df["RowNumber"])
def frequency_table(x):
    return pd.crosstab(index=x,  columns="count")

def get_frequency_dist():
    freqDistFile = open("freqDist.txt", "w")
    ctabs = {}
    for column in df:
        ctabs[column]=frequency_table(df[column])
        freqDistFile.write(column+"\n")
        freqDistFile.write(ctabs[column].to_string()+"\n\n\n")
    freqDistFile.close()
    print("Generated frequency distribution file")

def generate_vocab_files(printFile):
    vocab_dir = "vocab_dir/"
    reverse_vocab_dir = "reverse_vocab_dir/"
    ctabs = {}
    for column in df:
        ctabs[column] = frequency_table(df[column])

        feature_vocab = {}
        reversed_feature_vocab = {}
        current_id = 0
        for k, v in ctabs[column].to_dict()['count'].items():
            feature_vocab[k] = current_id
            reversed_feature_vocab[current_id] = k
            current_id += 1
        if printFile: print(str(feature_vocab))
        np.save(vocab_dir + column, feature_vocab)
        np.save(reverse_vocab_dir + column, reversed_feature_vocab)
        print("Vocab Size: {}".format(len(feature_vocab)))
        print("done")

if __name__=="__main__":
    generate_vocab_files(printFile=True)
