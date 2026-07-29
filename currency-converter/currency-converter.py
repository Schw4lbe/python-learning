import requests


class CurrencyExchangeData:
    def __init__(self):
        self.amount: int
        self.currency_in: str
        self.currency_out: str
        self.fetched_data: list

    def clear(self):
        self.amount
        self.currency_in
        self.currency_out
        self.fetched_data

    history: list = []

    CURRENCIES = {
        1: {"name": "US Dollar", "short_term": "USD"},
        2: {"name": "Euro", "short_term": "EUR"},
        3: {"name": "British Pound", "short_term": "GBP"},
        4: {"name": "Japanese Yen", "short_term": "JPY"},
        5: {"name": "Swiss Franc", "short_term": "CHF"},
        6: {"name": "Chinese Yuan", "short_term": "CNY"},
        7: {"name": "Thai Baht", "short_term": "THB"},
        8: {"name": "Indian Rupee", "short_term": "INR"},
    }


exchange = CurrencyExchangeData()


def init_currency_exchange():
    clear_currency_exchange_data()
    try:
        exchange.amount = get_exchange_amount()
        exchange.currency_in = int(input("Enter number start currency: "))
        exchange.currency_out = int(
            input("Enter number output currency or (0) for ALL: ")
        )
        prep_fetch_exchange_data(
            exchange.amount, exchange.currency_in, exchange.currency_out
        )
    except KeyboardInterrupt:
        print("keyboard exit")
    except ValueError:
        print("invalid input.")
        init_currency_exchange()


def clear_currency_exchange_data():
    exchange.clear()


def get_exchange_amount():
    amount: int = int(input("Enter amount (1 - 9999): "))
    if amount <= 0 or amount >= 10000:
        raise ValueError
    else:
        return amount


def prep_fetch_exchange_data(amount: int, cur_in: int, cur_out: int):
    cur_in_term: str = get_currency_in_short(cur_in)
    cur_out_terms: list = get_currency_output_shorts(cur_out)
    url_string_list: list = get_url_string_list(cur_out_terms, amount, cur_in_term)

    fetch_data(url_string_list)
    handle_display_result()
    init_currency_exchange()


def handle_display_result():
    data: list = exchange.fetched_data

    for item in data:
        item_amount: int = int(item["amount"])
        item_cur_in: str = item["base"]
        rate: float = next(iter(item["rates"].values()))
        item_rate: float = round(rate, 2)
        item_cur_out: str = next(iter(item["rates"].keys()))

        print(
            f"The exchange of {item_amount} {item_cur_in} equals {item_rate} {item_cur_out}"
        )

        exchange.history.append(item)
    display_exchange_history()


def display_exchange_history():
    print("\nEXCHANGE HISTORY:")
    for item in exchange.history:
        print(f"{item}")


def fetch_data(url_string_list: list):
    exchange_data: list = []

    for url in url_string_list:
        response = requests.get(url)
        data = response.json()
        exchange_data.append(data)
        print("_DEV fetch data: ", data)
        print("_DEV fetch status: ", response.status_code)

    exchange.fetched_data = exchange_data


def get_currency_in_short(value: int):
    return exchange.CURRENCIES[value]["short_term"]


def get_currency_output_shorts(value: int):
    results: list = []
    if value == 0:
        for i, item in exchange.CURRENCIES.items():
            results.append(item["short_term"])
    else:
        results.append(exchange.CURRENCIES[value]["short_term"])
    return results


def get_url_string_list(cur_out_terms: list, amount: int, cur_in_term: str):
    list_of_strings: list = []
    for item in cur_out_terms:
        # excludes exchange same currency
        if item == cur_in_term:
            continue
        else:
            list_of_strings.append(
                f"https://api.frankfurter.app/latest?amount={amount}&from={cur_in_term}&to={item}"
            )
    return list_of_strings


def print_currencies(currencies: dict):
    for key, currency in currencies.items():
        print(f"{key}: {currency['name']} ({currency['short_term']})")


def main():
    print_currencies(exchange.CURRENCIES)
    init_currency_exchange()


if __name__ == "__main__":
    main()
