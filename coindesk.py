from selenium import webdriver
import selenium
import time
import pandas as pd

browser=webdriver.Chrome(executable_path=r"C:\Users\puneet\Downloads\chromedriver.exe")
browser.get("https://coindesk.com")
i=0
''' this while loop will go to the last article of the page'''

while true:
    try:
        browser.find_element_by_id('byscripts_ajax_posts_loader_trigger').click()
    except:
        continue
    i+=1
    if(i>15):
        continue

html=browser.page_source
soup=BeautifulSoup(html,'lxml')
content=soup.find('div',id="content")

news=[]
date=[]
publisher=[]
paragraph=[]
headline=[]

'''finding date,headline,paragraphs,and publisher and storing in pandas dataframe'''

news=content.find_all('div',class_="post-info")
for i in news:
    date.append(i.find('p',class_="timeauthor").text[:20])
    publisher.append(i.find('p',class_="timeauthor").text[23:].strip())
    paragraph.append( i.find_all('p')[1].text)
    headline.append(i.find_all('a',class_="fade")[0].text)

test_df=pd.DataFrame({'Date':date,"Publisher":publisher,'Headline':headline,'Paragraph':paragraph})
