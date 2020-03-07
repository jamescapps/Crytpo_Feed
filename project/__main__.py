import requests
import json
import datetime
import tzlocal


def main():
    response = requests.get('https://api.alternative.me/v2/ticker/')
    res = json.loads(response.text)
    coin_found = True
    redo = False

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

    while True:
        if not coin_found and not redo:
            print('Coin not found...')
        coin = input(f'\nEnter the cryptocurrency you would like to see data on (symbol or name): ')
        redo = False
        for key, value in res.items():
            for index in value.items():
                for item in index:
                    if type(item) == dict:
                        for i in item.items():
                            for j in i:
                                if j == coin.upper() or j == coin.title():
                                    coin_found = True
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
                                        if k == 'last_updated':
                                            local_timezone = tzlocal.get_localzone()
                                            local_time = (datetime.datetime.fromtimestamp(v, local_timezone)).strftime(
                                                '%y-%m-%d %H:%M:%S')
                                            print(f'Data Last Updated: {str(local_time)}')
                                            while True:
                                                another = (input('\nWould you like to check another coin?: (y) (n)'))
                                                if another.lower() == 'y':
                                                    redo = True
                                                    break

                                                elif another.lower() == 'n':
                                                    print('Goodbye!')
                                                    exit()
                                                else:
                                                    print('Please enter y or n!')
                                                    continue
                                else:
                                    coin_found = False


if __name__ == "__main__":
    main()
