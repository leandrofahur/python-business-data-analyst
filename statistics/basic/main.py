import pandas as pd
# import seaborn as sns

df = pd.read_csv('Baseball.csv')
print(df.head())

# Mean of Runs Scored (RS):
rs_mean = df.RS.mean()
print(f'\nRS Mean: {rs_mean}')

# Mean of Runs Scored (RS) by the Arizona team (ARI):
rs_mean_ari_team = df[df.Team == 'ARI'].RS.mean()
print(f'\nRS Mean for Arizona team: {rs_mean_ari_team}')

# Mean of Runs Scored: (RS) by the Arizona team (ARI) since 2005:
rs_mean_ari_team_since_2005 = df[(
    df.Team == 'ARI') & (df.Year > 2005)].RS.mean()
print(f'\nRS Mean for Arizona team since 2005: {rs_mean_ari_team_since_2005}')

# Mean of Runs Allowed (RA) by the Chicago team (CHC) until 2007:
ra_mean_chc_team_until_2007 = df[(
    df.Team == 'CHC') & (df.Year < 2007)].RA.mean()
print(f'\nRA Mean for Chicago team until 2007: {ra_mean_chc_team_until_2007}')
