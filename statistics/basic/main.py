import pandas as pd
# import seaborn as sns

df = pd.read_csv('Baseball.csv')
print(df.head())

print('\nMean:')

# Mean of Runs Scored (RS):
rs_mean = df.RS.mean()
print(f'\nRS Mean: {rs_mean}')

# Mean of Runs Scored (RS) by the Arizona team (ARI):
rs_mean_ari_team = df[df.Team == 'ARI'].RS.mean()
print(f'RS Mean for Arizona team: {rs_mean_ari_team}')

# Mean of Runs Scored: (RS) by the Arizona team (ARI) since 2005:
rs_mean_ari_team_since_2005 = df[(
    df.Team == 'ARI') & (df.Year > 2005)].RS.mean()
print(f'RS Mean for Arizona team since 2005: {rs_mean_ari_team_since_2005}')

# Mean of Runs Allowed (RA) by the Chicago team (CHC) until 2007:
ra_mean_chc_team_until_2007 = df[(
    df.Team == 'CHC') & (df.Year < 2007)].RA.mean()
print(f'RA Mean for Chicago team until 2007: {ra_mean_chc_team_until_2007}')

# ------------------------------------------------------------------------------
# Mode: most frequent value in a set
# Median: middle value in a set

# Mean and median are not affected by outliers, but mode is affected by outliers. Let's check for the number of wins (W)
print('\nMean and median:')
wins_mean = df.W.mean()
print(f'\nWins Mean: {wins_mean}')

wins_meadian = df.W.median()
print(f'Wins Median: {wins_meadian}')

# Meadian of wins (W) of the Baltimore (BAL) team until 2000
meadian_wins_baltimore_team_until_2000 = df[(
    df.Year <= 2000) & (df.Team == 'BAL')].W.median()
print(
    f'Wins Median for Baltimore team until 2000: {meadian_wins_baltimore_team_until_2000}')

#  Mode, median and mean of On-Base Percentage (OBP):
median_obp = df.OBP.median()
print(f'OBP Median: {median_obp}')

median_obp = df.OBP.mean()
print(f'OBP Mean: {median_obp}')

mode_obp = df.OBP.mode()
print(f'\nOBP Mode: {mode_obp}')

#  Mode OBP during 2010:
mode_obp_2010 = df[df.Year == 2010].OBP.mode()
print(f'OBP Mode during 2010: {mode_obp_2010}')

# ------------------------------------------------------------------------------
# (Pearson) Correlation: relationship between two variables
# the correlation coefficient is a value between -1 and 1
# 1: perfect positive correlation
# 0: no correlation
# -1: perfect negative correlation
# IMPORTANT!!!! Correlation does not imply causation
