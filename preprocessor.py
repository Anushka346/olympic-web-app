import pandas as pd



def preprocess(df,region_df):
    #filter all summer olympics
    df=df[df['Season']=='Summer']
    #merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #conatinatig all medat sep in df
    df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df
