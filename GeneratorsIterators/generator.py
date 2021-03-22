def jokes_generator(jokes):
    next_index = 0
    while next_index < len(jokes):
        yield jokes[next_index]
        next_index += 1


if __name__ == '__main__':
    jokes_list = ['Не грусти, а то х*й не будет расти', 'Алло - х*ум по лбу не дало?']
    jokes = jokes_generator(jokes_list)
    for joke in jokes:
        print(joke)
