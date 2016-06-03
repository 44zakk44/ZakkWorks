from urllib import request

goog_url='http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=31&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def download_stock_data(csv_url):

# polaczenie z internetem

    response = request.urlopen(csv_url)
    csv = response.read()

# zapisanie jako tekst

    csv_str = str(csv)
    lines = csv_str.split("\\n")

# zrobienie pliku

    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)