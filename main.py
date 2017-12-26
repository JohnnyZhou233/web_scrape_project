
from urllib.request import urlopen

url  = "https://3c.tmall.com/?spm=a21bo.2017.201859.5.b182118kDB8qp"
def get_website(url):

	response = urlopen(url)
	data = response.read()
	text = data.decode("utf-8")
	return text

text = get_website(url)

with open('html_text.txt', 'w') as f:
    f.write(text)