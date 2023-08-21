

if __name__ == '__main__':
    dict = {'A': 1}
    for i in range(5):
        dict['B'] = 1 if 'B' not in dict else dict['B'] + 1
    print(dict['B'])