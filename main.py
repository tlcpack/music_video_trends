from pytrends.request import TrendReq
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["music video", "mv"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='youtube')

df_queries = pytrends.related_queries()

top_music_video = df_queries.get("music video").get("top")
top_mv = df_queries.get("mv").get("top")
df_top = pd.concat([top_music_video, top_mv])

# df_top.sort_values(['value'], ascending = False).head(5).reset_index(drop=True)

rising_music_video = df_queries.get("music video").get("rising")
rising_mv = df_queries.get("mv").get("rising")
df_rising = pd.concat([rising_music_video, rising_mv])

# df_rising.sort_values(['value'], ascending = False).head(5)

kw_list = ["Gacha Life", "Dynamite", "Blackpink", "BTS"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='youtube')
df_interest = pytrends.interest_over_time().drop(columns='isPartial')

plt.figure(figsize=(16,8))
plt.xticks(rotation=45)
sns.set(style="darkgrid", palette = 'rocket')
ax = sns.lineplot(data=df_interest)
ax.set_title('Music video trends over time', fontsize=20)