import pandas as pd



# this was a low hanging fruit. Replacing the None values with most frequent embarking station.
def fix_embarked(dataframe):
    dataframe.loc[61, "Embarked"] = 'S'


# categorizing the age field. Continuous to Categorical
def age_to_categorical(dataframe):
    cuts = pd.cut(dataframe['Age'], bins=10)
    hash_map = {}
    index_ = 0
    for e in cuts:
        if e not in hash_map:
            hash_map[e] = index_
            index_ += 1

    # replacing the intervals with respective discrete values.
    # fixing the NaNs.

    new_list = []
    for e in cuts:
        new_list.append(hash_map[e])
    return pd.Series(new_list)


