from bs4 import BeautifulSoup
import requests
import xlsxwriter

html= requests.get('https://www.gsmarena.com/apple-phones-48.php')
# print(html.text)
soup = BeautifulSoup(html.text,'lxml') #text converts the whole html request to a text readable by beautiful soup

devices= soup.find('div', class_ = 'makers')
print("Hello")
iphone_workbook = xlsxwriter.Workbook('iPhones.xlsx')
iphone_sheet = iphone_workbook._add_sheet('phones_trial_1')

iphone_sheet.write("A1","Phones")
iphone_sheet.write("B1","links")
devices_links = devices.find_all('a')
i = 2
for device_link in devices_links:
    if 'iPhone' in device_link.span.text:
        print(device_link.span.text) #printing the text of span inside a tag
        print('https://www.gsmarena.com/' + device_link['href'])
        iphone_sheet.write("A"+str(i),device_link.span.text)
        iphone_sheet.write("B"+str(i),'https://www.gsmarena.com/' + device_link['href'])
        i = i + 1

iphone_workbook.close()

