from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_club_names(html):
    soup = BeautifulSoup(html, 'lxml')
    uls = soup.find('ul',
                    class_='block-list-5 block-list-3-m block-list-1-s block-list-1-xs block-list-padding dataContainer').find_all(
        'li')
    names = []
    stadiums = []
    for li in uls:
        a = li.find('h4').getText()
        b = li.find('div', class_='stadiumName').getText()
        names.append(a)
        stadiums.append(b)

    info = {'Club': names,
                'Stadium': stadiums}

    print(info)
    return info


def write_csv(info):
    with open("info.csv", 'w',newline='')as f:
        header = info.keys()
        writer = csv.DictWriter(f, fieldnames=tuple(header))
        writer.writeheader()
        for pivoted in zip(*info.values()):
            writer.writerow(dict(zip(header, pivoted)))


def main():
    url = "https://www.premierleague.com/clubs"
    write_csv(get_club_names(get_html(url)))


if __name__ == '__main__':
    main()
