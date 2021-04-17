import urllib.request,urllib.parse,bs4,re

website = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1181904.html").read()
target_list = bs4.BeautifulSoup(website,"html.parser").find_all("span")

sum = 0
for item in target_list:
    sum += int(item.text)

print("the result is: ",sum)


