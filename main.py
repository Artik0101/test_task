# pip install prettytable
# pip install BeautifulSoup
# pip install requests
import requests

from prettytable import PrettyTable
from bs4 import BeautifulSoup

def get_countries_list(url):
    table = PrettyTable()
    table.field_names = ["Country","Capital","Flag"]
    response = requests.get(url)

    if response.status_code == 200:
        countries_list  = response.json()
        for country in countries_list:
            table.add_row([country['name']['common'], country.get('capital',["N/A"])[0],  country['flags']['png']])
    print(table)

def get_items_index():
            
    items_info = []
    with open ('index.html') as file:
        index = file.read()
    
    soup = BeautifulSoup(index,"html.parser")
    price = soup.find('div',class_='x-price-primary').text # type: ignore
    shipping = soup.find('div', class_='ux-labels-values__values-content').find('span').text # type: ignore
    shop = soup.find('h2', class_='d-stores-info-categories__container__info__section__title').find('span').text # type: ignore
    photo = soup.find('img')
    title = ' '.join(soup.find('h1',class_='x-item-title__mainTitle').text.split()) # type: ignore
    items_info.append({
        'title':title,
        'price':price,
        'shipping':shipping,
        'shop':shop,
        'photo_url':photo['src'] # type: ignore
    })
    print(items_info)


def get_index_from_url(url):
    
    headers = {
        'Accept':'*/*',
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
         }
    cookies = { 'ebay':'%5Ejs%3D1%5Esbf%3D%23000000%5E',
                's':'CgAD4ACBmnRK6ZDA2YWNhY2YxOTAwYTlmMTk1YzNiODNkZmZmMzc5Zjj7FVZY',
                '__deba':'O7L_HwHiMP_JHDWMkZPIXU0ZPUe5Ci7DFOvr3dgNVcSjtDAcSsIh-lUMkTdDBaatXR8UW1J2_XMwSXzXGqPFGKyV7SFxszKhmlf0p-Gll5d_2fGaBAQrUljfHSrSRSLHpvL9OjE4JFJD3YdKXDC2Eg==',
                'cpt':'%5Ecpt_guid%3Dc677f77c-38f5-422f-ae0c-02df73bbacba%5Ecpt_prvd%3Drecaptcha_v2%5E',
                'nonsession':'BAQAAAZBR14g6AAaAADMABGh97SYsRE5LAMoAIGpfIKZkMDZhY2FjZjE5MDBhOWYxOTVjM2I4M2RmZmYzNzlmOADLAAJmnMCuMTKlhbGcsulpoYRlwnV4w6C04E4dAg**',
                'bm_sv':'BA2F2C5B30591EC2E0960D035783A293~YAAQRDYQYEO4+8yQAQAAbjI11Bj5yK69qOV9HhP2bYPEXLA0FUKJ4an3Ux/b4Injl25Eps1cSNRTkNTuuK2ASsMM0b243r0fhyFHrjESICKz4ngc1WEKdbLiYNqYo3MzeD4h8M+MZYZN4L1zpwhXnhGD02m4UalNxYJP/DQ59SWA3l9UoLrPTzXZ1+Ye0nobVGTdG0ZBq8MVnpZkY9se9x0fQ8uVvsI8VWrSHuTp7f7piQ/RS8JkxhRRnJldthc=~1',
                'dp1':'bpbf/#c0002000000000000000006a5f26c3^bl/UA6a5f26a2^',   
                'ds2':'sotr/bGvQkzzzzzzz^'
               }
    response = requests.get(url,headers=headers,cookies=cookies)
    if response.status_code == 200:
        print(response.status_code)
        src = response.text
        with open('index.html','w') as file:
            file.write(src)
        get_items_index()
    else:
        print(response.status_code)

get_items_index()
get_countries_list("https://restcountries.com/v3.1/all")