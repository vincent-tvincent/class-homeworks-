import urllib.request, urllib.parse, bs4, re
def retrieve_data(url,number):
    data = bs4.BeautifulSoup(urllib.request.urlopen(url).read(),"html.parser")
    name_list = data.find_all("a")
    return [name_list[number-1].text,name_list[number-1]["href"]]

url = " http://py4e-data.dr-chuck.net/known_by_Justin.html"
for i in range(7):
    data = retrieve_data(url,18)
    name = data[0]
    url = data[1]
print("the name is: ", name)

