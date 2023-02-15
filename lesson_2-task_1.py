# Lesson 2. Task 1
# Урок 2. Работа с библиотекой Pandas, часть 1. Загрузка данных и анализ их структуры
"""
1. Загрузить, просмотреть, определить количество строк и склеить 3 датасета: marketing_campaign.csv, users.csv и subscribers.csv.
2. Определить количество, типы и описательные статистики колонок (столбцов) получившегося датасета.
3. Определить эффективность маркетинговых каналов по привлечению платящих игроков.
4. Определить самую раннюю дату подписки на сервис.
5. Определить портрет аудитории удержанных подписчиков (по возрасту и языку).
Результат - ссылка на готовый ноутбук в Colab.
"""

import pandas as pd
df_market = pd.read_csv('marketing_campaign.csv')
df_market.info()
len(df_market)
df_sub = pd.read_csv('subscribers.csv')
df_sub.info()
len(df_sub)
df_users = pd.read_csv('users.csv')
df_users.info()
len(df_users)

# Объдинение датасетов
df_merged = pd.merge(df_market, df_sub)
df_merged.info()

df_merged_1 = pd.merge(df_merged, df_users)

# Определим размер датасета.
df_merged_1.info()
print('Размер датасета df_2:', df_merged_1.shape)

# Определим типы столбцов
datatypes = df_merged_1.dtypes
print(datatypes)

# Описательная статистика для нечисловых столбцов датасета
df_merged_1.describe(include=['object'])
print(df_merged_1.describe)

# Определить эффективность маркетинговых каналов по привлечению платящих игроко
df_merged_1['subscribing_channel'].value_counts()
print(df_merged_1.value_counts())

# Определить самую раннюю дату подписки на сервис
data_subscribed_first = df_merged_1.filter(items = ['date_subscribed'])
print(data_subscribed_first.head(1))

#  Определить портрет аудитории удержанных подписчиков (по возрасту и языку).
df_merged_1[df_merged_1['language_preferred'].str.contains('English|German|', case = False)].tail()

