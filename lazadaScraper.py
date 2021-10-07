from re import I, S
from sys import version
from bs4 import BeautifulSoup
import requests
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# LAZADA SCRIPT................................................................
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait



main_list = []
# main_url = "https://www.lazada.sg/products/i-love-taimei-popcorn-chicken-with-flavor-top-up-redeem-in-storetakeaway-i641996874-s1933390719.html?spm=a2o42.home.flashSale.2.654346b5GZj9bn&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.0%3Babid%3A238030%3Bitem_id%3A641996874%3Bpvid%3Aeeef434d-030c-4593-b43b-117030ae2fb6%3Bmt%3Ahot%3Bdata_type%3Aflashsale%3Bscm%3A1007.17760.238030.%3Bchannel_id%3A0000%3Bcampaign_id%3A139794&scm=1007.17760.238030.0"
# main_url = "https://www.lazada.com.my/products/available-in-malaysiathe-lowest-pricewomens-new-korean-version-of-the-wild-korean-version-of-mickey-short-neck-collar-bottom-half-sleeve-t-shirt-i1069356480-s10021963397.html?"
# main_url = "https://www.lazada.com.my/products/body-glove-mens-basic-tee-yellow-i2267532667-s9627276120.html?"
# main_url  = "https://www.lazada.sg/products/180x80cm-women-crimp-crinkle-muslim-hijabs-shawls-solid-cotton-scarves-wrinkle-plain-islamic-pashmina-wraps-stole-katun-scarf-wj163-i643400592-s1939208159.html"
# main_url = "https://www.lazada.sg/products/huawei-honor-50-honor-50-pro-honor-50-se-108mp-100w-new-original-better-than-honor-40-i1824843841-s9899678070.html?spm=a2o42.searchlistcategory.list.87.129a3f03lqy1Xl&search=1&freeshipping=1"
main_url = "https://www.lazada.sg/products/i-love-taimei-popcorn-chicken-with-flavor-top-up-redeem-in-storetakeaway-i641996874-s1933390719.html?spm=a2o42.home.flashSale.2.654346b5GZj9bn&search=1&mp=1&c=fs&clickTrackInfo=rs%3A0.0%3Babid%3A238030%3Bitem_id%3A641996874%3Bpvid%3Aeeef434d-030c-4593-b43b-117030ae2fb6%3Bmt%3Ahot%3Bdata_type%3Aflashsale%3Bscm%3A1007.17760.238030.%3Bchannel_id%3A0000%3Bcampaign_id%3A139794&scm=1007.17760.238030.0"




item_id = main_url.split('-s')[-1]
# print(item_id)
item_id = item_id.split('.')
item_id = item_id[0]
# print(item_id)
item_id = item_id
print(item_id)
item_id = int(item_id)

driver = webdriver.Chrome()
driver.get(main_url)
time.sleep(2)




try:
    popup = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/span')
    popup.click()
    time.sleep(2)
except:
    pass

name  = driver.find_element_by_class_name("pdp-mod-product-badge-wrapper").text

try:
    rating = driver.find_element_by_class_name("score-average").text
    rating = float(rating)
except:
    try:
        rating = driver.find_element_by_xpath('//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/span[1]').text
        rating = float(rating)                                    
    except:
        try:
            rating = driver.find_element_by_css_selector('.score.score-average').text
            rating = float(rating)
        except:
            rating = "Not Found"
            
try:
    rating_count = driver.find_element_by_class_name("pdp-review-summary__link").text
    rating_count = rating_count.split(" ")[0]
    rating_count = int(rating_count)
except:
    rating_count = "Not Found"

print(rating_count,rating,name)



mains = driver.find_elements_by_css_selector(".sku-prop-selection")
imgss = []
try:
    for x in range(1,11):
        img = driver.find_element_by_xpath(f'//*[@id="module_item_gallery_1"]/div/div[2]/div/div[1]/div/div[{x}]/div/img')
        temp = img.get_attribute('src')
        temp = temp.replace('120x120','720x720')
        imgss.append(temp)
except:
    pass
print(imgss)

# hh = mains[0]
# kks = driver.find_elements_by_css_selector(".sku-variable-img-wrap")
# lable1 = len(kks)+1
# ss = mains[1]
# kkkg = driver.find_elements_by_css_selector(".sku-variable-size")
# lable2 = len(kkkg)+1
try:
    variant_n = driver.find_element_by_xpath('//*[@id="module_sku-select"]/div/div[1]/div/h6').text
    variant_n = variant_n.split(' ')[0]
    variant_n = variant_n.lower() 
except:
    variant_n = "size"
# print(variant_n)
try:
    variant_s = driver.find_element_by_xpath('//*[@id="module_sku-select"]/div/div[2]/div/h6').text
    variant_s = variant_s.split(' ')[0]
    variant_s = variant_s.lower() 
except:
    variant_s = "color"
# print(variant_s)
two_f = []
two_s = []
vatiants =  []

try:
    kks = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[1]')
    is_down = "sku-variable-img-wrap-selected" in kks.get_attribute("class")
    print(is_down)
    if is_down == False:
        kks.click()
except:
    pass
try:
    size  = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[2]/div/div/div[2]/span[1]')
    is_kk = "sku-variable-img-wrap-selected" in size.get_attribute("class")
    print(is_down)
    if is_kk == False:
        size.click()
except:
    pass



try:
    for x in range(1,15):                           
        hhsd = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[{x}]')
        hhsd.click()      
        time.sleep(2)   
        try:
            is_down = "sku-variable-img-wrap-selected" in hhsd.get_attribute("class")
            print(is_down)
        except:
            print("jjs") 
      
                                   
        driver.execute_script("window.stop()")
        try:
            is_main = "sku-variable-img-wrap-disabled" in hhsd.get_attribute("class")
            print(is_main)
        except:
            print("jjs")
        # try:
        #     jsh = driver.find_element_by_xpath('//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[1]/span')
        #     hhsd = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[{x}]/div/div/img')
        # except:
        #     hhsd = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[{x}]/div/div/img').click()
        
        # ssd = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[{x}]/span')
        namer = driver.find_element_by_xpath('//*[@id="module_sku-select"]/div/div[1]/div/div/div[1]/span').text
        
        # print(namer)
        two_f.append(namer)
        time.sleep(1)
        
       
        
        try:
            for y in range(1,15):
                size  = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[2]/div/div/div[2]/span[{y}]')
                sizes  = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[2]/div/div/div[2]/span[{y}]').text
        
                is_slec = "sku-variable-img-wrap-selected" in size.get_attribute("class")
                print(is_slec)
                size.click()
                print(sizes)
                try:
                    is_up = "sku-variable-size-disabled" in size.get_attribute("class")
                    print(is_up)
                except:
                    print("jjs")
                two_s.append(sizes)
                time.sleep(2)  




                try:
                    original_price = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module_product_price_1"]/div/div/span'))).text
                    # print(original_price)                                                                         /
                    original_price = original_price.split('M')[1]
                    original_price = original_price.split('$')[1]
                    original_price = float(original_price)
                except:
                    try:
                        original_price = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module_product_price_1"]/div/div/span[1]'))).text
                        original_price = original_price[1:]
                        original_price = float(original_price)
                    except:
                        original_price = "Not Found"
                try:
                    final_price = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module_product_price_1"]/div/div/span'))).text
                                                                                                        
                    final_price = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/div/span[1]').text
                    final_price = final_price.split('M')[1]
                    final_price = final_price.split('$')[1]
                    final_price = float(final_price)
                
                except:
                    try:
                        final_price = final_price[1:]
                        final_price = float(final_price)
                    except:
                        final_price = "Not Found"                                
  
               
               
                try:                                            
                    stock_count = driver.find_element_by_xpath('//*[@id="module_quantity-input"]/div/div/span').text
                    if stock_count == 'Out of stock':
                        stock_count = 0
                        stock_status = 'Out of stock'
                    else:
                        stock_count = stock_count.split(' ')[1]
                        stock_count = int(stock_count)
                except:
                    stock_count = 'null'
                    stock_status = 'available'
                # print(stock_status)
                try:
                    if stock_count == 'null':
                        stock_status = 'available'
                    elif stock_count == 0:
                        stock_status = 'sold out'
                    elif stock_count > 5:
                        stock_status = 'available'
                    elif stock_count <= 4:
                        stock_status = 'low '
                except:
                    stock_status = 'available'
                try:
                    discount = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/div/span[2]').text
                except:                                                
                    discount = "Not Found"
                print(stock_status,stock_count)
                size.click()
                varianyg = {
                    f'{variant_n}':namer,
                    f'{variant_s}':sizes
                }
                if (is_up == True and is_main == True):
                    stock_status = 'low'
                    stock_count = 1
                mains_dir = {
                'original_price':original_price,
                'final_price':final_price,
                'stock_status':stock_status,
                'stock_count':stock_count,
                'variant':varianyg,
                
                }
                if discount != 'Not Found':
                    mains_dir['discount'] = discount
                vatiants.append(mains_dir)
                print(mains_dir)
        except:
            pass

except:
    pass

two_s = set(two_s)
print(vatiants)

# models=[]
# try:
#     for x in range(1,lable1):
#         hhsd = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[{x}]/div/div/img').click()
    
#         namer = driver.find_element_by_xpath('//*[@id="module_sku-select"]/div/div[1]/div/div/div[1]/span').text
#         print(namer)
#         models.append(namer)
# except:
#     pass

hhs = []
flag = 0
if len(vatiants) == 0:                         
    try:
        two_f = []
        flag=1
        for x in range(1,30):                     
            hhsd = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div/div/div/div[2]/span[{x}]')
            namer = driver.find_element_by_xpath(f'//*[@id="module_sku-select"]/div/div/div/div/div[2]/span[{x}]').text
            hhsd.click()
            time.sleep(3)
            print(namer)
            two_f.append(namer)
            
            try:
                original_price = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
                # print(original_price)
                original_price = original_price.split('M')[1]
                original_price = original_price.split('$')[1]
                original_price = float(original_price)
            except:
                original_price = "Not Found"
            try:
                final_price = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/div/span[1]').text
                final_price = final_price.split('M')[1]
                final_price = final_price.split('$')[1]
                final_price = float(final_price)
            
            except:
                final_price = "Not Found"

            try:                                        
                stock_count = driver.find_element_by_xpath('//*[@id="module_quantity-input"]/div/div/span').text
                if stock_count == 'Out of stock':
                    stock_count = 0
                    stock_status = 'Out of stock'
                else:
                    stock_count = stock_count.split(' ')[1]
                    stock_count = int(stock_count)
                
            except:
                stock_count = 'null'
                stock_status = 'available'
            # print(stock_status)
            try:
                if stock_count == 'null':
                    stock_status = 'available'
                elif stock_count == 0:
                    stock_status = 'sold out'
                elif stock_count <= 4:
                    stock_status = 'low '
                elif stock_count >= 5:
                    stock_status = 'available'
                
            except:
                stock_status = 'available'
            try:
                discount = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/div/span[2]').text
            except:                                                
                discount = "Not Found"
            print(stock_status,stock_count)


            variants = {
                f'{variant_n}': namer,
            }
            mins_s = {
                'original_price':original_price,
                'final_price':final_price,
                'stock_count':stock_count,
                'stock_status':stock_status,
                'variant':variants,
                'discount':discount,
            }

            print(mins_s)
            vatiants.append(mins_s)
    except:
        print("okkk")
        pass

print(vatiants)

if len(vatiants) == 0:
    try:                                                   
        original_price = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
        # print(original_price)
        original_price = original_price.split('M')[1]
        original_price = original_price.split('$')[1]
        original_price = float(original_price)
    except:
        try:
            original_price = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div').text
            original_price = original_price.split('$')[1]
            original_price = float(original_price)
        except:
            original_price = "Not Found"
    try:
        final_price = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/div/span[1]').text
        final_price = final_price.split('M')[1]
        final_price = final_price.split('$')[1]
        final_price = float(final_price)
    
    except:
        final_price = "null"
    try:                                        
        stock_count = driver.find_element_by_xpath('//*[@id="module_quantity-input"]/div/div/span').text
        if stock_count == 'Out of stock':
            stock_count = 0
            stock_status = 'Out of stock'
        else:
            stock_count = stock_count.split(' ')[1]
            stock_count = int(stock_count)
        
    except:
        stock_count = 'null'
        stock_status = 'available'
    # print(stock_status)

    try:
        if stock_count == 'null':
            stock_status = 'available'
        elif stock_count == 0:
            stock_status = 'sold out'
        elif stock_count <= 4:
            stock_status = 'low '
        elif stock_count >= 5:
            stock_status = 'available'
        
    except:
        stock_status = 'available'
    try:
        discount = driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/div/span[2]').text
    except:                                                
        discount = "Not Found"
    print(stock_status,stock_count)
    mins_s = {
                'original_price':original_price,
                'final_price':final_price,
                'stock_count':stock_count,
                'stock_status':stock_status,
                'variant':'null',
                'discount':discount,
            }

    print(mins_s)
    vatiants.append(mins_s)





try:
   description = driver.find_element_by_class_name("pdp-button_theme_white pdp-button_size_m")
   description.click()
   des = driver.find_element_by_class_name("specification-keys").text
except:
    try:
        description = driver.find_element_by_xpath('//*[@id="module_product_detail"]/div/div/div[2]/button')
        description.click()
        des = driver.find_element_by_class_name("specification-keys").text
    except:
        des = "Not Found"

vvs = {
    f'{variant_n}': two_f,
    f'{variant_s}':two_s,
}

if flag == 1:
    del vvs[f'{variant_s}']

item_parent = {
    'name':  name,
    'description': des,
    'rating': rating,
    'rating_count': rating_count,
    'url': main_url,
    'item_id': item_id,
    'variants':vvs,
    'images': imgss,

}




# item_variants1 = []
# item_variants1.append(item_variants)
main_dir = {
    "item_parent": item_parent,
    "item_variants": vatiants,
}

main_list.append(main_dir)
df = pd.DataFrame(main_list)
df.to_json('lazadaOutput.json', orient='records', lines=True)


print('script run successfully')

driver.quit()

