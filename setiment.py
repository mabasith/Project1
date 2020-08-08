import pandas as pd 
import nltk
from nltk.sentiment.veder import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='data.xlsx'
xl=pd.ExcelFile(file)
dfs.xl.parse(xl.sheet_name[0])
dfs=list(dfs['Timeline'])
sid=SentimentIntensityAnalyzer()
str1=""
for data in dfs:
	a=data.find(str1)
	if a==-1:
		ss=sid.polarity_scores(data)
		print(data)
		for k in ss:
			print(k,ss[k])
