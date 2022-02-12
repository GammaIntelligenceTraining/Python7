import csv
import time


def get_top_results(column, top_number):
    results = []
    for entry in data:
        results.append([entry[column], entry['Country or region']])
    results.sort()
    output = []
    while top_number > 0:
        output.append(results.pop())
        top_number -= 1
    return output


def results_printer(result):
    for entry in result:
        print(f'{entry[1]}: {entry[0]}')
    print()
    time.sleep(5)


def main():
    while True:
        user_choice = input('Please choose:\n'
                            '1.Score\n'
                            '2.GDP per capita\n'
                            '3.Social support\n'
                            '4.Healthy life expectancy\n'
                            '5.Freedom to make life choices\n'
                            '6.Generosity\n'
                            '7.Perceptions of corruption\n'
                            '0.Exit\n'
                            '--> ')
        try:
            user_top = int(input('Please enter how many countries: '))
            if int(user_top) > len(data):
                raise UserWarning
        except UserWarning:
            print()
            print(f'There are {len(data)} countries!')
            time.sleep(3)
            continue
        except ValueError:
            print()
            print('Value you entered is not numeric!')
            time.sleep(3)
            continue
        else:
            if user_choice == '0':
                break
            elif user_choice == '1':
                print()
                print('Top Score')
                results_printer(get_top_results('Score', user_top))
            elif user_choice == '2':
                print()
                print('Top GDP per capita')
                results_printer(get_top_results('GDP per capita', user_top))
            elif user_choice == '3':
                print()
                print('Top Social support')
                results_printer(get_top_results('Social support', user_top))
            elif user_choice == '4':
                print()
                print('Top Healthy life expectancy')
                results_printer(get_top_results('Healthy life expectancy', user_top))
            elif user_choice == '5':
                print()
                print('Top Freedom to make life choices')
                results_printer(get_top_results('Freedom to make life choices', user_top))
            elif user_choice == '6':
                print()
                print('Top Generosity')
                results_printer(get_top_results('Generosity', user_top))
            elif user_choice == '7':
                print()
                print('Top Perceptions of corruption')
                results_printer(get_top_results('Perceptions of corruption', user_top))
            else:
                print()
                print('Choice is out of range!')
                time.sleep(3)
                continue


with open('2019.csv', 'r', encoding='utf8') as survey:
    data = list(csv.DictReader(survey))


main()