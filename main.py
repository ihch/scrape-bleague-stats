import csv
from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    html = requests.get("https://www.bleague.jp/stats/").text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.findAll("table", {"id": "tbl-player"})[0]
    rows = table.findAll("tr")

    with open("bleague-stats.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in rows:
            csv_row = []
            for item in row.findAll(['td', 'th']):
                csv_row.append(item.get_text().strip())
            writer.writerow(csv_row)
