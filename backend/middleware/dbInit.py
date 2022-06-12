import requests
import sys
import re
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo
from selenium.webdriver.chrome.options import Options
CHROMEDRIVER_PATH = "C:\\Users\\tuzoe\\Documents\\Projects\\Ecom\\chromedriver.exe"
sys.path.append(CHROMEDRIVER_PATH)

try:
    mongo = pymongo.MongoClient(host="localhost", port=27017)
    mongo.server_info()
    db = mongo.shop
    print('CONNECTED TO MONGO SERVER')
except Exception as e:
    print('Failed to connect to Server')


class ItemDetails:
    def urlToTitle(self, url):
        url = url.split('products/')[1]
        url = url[0:-1]
        temp1 = url.split('-')[1::]
        temp2 = ''
        for term in temp1:
            try:
                term1 = term[0].upper() + term[1::]
                temp2 += term1 + ' '
            except:
                pass
        return temp2

    def descriptionParser(self, txt):
        x = re.findall("LISTED.*AGO", txt)[0]
        desc = txt.split(x)[1]
        return(desc)

    def getItemDetails(self, url):
        try: 
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')  
            browser = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
            browser = webdriver.Chrome(CHROMEDRIVER_PATH)


            url = url
            browser.get(url)

            # wait for visibility of the specified element
            WebDriverWait(browser, 16).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='cookieBanner__acceptAllButton']")))

            accept_cookies_button = browser.find_element_by_xpath("//button[@data-testid='cookieBanner__acceptAllButton']")
            accept_cookies_button.click()

            desc = browser.find_element_by_xpath("//div[@data-testid='product__details']")

            strDesc = desc.text
            browser.execute_script("document.body.style.zoom='25%'")

            ''' 
            EXAMPLE OF RESPONSE
            ////////////////////////////////////////////////////////////
            Vintage 90s Lions Football large print graphic tee shirt.

            See photo 3 for minor stain on the back of shirt.

            Shipping is $5. Same/Next day dispatch!
            Men's M. Model is 5'8” 140lbs.
            DM for measurements and questions!

            #graphictee #sports #indie #cute #vintage
            10% off10% off
            Price
            US$25.00US$22.50
            Size M
            Brand Fruit of the Loom
            Condition Used - Good
            Style Streetwear, Sportswear, Indie, 90s, Vintage, Preloved
            Colour Grey, Navy
            LISTED 1 HOUR AGO
            ///////////////////////////////////////////////////////////////
            '''
            #try to standardize this data ^^
            itemDetails = {

            }
            itemDetails['ItemUrl'] = url
            itemDetails['Title'] = self.urlToTitle(url)
            descripton = strDesc.split('Price')[0] 
            if len(descripton) == 0:
                descripton = self.descriptionParser(strDesc)

            itemDetails['Description'] = descripton

            stdData = strDesc.split('Price')[1].split('LISTED')[0][0:-1]

            price = ["Price"]
            stdData2 = price + stdData.split('\n')[1::]

            for item in stdData2:
                if 'Size ' in item:
                    itemDetails['Size'] = item.split('Size ')[1]
                if 'Brand ' in item:
                    itemDetails['Brand'] = item.split('Brand ')[1]
                if 'Condition ' in item:
                    itemDetails['Condition'] = item.split('Condition ')[1]
                if 'Style ' in item:
                    itemDetails['Style'] = item.split('Style ')[1].split(', ')
                if 'Colour ' in item:
                    itemDetails['Colour'] = item.split('Colour ')[1].split(', ')
                if 'Color ' in item:
                    itemDetails['Color'] = item.split('Color ')[1].split(', ')

            priceDetails = stdData2[1]
            temp1 = priceDetails.split('US$')[1::]
            if len(temp1) > 1:
                itemDetails['OriginalPrice'] = temp1[0]
                itemDetails['DiscountedPrice'] = temp1[1]
            else:
                itemDetails['OriginalPrice'] = temp1[0]

            picsContainer = browser.find_element_by_xpath("//div[@data-testid='product__images']")

            pics = picsContainer.find_elements_by_tag_name("img")

            listOfPics = []
            for pic in pics:
                listOfPics.append(pic.get_attribute("src"))

            itemDetails['Images'] = listOfPics
            browser.close()
            return itemDetails
        except TimeoutException as e:
            print(e)
            browser.close()


req = requests.get("https://webapi.depop.com/api/v1/shop/29188092/filteredProducts/selling?limit=50")
products = req.json()['products']

latest_200_product_links = []
for productObject in products:
    latest_200_product_links.append("https://www.depop.com/products/" + productObject['slug'])


productDetails = []  
for link in latest_200_product_links:
    client = ItemDetails()
    productDetails.append(client.getItemDetails(link))


data = {"data": productDetails}

dbResponse = db['Data'].insert_one(data)