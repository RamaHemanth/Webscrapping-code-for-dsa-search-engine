# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import time

from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.codechef.com/tags/problems/dynamic-programming")

time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_ques_div = soup.findAll("div", {"class": "problem-tagbox-inner"})

all_ques = []

for ques in all_ques_div:
    all_ques.append(ques.findAll("div")[0].find("a"))

urls = []
titles = []

for ques in all_ques:
    urls.append("https://www.codechef.com"+ques['href'])
    titles.append(ques.text)

#with open("problem_urls_dp.txt", "w+") as f:
#    f.write('\n'.join(urls))

#with open("problem_titles_dp.txt", "w+") as f:
# 	f.write('\n'.join(titles))
cnt = 0
for url in urls:
    driver.get(url)
    cnt += 1
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    problem_text = soup.find('div', {"class": "problem-statement"}).get_text()
    print(problem_text)
    problem_text = problem_text.encode("utf-8")
    problem_text = str(problem_text)

    with open("problem"+str(cnt)+".txt", "w+") as f:
        f.write(problem_text)