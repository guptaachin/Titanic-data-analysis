import pandas as pd
import numpy as np
from random import shuffle

# this was a low hanging fruit. Replacing the None values with most frequent embarking station.
def fix_embarked(dataframe):
    dataframe.loc[61, "Embarked"] = 'S'
    dataframe.loc[829, "Embarked"] = 'S'


# cutting age variable
def cut_age_variable(dataframe):
    cuts = pd.cut(dataframe['Age'], bins=10)
    # categorizing the cuts variables
    hash_map = {}
    index_ = 0
    for e in cuts:
        if e not in hash_map:
            hash_map[e] = index_
            index_ += 1

    
    cat_variable = []
    for c,a in zip(cuts, dataframe['Age']):
        if hash_map[c] != 3:
            cat_variable.append(hash_map[c])
        else:
            cat_variable.append(np.nan)

    return pd.Series(cat_variable)


def create_distribution_list(ans):
    v_c = ans.value_counts()
    distribution_list = []
    for i, freq in zip(v_c.index, v_c):
        distribution_list += ([int(i)] * freq)
    shuffle(distribution_list)
    return distribution_list


def fix_age(dataframe, distribution_list, ans):
    dataframe['dis_age'] = ans
    for e in dataframe[dataframe['dis_age'].isnull()].index:
        dataframe.loc[e, 'dis_age'] = np.random.choice(distribution_list, replace=False)
    dataframe.dis_age = dataframe.dis_age.astype(int)


# categorizing the age field. Continuous to Categorical
def age_to_categorical(dataframe):
    cuts = pd.cut(dataframe['Age'], bins=10)


    # replacing the intervals with respective discrete values.
    # fixing the NaNs.

    new_list = []
    for e in cuts:
        new_list.append(hash_map[e])
    return pd.Series(new_list)


