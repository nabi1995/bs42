from bs4 import BeautifulSoup

with open("website.html") as file1:
    content = file1.read()

soup = BeautifulSoup(content, "html.parser")

anchor_tags = soup.find_all(name="a")

for anchor in anchor_tags:
    print(anchor.getText())

print("Hello world")


