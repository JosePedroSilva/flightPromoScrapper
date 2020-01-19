import requests
from bs4 import BeautifulSoup

nums_played = [3, 4, 20, 44, 49]
stars_played = [3, 9]


URL = 'https://www.jogossantacasa.pt/web/SCCartazResult/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# Requests the numbers to URL and returns raw HTML
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the winning numbers and convert them into a list
result = soup.find(attrs="colums").get_text()
r = (result.replace('+', '').strip())

# Removes unnecessary and duplicate information from the list and creates a list for the numbers and a list for the stars
try:
    result_comp = list(map(int, r.split()))
    result_comp = result_comp[0:7]
    numbers = result_comp[0:5]
    stars = result_comp[5:]
except ValueError:
    print('Unble to convert into list.')

# Checks the numbers that are correct and returns the number of correct
counter_nums = 0
for n in nums_played:
    for n2 in numbers:
        if n == n2:
            counter_nums += 1

# Checks the stars that are correct and returns the number of correct
counter_stars = 0
for s in stars_played:
    for s1 in stars:
        if s == s1:
            counter_stars += 1

print(
    f'You have {counter_nums} number correct and {counter_stars} star correct')
