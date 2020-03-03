import pandas as pd

cols = ['PersonId', 'Name', 'LastName', 'CurrentRole', 'Country', 
        'Industry', 'NumberOfRecommendations','NumberOfConnections']
profiles = pd.read_csv('R&D Challenge - file 2 (people).in', sep='|', header=None, names=cols)


def recommend(profiles, CurrentRole=None, Country=None, Industry=None):
    """Returns the ids of top profiles which have the good conversion rate"""
    
    # filter profiles if needed only to a particular
    # country, role or industry. This can help us narrow down our target list
    
    if CurrentRole:
        profiles = profiles[profiles['CurrentRole'] == CurrentRole]
    if Country:
        profiles = profiles[profiles['Country'] == Country]
    if Industry:
        profiles = profiles[profiles['Industry'] == Industry]
    
    # to identify top management profiles with high decision power
    profiles = profiles[profiles["CurrentRole"].str.contains("board|director|vice|president|chairman|owner|partner|officer|chief|senior", na=False)]
    
    # sort by stronger profiles
    profiles = profiles.sort_values(['NumberOfConnections', 'NumberOfRecommendations'], ascending=False)
    
    ids = profiles['PersonId'][:10].values.tolist()
    ids = [str(personid) for personid in ids]
    
    # write the ids to a people.out file
    with open('people.out', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(ids))
        
    return profiles
    
    
r = recommend(profiles=profiles)
r.head(10)