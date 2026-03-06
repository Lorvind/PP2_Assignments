import re, json

def turn_to_float(s: str):
    l = ""
    for c in s:
        if c == ',':
            l += '.'
        elif c == ' ':
            continue
        else:
            l += c

    return float(l)

prices_pattern = r"Стоимость\s(\d+,\d+)"
product_names_pattern = r"\d+\.\s*\n(.*)"
datetime_pattern = r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}"
bank_card_pattern = r"(Банковская карта):\n(.*)"


with open("raw.txt", 'r') as file:
    text = file.read()

    prices = re.findall(prices_pattern, text)
    product_names = re.findall(product_names_pattern, text)

    date_time = re.search(datetime_pattern, text).group()
    amount_payed_by_card = re.search(bank_card_pattern, text)

    if turn_to_float(amount_payed_by_card.group(2)) > 0:
        payment_method = amount_payed_by_card.group(1)
    else:
        payment_method = "Наличные"

total_amount = sum(list(map(turn_to_float, prices)))

with open("result.txt", 'w') as output_file:
    date = {
        "Prices": prices,
        "Product names": product_names,
        "Total amount": total_amount,
        "Date and time": date_time,
        "Payment method": payment_method,
    }

    json.dump(date, output_file, ensure_ascii=False, indent=4)