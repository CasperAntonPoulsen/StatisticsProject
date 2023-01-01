from sklearn.base import BaseEstimator, TransformerMixin
import math
import pandas as pd

class WindVectorTransformer(BaseEstimator, TransformerMixin):
	def __init__(self):
		self.directions =  ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
		self.md_dict = {}
		for i in range(len(self.directions)):
			md = 270 - (i*22.5)
			if md < 0:
				md += 360
			self.md_dict[self.directions[i]]=md

	def calculate_u(self, wwd, ws):
		return ws*math.cos(self.md_dict[wwd])

	def calculate_v(self, wwd, ws):
		return ws*math.sin(self.md_dict[wwd])

	def transform(self, X, y = None):
		X_ = X
		rows = []
		for index, row in X_.iterrows():
			vector = [self.calculate_u(row["Direction"],row["Speed"]),
					  self.calculate_v(row["Direction"],row["Speed"])]
			rows.append(pd.DataFrame.from_dict({index:vector},columns=["u","v"],orient="index"))

		return pd.concat(rows)

	def fit(self, X, y = None):
		return self


class WindDegreeTransformer(BaseEstimator, TransformerMixin):
	def __init__(self):
		self.directions =  ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
		self.md_dict = {}
		for i in range(len(self.directions)):
			md = 270 - (i*22.5)
			if md < 0:
				md += 360
			self.md_dict[self.directions[i]]=md

	def transform(self, X, y = None):
		return X["Direction"].apply(lambda x: self.md_dict[x])

	def fit(self, X, y = None):
		return self