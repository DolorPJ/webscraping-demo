from lxml import html
from openpyxl.workbook import Workbook
import requests
import pandas as pd


def get_data(url):
    main_page = requests.get(url)
    content = html.fromstring(main_page.content)
    header  = content.xpath('//*[@id="schwab_header"]')
    footer = content.xpath('//*[@id="footer"]')

    data = []
    item = {}
    for head in header:
        item["Header Links"] = head.xpath('//*[@id="schwab_header"]//a/@href')
        
        item["Header Text"] = []
        for i in  head.xpath('//*[@id="schwab_header"]//a/text()'):
            item["Header Text"].append(i.replace('\n', '').strip()) 

    for foot in footer:
        item["Footer Links"] = foot.xpath('//*[@id="footer"]//a/@href')

        item["Footer Text"] = []
        for j in foot.xpath('//*[@id="footer"]//a/text()'):
            item["Footer Text"].append(j.replace('\n', '').strip())


        data.append(item)
    
    # print(data)
    return data

# data = get_data("https://www.schwab.com")



def export_data(data):
    df = pd.DataFrame(data)
    
    df.to_excel("prasad.xlsx")

if __name__ == "__main__":
    data = get_data("https://www.schwab.com")
    export_data(data)
    print("done")



page = requests.get("https://www.schwab.com/")

# parsing the page
content = html.fromstring(page.content)
# content = lxml.html.fromstring(page.content)

header = content.xpath('//*[@id="schwab_header"]')
footer = content.xpath('//*[@id="footer"]/div')
def removeElement(header, footer):
# to remove header content
    for badHeader in header:
        badHeader.getparent().remove(badHeader)

# to remove footer content
    for badFooter in footer:
        badFooter.getparent().remove(badFooter)

    main_content = html.tostring(content, pretty_print=True)

    print(main_content)

removeElement(header, footer)
