# %%
import pandas as pd
import seaborn as sb

# %%
# source = https://www.kaggle.com/sudalairajkumar/covid19-in-india?select=covid_vaccine_statewise.csv
data = pd.read_csv('covid_vaccine_statewise.csv')

# %%
data.head()

# %%
data.describe()

# %%
data.info()

# %%
data.groupby('State')['First Dose Administered'].sum()

# %%
data.groupby('State')['Second Dose Administered'].sum()

# %%
FirstDoseData = data.groupby('State')['First Dose Administered'].sum()

# %%
FirstDoseData.drop('India', inplace=True)

# %%
FirstDoseData.plot(kind='bar')

# %%
SecondDoseData = data.groupby('State')['Second Dose Administered'].sum()

# %%
SecondDoseData.drop('India', inplace=True)
SecondDoseData.plot(kind='bar')

# %%
MalesVaccinated = data[['State', 'Male (Doses Administered)']].groupby(
    'State').sum()

# %%
MalesVaccinated

# %%
FemalesVaccinated = data[['State', 'Female (Doses Administered)']].groupby(
    'State').sum()

# %%
FemalesVaccinated

# %%
MalesVaccinated.drop('India', inplace=True)
MalesVaccinated.plot(kind='bar')

# %%
FemalesVaccinated.drop('India', inplace=True)
FemalesVaccinated.plot(kind='bar')
