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
        for key, value in res.items():
            x = [v + z for v in value for z in v]
            print(x)
            '''for index, v in value.items():
                for y, z in v.items():
                    if z == coin.upper() or z == coin.title():
                        coin_found = True
                        show_coin_data(v, coin)'''

        x = [value + v for value in res for v in value]
        print(x)

def show_coin_data(item, coin):
    for k, v in item.items():
        if k == 'name':
            print('\n' + k.title() + ': ' + v)
        if k == 'symbol':
            print(k.title() + ': ' + v)
        if k == 'rank':
            print(k.title() + ': ' + str(v))
        if k == 'circulating_supply':
            print(f'Circulating Supply: {int(v):,d} {coin}')
        if k == 'total_supply':
            print(f'Total Supply (Coins in existence minus verified burns): '
                  f'{int(v):,d} {coin}')
        if k == 'max_supply' and v != 0:
            print(f'Max Supply: {int(v):,d} {coin}')
        if k == 'quotes':
            for x in v.items():
                for y in x:
                    # Run function to get the price data
                    price_data(y)
        if k == 'last_updated':
            local_timezone = tzlocal.get_localzone()
            local_time = (datetime.datetime.fromtimestamp(v, local_timezone)).strftime(
                '%y-%m-%d %H:%M:%S')
            print(f'Data Last Updated: {str(local_time)}')
            # Run next function
            get_another()


def price_data(y):
    if type(y) == dict:
        for z, a in y.items():
            if z == 'price':
                print(f'{z.title()}: ${a:,.2f}')
            if z == 'volume_24h':
                print(f'24 Hour Volume: ${a:,.2f}')
            if z == 'market_cap':
                print(f'Market Cap: ${a:,.2f}')
            if z == 'percentage_change_1h':
                print(f'1 Hour % Change: %{a}')
            if z == 'percentage_change_24h':
                print(f'24 Hour % Change: %{a}')
            if z == 'percentage_change_7d':
                print(f'7 Day % Change: %{a}')


def get_another():
    while True:
        another = (input('\nWould you like to check another coin?: (y) (n)'))
        if another.lower() == 'y':
            # Run again
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