import csv
import os.path


# def add_pet(pet_name_en, pet_name_chn):
#     pet_file = open('C:\ssr-config\\trunk\config\csv\Pet.csv', encoding='utf-8')
#     petType_file = open('C:\ssr-config\\trunk\config\csv\PetType.csv', encoding='utf-8')
#     dict_reader = csv.DictReader(pet_file)
#     reader = csv.reader(pet_file)
#
#     writer = csv.writer(file)
#     print(dict_reader[5]['StringId'])
#     # for row in reader:
#     #     print(row[0])

def add_pet_model(pets):
    art_resc_file = open('C:\ssr-config\\trunk\config\csv\ArtResource.csv', encoding='utf-8')
    reader_art_resc = csv.reader(art_resc_file)
    rows_art_resc = list(reader_art_resc)

    pet_file = open('C:\ssr-config\\trunk\config\csv\Pet.csv', encoding='utf-8')
    reader_pet = csv.reader(pet_file)
    rows_pet = list(reader_pet)

    # 读取ArtResource.csv文件中ID列值>=2000000且<3000000的最后一行
    for row in rows_art_resc:
        if row[0] < '3000000':
            last_row = row
    line = 0
    for row in rows_art_resc:
        line += 1
        if row[0] == last_row[0]:
            break

    print(line)

    num = int(last_row[1].split('S')[1].split('_')[0])
    last_num = int(last_row[0])

    for en_name, cn_name in pets:
        num += 1
        rows_art_resc.insert(line,
                             [str(last_num + 1), 'mdl_battlePet_B' + str(num), '宠物展示模型_' + cn_name, '0', '模型',
                              'mdl_pet_' + en_name + '_lod0', '', '', '', '', '', '', '', '', '', '', '0;-0.88;0'])
        rows_art_resc.insert(line + 1,
                             [str(last_num + 2), 'mdl_battlePet_A' + str(num), '宠物展示模型_' + cn_name, '0', '模型',
                              'mdl_pet_' + en_name + '_lod0', '', '', '', '', '', '', '', '', '', '', '0;-0.88;0'])
        rows_art_resc.insert(line + 2,
                             [str(last_num + 3), 'mdl_battlePet_S' + str(num), '宠物展示模型_' + cn_name, '0', '模型',
                              'mdl_pet_' + en_name + '_lod0', '', '', '', '', '', '', '', '', '', '', '0;-0.88;0'])
        rows_art_resc.insert(line + 3,
                             [str(last_num + 4), 'mdlBG_battlePet_B' + str(num), '宠物展示背景_' + cn_name, '0', '模型',
                              'mdl_ui3d_background1', '', '', '', '', '', '', '', '', '', '', ''])
        rows_art_resc.insert(line + 4,
                             [str(last_num + 5), 'mdlBG_battlePet_A' + str(num), '宠物展示背景_' + cn_name, '0', '模型',
                              'mdl_ui3d_background1', '', '', '', '', '', '', '', '', '', '', ''])
        rows_art_resc.insert(line + 5,
                             [str(last_num + 6), 'mdlBG_battlePet_S' + str(num), '宠物展示背景_' + cn_name, '0', '模型',
                              'mdl_ui3d_background1', '', '', '', '', '', '', '', '', '', '', ''])
        rows_art_resc.insert(line + 6,
                             [str(last_num + 7), 'mdl_battlePet_B' + str(num) + '_wild', '宠物大地图模型_' + cn_name,
                              '0', '模型',
                              'mdl_pet_' + en_name + '_lod2', '', '', '', '', '', '', '', '', '', '', ''])
        rows_art_resc.insert(line + 7,
                             [str(last_num + 8), 'mdl_battlePet_A' + str(num) + '_wild', '宠物大地图模型_' + cn_name,
                              '0', '模型',
                              'mdl_pet_' + en_name + '_lod2', '', '', '', '', '', '', '', '', '', '', ''])
        rows_art_resc.insert(line + 8,
                             [str(last_num + 9), 'mdl_battlePet_S' + str(num) + '_wild', '宠物大地图模型_' + cn_name,
                              '0', '模型',
                              'mdl_pet_' + en_name + '_lod2', '', '', '', '', '', '', '', '', '', '', ''])
        last_num += 9
        line += 9

        with open('C:\ssr-config\\trunk\config\csv\ArtResource.csv', 'w', newline='',
                  encoding='utf-8') as art_resc_file:
            writer = csv.writer(art_resc_file)
            writer.writerows(rows_art_resc)

        for row in rows_pet:
            if row[4] == en_name:
                if row[7] == 'LV2':
                    row[13] = 'mdl_battlePet_B' + str(num)
                    row[14] = 'mdlBG_battlePet_B' + str(num)
                elif row[7] == 'LV3':
                    row[13] = 'mdl_battlePet_A' + str(num)
                    row[14] = 'mdlBG_battlePet_A' + str(num)
                elif row[7] == 'LV4':
                    row[13] = 'mdl_battlePet_S' + str(num)
                    row[14] = 'mdlBG_battlePet_S' + str(num)

        with open('C:\ssr-config\\trunk\config\csv\Pet.csv', 'w', newline='', encoding='utf-8') as pet_resc_file:
            writer = csv.writer(pet_resc_file)
            writer.writerows(rows_pet)


# if __name__ == '__main__':
    # 配置宠物模型资源
    # 输入格式：[[宠物1英文名，宠物1中文名], [宠物2英文名，宠物2中文名], ...]
    # add_pet_model()
