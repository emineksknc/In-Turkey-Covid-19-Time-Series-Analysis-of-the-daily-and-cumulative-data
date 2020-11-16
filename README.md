# In-Turkey-Covid-19-Time-Series-Analysis-of-the-daily-and-cumulative-data

Installation 
 conda install -c conda-forge fbprophet

Verisetinin görselleştirilmesi.py
Kümülatif değerleri görselleştirmek için:
data =[ df['Confirmed'],df['Deaths'],df['Recovered']] kullanılmalıdır.
Günlük değerleri görselleştirmek için:
data =[ df['Daily_Confirmed'],df['Daily_Deaths'],df['Daily_Recovered']] kullanılmalıdır.

Prophet ile Zaman Serisi Analizleri.py
Kümülatif değerler için zaman serisi analizleri için:
df = data.loc[:, ["Last_Update"," Recovered veya Confirmed veya Deaths"]]
df = df.rename(columns={'Last_Update': 'ds',
                        ' Recovered veya Confirmed veya Deaths: 'y'}) kullanılmalıdır.

Günlük değerler için zaman serisi analizleri için:
df = data.loc[:, ["Last_Update"," Daily_Recovered veya Daily_Confirmed veya Daily_Deaths"]]
df = df.rename(columns={'Last_Update': 'ds',
                        ' Daily_Recovered veya Daily_Confirmed veya Daily_Deaths: 'y'}) kullanılmalıdır.


Dataset
https://www.kaggle.com/gkhan496/covid19-in-turkey


