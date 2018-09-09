import pandas as pd
import numpy as np
from random import shuffle

# this was a low hanging fruit. Replacing the None values with most frequent embarking station.
def fix_embarked(dataframe):
    dataframe.loc[61, "Embarked"] = 'S'
    dataframe.loc[829, "Embarked"] = 'S'


# cutting age variable
def cut_age_variable(dataframe, bins_, str_):
    cuts = pd.cut(dataframe[str_], bins=bins_)
    # categorizing the cuts variables
    hash_map = {}
    index_ = 0
    for e in cuts:
        if e not in hash_map:
            hash_map[e] = index_
            index_ += 1

    cat_variable = []
    for c,a in zip(cuts, dataframe[str_]):
        if np.isnan(a):
            cat_variable.append(np.nan)
        else:
            cat_variable.append(hash_map[c])

    return pd.Series(cat_variable)


def create_distribution_list(ans):
    v_c = ans.value_counts()
    distribution_list = []
    for i, freq in zip(v_c.index, v_c):
        distribution_list += ([int(i)] * freq)
    shuffle(distribution_list)
    return distribution_list


def fix_age(dataframe, distribution_list, ans, str_):
    dataframe['dis_'+str_] = ans
    for e in dataframe[dataframe['dis_'+str_].isnull()].index:
        dataframe.loc[e, 'dis_'+str_] = np.random.choice(distribution_list, replace=False)
    dataframe['dis_'+str_] = dataframe['dis_'+str_].astype(int)


def cont_discrete(dataframe, bins_, str_):
    # cutting the age_variable
    ans = cut_age_variable(dataframe, bins_, str_)
    # creating the distribution list
    dist_list = create_distribution_list(ans)
    # populating the Age NaNs
    fix_age(dataframe, dist_list, ans, str_)


def discretize_field(dataframe, str_):
    series = dataframe[str_]
    u_values = series.unique()
    h_map = {}
    counter = 0
    for u in u_values:
        if u not in h_map:
            h_map[u] = counter
            counter += 1
    new_list = list()
    for each in dataframe[str_]:
        new_list.append(h_map[each])

    dataframe['dis_'+str_] = pd.Series(new_list)


# using information from the names field.
def working_with_names(dataframe):
    ex_series = dataframe.Name.str.extract("([A-Za-z]*\.)")
    ls_ = []
    female_ = set(['Miss.', 'Mrs.', 'Ms.'])
    male_ = set(['Mr.'])
    child_ = set(['Master.'])
    imp_people = set(["Dr.", "Rev.", "Col.", "Mlle.", "Major.", "Jonkheer.", "Capt.", "Sir.", "Don.", "Countess.", "Lady.", "Mme."])

    for e in ex_series:
        if e in female_:
            ls_.append(0)
        elif e in male_:
            ls_.append(1)
        elif e in child_:
            ls_.append(2)
        elif e in imp_people:
            ls_.append(3)

    dataframe['dis_name'] = pd.Series(ls_)


# using information from the names field.
def have_siblings_not(dataframe):
    ls_ = []

    for s,p in zip(dataframe['SibSp'], dataframe['Parch']):
        if (s+p) > 0:
            ls_.append(1)
        else:
            ls_.append(0)

    dataframe['hasSomeOne'] = pd.Series(ls_)
    