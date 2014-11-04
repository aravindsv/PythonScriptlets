import urllib
from bs4 import BeautifulSoup

url = "https://ccle.ucla.edu/pluginfile.php/750795/mod_resource/content/0/Midterm1_scores.pdf"
html = urllib.urlopen(url).read()
raw = BeautifulSoup(html).get_text()

print raw

