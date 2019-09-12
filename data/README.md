# Data Description
| Dataset                   | # of Records   | # of Attributes   |
|:--------------------------|:--------------:|:-----------------:|
| prices.csv                | 851,264        | 7                 |
| prices-split-adjusted.csv | 1,036,531      | 7                 |
| securities.csv            | 505            | 8                 |
| fundamentals.csv          | 1,781          | 78                |

![](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/num_companies_bySector.png)
# Challenges with datasets
* Huge amount of data
* Tons of attributes in data sets
* Wide-ranging and unbiased data sets
# Data Preprocessing
Replace missing values, change data type, and reduce attributes.<br><br>

Final attributes are selected by experienced professionals based on how much an attribute will affect the stock price:<br>
_EPS, Year End, After Tax ROE, Current Ratio, Earnings Before Interest and Tax, Gross Margin,
Gross Profit, Net Income Applicable to Common Shareholders, Profit Margin, Quick Ratio,
Asset TO Ratio, Retained Earnings, Total Assets, Total Equity, Total Liabilities, Total Revenue	,
Estimated Shares Outstanding, GICS Sector, GICS Sub Industry, Ticker Symbol_<br><br>

_Clean and merge process_
![clean and merge](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/clean_and_merge%20process.JPG)

_Replace missing values with zeros_
![data info](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/data_infor.png)
![replace_missing](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/replace_missing.png)
![replace_missing_param](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/replace_missing_param.png)

_Change data type for Decision Tree_
![change_type](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/replace_missing.png)
![change_type_param](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/change_type_param.png)

_Select attributes_
![select_attributes](https://github.com/erinqhu/stock-price-RapidMiner/blob/master/data/select_attributes.png)
