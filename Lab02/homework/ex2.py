from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connect = urlopen(url)

raw_data = connect.read()
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")

header = soup.find("table", id="tblGridData").tr.find_all("td")
table = soup.find("table", id="tableContent").find_all("tr")

tableheader = []
for i in header:
    a = i.text.strip()
    tableheader.append(a)
tableheader.pop()

tablecontent = []
for td in table:
    a = td.find_all("td")
    a_list = []
    for i in a:
        b = i.text.strip()
        a_list.append(b)
    if a_list != [] and (not all(v == "" for v in a_list)):
        a_list = a_list[:5]
        tablecontent.append(a_list)

tablefull = []
for content in tablecontent:
    row = {}
    for i in range(len(tableheader)):
        a = tableheader[i]
        b = content[i]
        row[a] = b
        row = OrderedDict(row)
    tablefull.append(row)

pyexcel.save_as(records=tablefull, dest_file_name="data.xlsx")
