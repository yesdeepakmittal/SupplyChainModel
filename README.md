# Supply Chain Maturity Model using Machine Learning
Supply Chain Maturity model is the implementation of machine learning and data science to analyze the business data. In this project, we incorporated the unstructured data and transformed it into facts and figures.

## How to get started?
- Make a [virtual Environment](https://gist.github.com/yesdeepakmittal/61494217c8be4a7e61524e27824943bd) and activate it
- `git clone https://github.com/yesdeepakmittal/SupplyChainModel`
- `cd SupplyChainModel`
- `pip install -r requirements.txt`
- `python index.py`
- run your application in browser `http://127.0.0.1:8050/`


## Overview

<div align="center">
  <img src="https://github.com/yesdeepakmittal/SupplyChainModel/blob/main/assets/home.png" width="800" title="feedback page" alt="feedback page"><br>
  <img src="https://github.com/yesdeepakmittal/SupplyChainModel/blob/main/assets/location.png" width="600" title="location" alt="location"><br>
  <img src="https://github.com/yesdeepakmittal/SupplyChainModel/blob/main/assets/social%20media.png" width="600" title="social media" alt="social media"><br>
  <img src="https://github.com/yesdeepakmittal/SupplyChainModel/blob/main/assets/data%20model.png" width="600" title="data model" alt="data model"><br>
  <img src="https://github.com/yesdeepakmittal/SupplyChainModel/blob/main/assets/macroeconomic_indicator.png" width="600" title="india inflation" alt="india inflation"><br>
  <img src="https://github.com/yesdeepakmittal/SupplyChainModel/blob/main/assets/world%20inflation.png" width="600" title="world inflation" alt="world inflation"><br>
  </div>
</div>


##  Data Source
- Data need to fetch from DB as well as from other sources by running below mentioned Python scripts. 
- Run `data.py`, `db.py`, `macroeconomic_indicator.py`,`sentiment.py`,`twitter.py` stored in data folder. 
- You can write another script to run all these function simultaneously and add a button on the dashboard.
- Make sure to add your DB crediential in the `db.py` file if you are using remote database and twitter secrets in twitter.py


## References
- https://pythonprogramming.net/
- https://www.youtube.com/user/sentdex
- https://www.coursera.org/learn/social-media-data-analytics
