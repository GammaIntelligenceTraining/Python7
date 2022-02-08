with open('text_files/trimushketera.txt', 'r', encoding='utf8') as file:
    data = file.read().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('"', '')\
        .replace(':', '').replace(';', '').lower()
    word_list = data.split()
    unique_list = list(set(data.split()))

    with open('results/trimushketera_result.txt', 'w', encoding='utf8') as wfile:
        wfile.write(f'There are {len(word_list)} words in text.\n')
        wfile.write(f'There are {len(unique_list)} unique words in text.\n')
        for word in sorted(unique_list):
            wfile.write(word + '\n')
