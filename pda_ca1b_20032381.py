# -*- coding: utf-8 -*-
"""PDA_CA1B_20032381.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JR39HJUaNh3xPHB5I5gChwybzA8JrL95
"""



"""# Data Acquisition
From Asos website https://www.asos.com/search/?q=shoes&page=2


"""



# Loading libraries
import requests
import json
import pandas as pd

# Fetching data from api
url = 'https://www.asos.com/api/product/search/v2/?offset=72&includeNonPurchasableTypes=restocking&q=shoes&store=ROW&lang=en-GB&currency=EUR&rowlength=3&channel=desktop-web&country=IE&keyStoreDataversion=mhabj1f-41&limit=72'

data = "offset=72&includeNonPurchasableTypes=restocking&q=shoes&store=ROW&lang=en-GB&currency=EUR&rowlength=3&channel=desktop-web&country=IE&keyStoreDataversion=mhabj1f-41&limit=72"

headers = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate',
'accept-language': 'en-US,en;q=0.9,mr;q=0.8',
'asos-c-name': '@asosteam/asos-web-product-listing-page',
'asos-c-plat': 'web',
'asos-c-ver': '1.2.0-c3dbfdf8-90',
'asos-cid': '80540303-1bdf-4ce4-858b-507804cdeaae',
'cookie': 'browseCountry=IE; browseCurrency=EUR; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=ROW; currency=19; s_ecid=MCMID%7C38755829175050667370808691236603999908; featuresId=b94616f7-e6bc-494b-bdf9-b049c11b8c86; _cs_c=0; _ga=GA1.1.1162803615.1729159158; FPID=FPID2.2.2ZZH%2BZ21wBraZ99X1PMEIYELCX4rSS0vmhM65Pt3QMQ%3D.1729159158; OptanonAlertBoxClosed=2024-10-17T09:59:21.427Z; eupubconsent-v2=CQGorZgQGorZgAcABBENBLF8AP_gAEPgAAYgKfwEwAMAB3AD4AJsAfoBRQEIAImATYApcBTYC8wGXAPrAjYBL8CekFMgU0gpsCn4KeQDAA-AD9AQgAiYBTYC8wGXAPrAnoBTICmoFPAAAAAA.f_wACHwAAAAA; OTAdditionalConsentString=1~230.318.540.737.1040.1166.1227.1548.1638.1651.1677.1703.1721.1765.1782.1786.1832.1917.1944.1987.2008.2039.2107.2140.2150.2177.2219.2292.2305.2312.2331.2370.2377.2387.2461.2493.2501.2535.2567.2569.2604.2612.2614.2643.2645.2650.2651.2784.2875.2898.2908.2920.3012.3017.3018.3048.3055.3112.3173.3185.3223.3227.3235.3293.3306.3309.3315.3328.3331.3731.8931.9731.13731.16931.27831.31631.32531.33631.34231.34631; _gcl_au=1.1.948985723.1729159162; bt_stdstatus=NOTSTUDENT; FPAU=1.1.948985723.1729159162; stc-welcome-message=cappedPageCount=2; optimizelyEndUserId=oeu1729159168655r0.4816726432835303; plp_columsCount=threeColumns; asosAffiliate=affiliateId=17295; bt_utmSource=organic_search; floor=1000; asos=currencyid=19&currencylabel=EUR&topcatid=1000; __gads=ID=b12012a37492e92e:T=1729176769:RT=1729198086:S=ALNI_MZUdWtju9FoNqddHvaLUTWbfABcgA; __eoi=ID=cb1e562e7046cd13:T=1729176769:RT=1729198086:S=AA-AfjajBVY3umTK17MsmT6Hjmnn; geocountry=IE; asos_drmlp=b9902a1be2e5955ccb96c6f8cc0f1a27; _abck=E7378A7A400E7514C3C01C066CEDB7B0~0~YAAQDWJkX24QjpmSAQAA7K1onwwo880808KvXSmAOy4crkKGB5wsupQHO+ONkNPtRPwXDH6zpJcUwPVAHFYTzsQBmC778tZt2Phv7a96vIHvuCLlcTxRr5O65cHxKJ86B36iRI+A92Utm7deuNod8TFnRFhaYqGzniCiVHpZU/MtY1qCQBoTYOcnWer4OFP59TJybLvPpp7r4PfdhYH7OBkRzYZ+GMI1gUQ3TgAiHrn5J0aTkucX8aSJ+9y/h8WrTHTkT5dTGN8BW/aM+VPkHhKEResKGsb9DTlS9no6hgR8NZ33HkdR37cjDPslrMriQxFgjdavulnjZIfWbpECeblsEn93YxqbCZ6yN/9cBOiAzUONImb1fWUyVV3lKFFVpdC+M7TGsgBL+mRguphBfSHw4nb/E+dX4SC9Rt8Oym+MGIes30+dgFTApL0S+oFIeYlyYYc/6r/0NraDlgX2Z9aKdktuAgiDfUEICiot~-1~-1~-1; siteChromeVersion=au=13&com=13&de=13&dk=13&es=13&fr=13&it=13&nl=13&pl=13&roe=13&row=13&ru=13&se=13&us=13; keyStoreDataversion=mhabj1f-41; asos-anon12=01929f68c13679978e5d59390dcbadc9; asos-ts121=01929f68-c139-71db-9acd-a4a334d2a609; asos-b-sdv629=mhabj1f-41; ak_bmsc=78BF77585004AEFC764EA6D7D5D6ABC3~000000000000000000000000000000~YAAQDWJkXwkSjpmSAQAAdMJonxnXN4ixr8Pid5Fplp9XI4tQkgY+Faenh0sL7blPo6E85w3XcUp1gj7Dres0yE5JlVkefeKRC2Nrdrxw47fYH31qpgRrWXXrrtRIQIIKybb5hE6/2F7fC8L7dJKZEzH8dT3cNP1Bl2dqK3zZ4tIowqulH/SObJm0khxNh30+hQX9b6yKaMTy7rzXs/ZCu0usWzHBfq+HwEr0hg2YaRLKdCApkqEa/iDs6jn+vMeOO8m+KrIGMZRCgxEPeiB5/zZEANirI26zm9zS7ClNm69Jp99p/mtvWirkobWX2d/UAM73L9O/Va69knsMp0/w1QAvBPkFo+s0MTFe0ULIeUD49IIw03foSCHEkc+xA0qrkfIRx8CPVzo=; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCMID%7C38755829175050667370808691236603999908%7CMCAAMLH-1729856096%7C6%7CMCAAMB-1729856096%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C0%7CMCOPTOUT-1729258496s%7CNONE%7CvVersion%7C3.3.0%7CMCAID%7CNONE; _s_fpv=true; s_cc=true; _cs_mk_aa=0.964717105377318_1729251299722; FPLC=A9CfJ6yAUKd153YcwjBtinSYlVW6LMY4GVI4t%2F0sz%2BLjnNcf3%2F%2BeIQqBK4E6gvRkGr%2BUKIJd5BAP6GqfYK05WBH9c%2FVqYgwPa71xGu1MZSmlnuJGBB8BmVkkIVag4g%3D%3D; FPGSID=1.1729251305.1729251305.G-H5HS29D9X2.evHmdTGbv_tQ2dI-TFtFfA; bm_sz=D1B4BED66DFC11B3957D1C409A345A65~YAAQDWJkX3AUjpmSAQAA5+honxlZzQR7l1SFV4z8MVrowgTEf6qIHKYCwJK2M6hsdZA8VhLuSb0ZnomAXbRMrj36RFVo21lsY+04RNjHdgthallTb3mMvc4WcxsI6dxk6b5AhF7Gm1E3egBeZCfzFM8VImQGcbBLLgMdHKV1AjKlKhTvfC1e823LCsTQahZZDoQq98skqH6mphmDWH5MLz/E765XSmBwfMBdfJngIN7j6jjUM9UjMlTWVzC+4RVmytGjh2uBJhaE+xpoCQ6TR8t3/aOJaz0IpsrahkKlQrZ45q6tA6T5xy0bOftpR5Ts0CwSdO/VnXwzfJr+LX3zB9WuRVss0vJynhhUpMYAS+kcQJnQ6SEjr1a44vavitylknGp6vvTXIJTFQpHASimjhSjR6dYuC4=~4405554~3356995; s_pers=%20s_vnum%3D1730419200098%2526vn%253D5%7C1730419200098%3B%20gpv_p6%3D%2520%7C1729253095588%3B%20eVar225%3D2%7C1729253108021%3B%20visitCount%3D5%7C1729253108024%3B%20gpv_e231%3D37dbcc1b-8db1-4021-bc6c-e91a182da8c1%7C1729253110109%3B%20s_invisit%3Dtrue%7C1729253110122%3B%20s_nr%3D1729251310124-Repeat%7C1760787310124%3B%20gpv_e47%3Dno%2520value%7C1729253110125%3B%20gpv_e198%3Db94616f7-e6bc-494b-bdf9-b049c11b8c86%7C1729253110128%3B%20gpv_p10%3Ddesktop%2520row%257Csearch%2520page%257Csuccessful%2520search%7C1729253110130%3B; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+18+2024+12%3A35%3A13+GMT%2B0100+(British+Summer+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=63e0b9ad-12f3-4fbb-9935-c449c1bf602f&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0003%3A1%2CV2STACK42%3A1&geolocation=IE%3BL&AwaitingReconsent=false; _cs_id=17344412-4686-a315-9017-20855ca2eab2.1729159157.6.1729251313.1729251301.1628755191.1763323157066; _cs_s=2.0.0.1729253113413; _ga_H5HS29D9X2=GS1.1.1729251304.7.1.1729251315.60.0.1758779314; RT="z=1&dm=asos.com&si=5bed0991-c094-4c6e-8eb1-e051972da74d&ss=m2enkipi&sl=3&tt=93r&bcn=%2F%2F684dd32a.akstat.io%2F&ld=kpp&nu=370qxwu5&cl=tzf"; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520row%25257Csearch%252520page%25257Csuccessful%252520search%2526link%253DLOAD%252520MORE%2526region%253Dplp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c',
'priority': 'u=1, i',
'referer': 'https://www.asos.com/search/?q=shoes&page=2',
'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

r = requests.get(url, data=data, headers=headers)

r

r.content

j=json.loads(r.content)
# json = data is same as data=json.dumps(data)
# data = data means json = json.loads(data)

j.keys()

pd.json_normalize(j['products'])

"""# Features Extraction
asos_df consists 32 columns/features.
Out of this, key features can be extracted for further analysis.
"""

asos_df = pd.json_normalize(j['products'])
print('Data types of each feature of asos_df\n',asos_df.dtypes)

# Removing additional unnecessary features
#asos_df = asos_df.drop(columns = 'facetGroupings') #Empty data
asos_df = asos_df.drop(['additionalImageUrls','facetGroupings'], axis=1) #Empty data

for i in asos_df.columns:
  print('Length of unique values in',i, 'is',len(asos_df[i].unique()))

# asos_df = asos_df.drop(['colour','hasVariantColours', 'hasMultiplePrices', 'groupId','productType'], axis=1) #Empty or only unique data
# asos_df

# Selecting key features from asos_df, neglecting empty, irrelavant and repetitive features
key_features = asos_df[['id','name','colourWayId','brandName','productCode','isSellingFast','price.current.value','price.previous.value','price.lowestPriceInLast30Days.value','price.isMarkedDown','price.currency']]
key_features.rename(columns={
    'isSellingFast': 'sellingIsFast',
    'price.current.value': 'currentPrice',
    'price.previous.value': 'previousPrice',
    'price.lowestPriceInLast30Days.value': 'lowestPriceInLast30Days',
    'price.isMarkedDown': 'priceIsMarkedDown',
    'price.currency': 'currency'
}, inplace=True)
key_features

"""# Data Transformation"""

# Checking null vaules in selected features table
null_count = key_features.isnull().sum()
print('Null values in the each feature:\n',null_count)

"""Features **'previousPrice'** and **'lowestPriceInLast30Days'** shows NAN values only when the feature **'priceIsMarkedDown'** is False. If **'priceIsMarkedDown'** is True then above two features are filled with their respective values. This observation concludes that as price value non changed these values assigned with NAN.

Logically, **'currentPrice'** can be copied to **'previousPrice'** and **'lowestPriceInLast30Days'** wherever NAN assigned.
"""

key_features['previousPrice'].fillna(key_features['currentPrice'], inplace=True)
key_features['lowestPriceInLast30Days'].fillna(key_features['currentPrice'], inplace=True)

# Checking null vaules in selected features table after clean up
null_count = key_features.isnull().sum()
print('Null values in the each feature:\n',null_count)

# Data after replacing NAN values
key_features

"""Visualization of features."""

# Plotting pie chart for brand name.
# key_features['brandName'].value_counts()
import matplotlib.pyplot as plt
import seaborn as sns
key_features['brandName'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(8,8))
plt.title('Distribution of Brand name')
plt.ylabel('')
plt.show()

# Encoded the brandName
# key_features['brandName_encoded'] = pd.Categorical(key_features['brandName']).codes

# Plotting bar chart for 'priceIsMarkedDown'

sns.countplot(x='priceIsMarkedDown', data=key_features)
#plt.xticks(rotation=30)
plt.title('Distribution of priceIsMarkedDown')
plt.grid(axis='y')
plt.show()
# key_features['priceIsMarkedDown'].value_counts()

# Converting this boolean feature into binary integers.
# key_features['priceIsMarkedDown'] = key_features['priceIsMarkedDown'].astype(int)

# Plotting bar chart for 'sellingIsFast'
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x='sellingIsFast', data=key_features)
#plt.xticks(rotation=30)
plt.title('Distribution of sellingIsFast')
plt.grid(axis='y')
plt.show()


# Converting this boolean feature into binary integers.
# key_features['sellingIsFast'] = key_features['sellingIsFast'].astype(int)

# Plotting boxplot for currentPrice
sns.boxplot(x=key_features['currentPrice'])
plt.title('Boxplot of currentPrice')
plt.show()
# Outliers observed on positive side of boxplot.

#min(key_features['currentPrice'])
#key_features['currentPrice'].median()

# Adding new feature: Price Range Indicator
A = key_features['currentPrice'].quantile(0.25)
B = key_features['currentPrice'].quantile(0.75)
C = key_features['currentPrice'].quantile(0.75)+1.5*(key_features['currentPrice'].quantile(0.75)-key_features['currentPrice'].quantile(0.25))
D = max(key_features['currentPrice'])
key_features['price_range_indicator'] = pd.cut(key_features['currentPrice'], bins=[0, A, B, C, D], labels=['Low', 'Medium', 'High', 'Very High'])

# Adding new feature; Discount percentage in %.
key_features['discount_percentage'] = ((key_features['previousPrice'])-(key_features['currentPrice']))/(key_features['previousPrice'])*100
key_features['discount_percentage'] = key_features['discount_percentage'].round(1)
key_features['discount_percentage'] = key_features['discount_percentage'].fillna(0).clip(lower=0)

# Adding new feature; Lowest price tag: It will show up to customer only if it is True
key_features['lowest_price_tag'] = key_features['currentPrice'] == key_features['lowestPriceInLast30Days']

# Data after encoding and adding new features
key_features

"""# Loading Data"""

import sqlite3
connection = sqlite3.connect('asos.db', check_same_thread=False)
key_features.to_sql('asos_data', connection, if_exists='append', index=False)
cursor = connection.cursor()

cursor.execute("SELECT * FROM asos_data")
rows = cursor.fetchall()
rows

#!pip install Flask

from flask import Flask
from flask import render_template
from flask import request
# !pip install flask_cors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/home.html") # Default-show data
def home():
    return render_template("home.html")

@app.route("/addShoes", methods=['GET','POST']) # Add shoes
def addShoes():
  if request.method == 'POST':
    Id = request.form['id']
    name = request.form['name']
    colourWayId = request.form['colourWayId']
    brandName = request.form['brandName']
    productCode = request.form['productCode']
    sellingIsFast = request.form['sellingIsFast']
    currentPrice = request.form['currentPrice']
    previousPrice = request.form['previousPrice']
    lowestPriceInLast30Days = request.form['lowestPriceInLast30Days']
    priceIsMarkedDown = request.form['priceIsMarkedDown']
    currency = request.form['currency']
    #brandName_encoded = request.form['brandName_encoded']
    brandName = request.form['brandName']
    price_range_indicator = request.form['price_range_indicator']
    discount_percentage = request.form['discount_percentage']
    lowest_price_tag = request.form['lowest_price_tag']
    print(name,colourWayId,brandName,productCode,sellingIsFast,currentPrice,previousPrice,lowestPriceInLast30Days,priceIsMarkedDown,currency,brandName_encoded,price_range_indicator,discount_percentage,lowest_price_tag)
    #print(name,colourWayId)
    cursor = connection.cursor() #create a connection to the SQL instance
    #s='''INSERT INTO asos_data(name, colourWayId, brandName, productCode, sellingIsFast, currentPrice, previousPrice, lowestPriceInLast30Days, priceIsMarkedDown, currency, brandName_encoded, price_range_indicator, discount_percentage, lowest_price_tag) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(name, colourWayId, brandName, productCode, sellingIsFast, currentPrice, previousPrice, lowestPriceInLast30Days, priceIsMarkedDown, currency, brandName_encoded, price_range_indicator, discount_percentage, lowest_price_tag)
    s='''INSERT INTO asos_data(Id, name, colourWayId, brandName, productCode, sellingIsFast, currentPrice, previousPrice, lowestPriceInLast30Days, priceIsMarkedDown, currency, brandName_encoded, price_range_indicator, discount_percentage, lowest_price_tag) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(Id, name, colourWayId, brandName, productCode, sellingIsFast, currentPrice, previousPrice, lowestPriceInLast30Days, priceIsMarkedDown, currency, brandName_encoded, price_range_indicator, discount_percentage, lowest_price_tag)
    app.logger.info(s)
    cursor.execute(s)
    connection.commit()
    app.config['DEBUG'] = True

  else:
    return render_template('addShoes.html')
  return '{"Result":"Success"}'

@app.route("/getShoes", methods=['GET']) #Get Shoes
def get():
  cursor.execute("SELECT * FROM asos_data")
  rows = cursor.fetchall()
  Results=[]
  for row in rows: #Format the Output Results and get to return string
    Result={}
    Result['id']=row[0]
    Result['name']=row[1]
    Result['colourWayId']=row[2]
    Result['brandName']=row[3]
    Result['productCode']=row[4]
    Result['sellingIsFast']=row[5]
    Result['currentPrice']=row[6]
    Result['previousPrice']=row[7]
    Result['lowestPriceInLast30Days']=row[8]
    Result['priceIsMarkedDown']=row[9]
    Result['currency']=row[10]
    #Result['brandName_encoded']=row[11]
    Result['brandName']=row[11]
    Result['price_range_indicator']=row[12]
    Result['discount_percentage']=row[13]
    Result['lowest_price_tag']=row[14]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format

if __name__ == "__main__":
  #app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
  #app.run(host='0.0.0.0',port='5000', debug=True) #Run the flask app at port 8080
