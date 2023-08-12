import csv

def add_pet(pet_name_en, pet_name_chn):
    pet_file = open('C:\ssr-config\\trunk\config\csv\Pet.csv', encoding='utf-8')
    petType_file = open('C:\ssr-config\\trunk\config\csv\PetType.csv', encoding='utf-8')
    dict_reader = csv.DictReader(pet_file)
    reader = csv.reader(pet_file)

    writer = csv.writer(file)
    print(dict_reader[5]['StringId'])
    # for row in reader:
    #     print(row[0])



if __name__ == '__main__':
    for i in ['B', 'A', 'S']:
        for j in range(8):
            print('Rank_battlePet_%s%s' % (i, 10+j))