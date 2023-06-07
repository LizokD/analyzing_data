import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv('WHO-COVID-19-global-data.csv', index_col=0)
df_sk = df[df['Country_code'] == 'SK']
df_cz = df[df['Country_code'] == 'CZ']
ds_sk = df_sk['New_cases']
ds_cz = df_cz['New_cases']

print(df)
print(df.columns)

correl = ds_sk.corr(ds_cz)
correlp = stats.pearsonr(ds_sk, ds_cz)

print(correl) #0.8345465968195168 - wysoka korelacja
print('Korelacja Pearsona', correl)
print('P-value', correlp[1])

if correl == correlp[0] and correlp[1] < 0.05:
    print('Korelacja jest istotna statystycznie')
else:
    print('Korelacja nie jest istotna statystycznie')

plt.plot(ds_cz, color = 'grey', linewidth = 0.6, label = "Czechy")
plt.plot(ds_sk, color = 'black', linewidth = 0.6, label = "Słowacja")
plt.xticks(['2020-01-03', '2021-01-01', '2022-01-01', '2022-01-01'], [2020, 2021, 2022, 2023])
plt.legend()
plt.grid()
plt.title('Liczba nowych przypadków COVID-19')
plt.show()

plt.scatter(ds_sk, ds_cz, c = 'black', s = 5)
plt.xlabel("Slowacja")
plt.ylabel("Czechy")
plt.title('Korelogram liczby nowych przypadków COVID-1')
plt.show()