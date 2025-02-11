
def wrangle(df):
    data1 = df.iloc[1:, 1:]
    data1.columns = data1.loc[1].values
    data1 = data1.drop(1, axis=0).reset_index().drop('index', axis=1)
    data1 = data1.fillna(0)
    data1 = data1.iloc[:-1, :]

    return data1

def cumulative(df):
    cumulative = df[['Total YIW','Total Female YIW', 'Total Male YIW']]
    return cumulative
    

def normal(df):
    norm = df.iloc[:, 6:9]
    return norm
    

def refuge(df):
    refuge = df[['Total Youth refugees in Work',
                          'Total Female Youth refugees in Work',
                          'Total Male Youth refugees in Work',]]
    return refuge
    

def community(df):
    community = df[['Total Youth Host community in Work',
                             'Total Female Youth Host community in Work',
                             ' Total Male Youth Host community in Work',]]
    return community


def pwd(df):
    pwd = df.iloc[:, 15:]
    return pwd
