import pandas as pd


# categorizing the age field. Continuous to Categorical
def age_to_categorical(dataframe):
    cuts = pd.cut(dataframe['Age'], bins=10)
    hash_map = {}
    index_ = 0
    for e in cuts:
        if e not in hash_map:
            hash_map[e] = index_
            index_ += 1

    new_list = []
    for e in cuts:
        new_list.append(hash_map[e])
    return pd.Series(new_list)


