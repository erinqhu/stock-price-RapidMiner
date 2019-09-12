# Data Mining and Decision Analysis based on NYSE Data
## Project Background
* Large portion of stock investors ended the year with zero or negative return in 2014.(http://fortune.com/2015/01/06/stock-market-2014-losers)
* Stock market is considered erratic and unpredictable.
* Data mining techniques can be used to evaluate past stock prices and acquire useful knowledge through the calculation of some financial indicators.
## Business Problem to Solve
How to increase return on stock investment (ROI)
* __Identify Industry Performance:__ Conduct industry performance analysis to provide insights and clarity on hedging decisions. 
* __Rank Company Performance based on Financial Indicators:__ Identify top 10 performing companies based on fundamental indicators (financial attributes & ratios). 
* __Predict Stock Prices:__ Build  various forecasting methods to determine future price of the stock based on past trends.
## Data
`Prices.csv` Daily price information along with the opening price, closing price, low and  high price of the different stocks listed 2010-2016, broken down by ticker symbol.<br>
`Prices-split-adjusted.csv` Price information adjusted for price splits and information of the volume traded.<br>
`Securities.csv` Industry information by sector.<br>
`Fundamentals.csv` Financial performance and financial position information of different companies extracted from SEC 10K filings (2012-2016).
## Approaches
Approaches used in this project include: Linear Regression, Decision Tree, Clustering, Association Rule Mining, Moving Average, Exponential Smoothing, and Artificial neural network(ANN).
## Results
_Identify Industry Performance:_ Decision Tree approach identifies top 5 performing industies - Consumer Discretionary, Industrials, Information Technology, Health Care, and Financials.<br><br>
_Rank Company Performance:_ Association Rule Mining generates 12 rules. Following each rule, Top 11 performing companies appear most frequently: KLA-Tencor Corp., Michael Kors Holdings, Cintas Corporation, Lam Research, Rockwell Automation Inc., Snap-On Inc., AutoZone Inc., AmerisourceBergen Corp, Home Depot, Symantec Corp., and TransDigm Group.<br><br>
_Predict Stock Prices:_ Moving Average with ANN achieves 64.5% accuracy.
## Conclusion
According to the five-year return of the top 5 performing industries, the industries to Invest and manage portfolio are suggested as below:<br>
Companies/Stocks to be considered:<br>

## Limitation
* Need to create multiple models to get favorable results.
* Rapid Miner has limited operators for stock prediction and forecasting. For more accurate prediction, R and Python will have good libraries to work with.<br><br>

_Note: this is a group project for CIS9660 Data mining._
