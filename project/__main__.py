import requests
import json
import datetime
import tzlocal


def start_up():
    class Colors:
        purple = '\033[95m'
        blue = '\033[94m'
        green = '\033[92m'
        red = '\033[91m'

    print('\n')
    print(f'{Colors.purple}******** ********  *     *  ******** ******** ********        ')
    print(f'{Colors.blue}*        *  * ***    * *    * ******     *    *      *        ')
    print(f'{Colors.green}*        *   *        *     *            *    *      *        ')
    print(f'{Colors.red}******** *    *       *     *            *    ********        ')
    print(f'                                                         ')
    print(f'{Colors.purple}          ********  *******  ******* ****                     ')
    print(f'{Colors.blue}           *         *        *       *   *                    ')
    print(f'{Colors.green}          *****     *****    *****   *    *                   ')
    print(f'{Colors.red}          *         *        *       *    *                   ')
    print(f'{Colors.purple}          *         *******  ******* *****               ')


def get_coin():
    response = requests.get('https://api.alternative.me/v2/ticker/')
    res = json.loads(response.text)
    coin_found = True

    while True:
        if not coin_found:
            print('Coin not found...')

        coin = input(f'\nEnter the cryptocurrency you would like to see data on (symbol or name): ')
        for coin_id, coin_info in res.items():
            for data in coin_info.values():
                if data['name'] == coin.title() or data['symbol'] == coin.upper():
                    show_coin_data(data, coin)
                else:
                    coin_found = False
                    continue
                break
            break


def show_coin_data(data, coin):
    for key, value in data.items():
        if key == 'name':
            print('\n' + key.title() + ': ' + value)
        if key == 'symbol':
            print(key.title() + ': ' + value)
        if key == 'rank':
            print(key.title() + ': ' + str(value))
        if key == 'circulating_supply':
            print(f'Circulating Supply: {int(value):,d} {coin}')
        if key == 'total_supply':
            print(f'Total Supply (Coins in existence minus verified burns): '
                  f'{int(value):,d} {coin}')
        if key == 'max_supply' and value != 0:
            print(f'Max Supply: {int(value):,d} {coin}')
        if key == 'quotes':
            for currency, info in value.items():
                price_data(info)
        if key == 'last_updated':
            local_timezone = tzlocal.get_localzone()
            local_time = (datetime.datetime.fromtimestamp(value, local_timezone)).strftime(
                '%y-%m-%d %H:%M:%S')
            print(f'Data Last Updated: {str(local_time)}')
            get_another()


def price_data(info):
    for key, value in info.items():
        if key == 'price':
            print(f'{key.title()}: ${value:,.2f}')
        if key == 'volume_24h':
            print(f'24 Hour Volume: ${value:,.2f}')
        if key == 'market_cap':
            print(f'Market Cap: ${value:,.2f}')
        if key == 'percentage_change_1h':
            print(f'1 Hour % Change: %{value}')
        if key == 'percentage_change_24h':
            print(f'24 Hour % Change: %{value}')
        if key == 'percentage_change_7d':
            print(f'7 Day % Change: %{value}')


def get_another():
    while True:
        another = (input('\nWould you like to check another coin?: (y) (n)'))
        if another.lower() == 'y':
            get_coin()
        elif another.lower() == 'n':
            print('Goodbye!')
            exit()
        else:
            print('Please enter y or n!')


def main():
    start_up()
    get_coin()


if __name__ == "__main__":
    main()
