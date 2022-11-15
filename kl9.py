import requests

response = requests.get("https://coinmarketcap.com/")
responseText = response.text
responseParse = responseText.split("<span>")

parse_list = []

for parse_elem_1 in responseParse:
    if parse_elem_1.startswith('$'):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith('$') and parse_elem_2[1].isdigit():
                parse_list.append(parse_elem_2)

print(parse_list[0])
bitcoinDollar = parse_list[0]
bitcoinDollar = bitcoinDollar[1:len(bitcoinDollar)-3]
bitcoinDollar = bitcoinDollar.replace(",",".")
print(bitcoinDollar)

print("Kurs uah", float(bitcoinDollar) * 41)