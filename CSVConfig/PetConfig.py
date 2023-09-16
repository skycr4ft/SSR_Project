import csv
import os.path


## 配置宠物模型
def add_pet_model(pets):
    art_resc_file = open('C:\ssr-config\\trunk\config\csv\ArtResource.csv', encoding='utf-8')
    reader_art_resc = csv.reader(art_resc_file)
    rows_art_resc = list(reader_art_resc)

    pet_file = open('C:\ssr-config\\trunk\config\csv\Pet.csv', encoding='utf-8')
    reader_pet = csv.reader(pet_file)
    rows_pet = list(reader_pet)

    # 读取ArtResource.csv文件中ID列值>=2000000且<3000000的最后一行
    for row in rows_art_resc:
        if row[0] < '2100000':
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
            if row[4] == cn_name:
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


## 添加宠物
def add_pet(pets):
    ## 在PetType.csv文件中添加宠物
    pet_type_file = open('C:\ssr-config\\trunk\config\csv\PetType.csv', encoding='utf-8')
    reader_pet_type = csv.reader(pet_type_file)
    rows_pet_type = list(reader_pet_type)

    last_row = rows_pet_type[-1]
    line = len(rows_pet_type)
    last_num = int(last_row[0])

    # for en_name, cn_name in pets:
    #     rows_pet_type.insert(line,
    #                          [str(last_num + 1), en_name, cn_name, 'icon_battlePet_C' + str(last_num - 100),
    #                           'battlePet_C' + str(last_num - 100),
    #                           '0.5;0.2;1.6;0.6', 'TRUE', '50', '0;0.85;0;1.34;1', ''])
    for en_name, cn_name in pets:
        rows_pet_type.insert(line,
                             [str(last_num + 1), en_name, cn_name, rows_pet_type[line - 1][3],
                              rows_pet_type[line - 1][4],
                              '0.5;0.2;1.6;0.6', 'TRUE', '50', '0;0.85;0;1.34;1', ''])

        line += 1
        last_num += 1

    ## 在Pet.csv文件中添加宠物
    pet_file = open('C:\ssr-config\\trunk\config\csv\Pet.csv', encoding='utf-8')
    reader_pet = csv.reader(pet_file)
    rows_pet = list(reader_pet)

    for pivot, quality in [['2000', 'B'], ['3000', 'A'], ['4000', 'S']]:
        for row in rows_pet:
            if row[0] < pivot:
                last_row = row
        line = 0
        for row in rows_pet:
            line += 1
            if row[0] == last_row[0]:
                break

        num = int(last_row[1].split(quality)[1])
        last_num = int(last_row[0])

        for en_name, cn_name in pets:
            num += 1
            rows_pet.insert(line,
                            [str(last_num + 1), 'battlePet_' + quality + str(num), cn_name, 'pet' + str(num) + '_name',
                             en_name, rows_pet[line - 1][5], rows_pet[line - 1][6], rows_pet[line - 1][7],
                             rows_pet[line - 1][8], rows_pet[line - 1][9], rows_pet[line - 1][10],
                             rows_pet[line - 1][11],
                             rows_pet[line - 1][12], rows_pet[line - 1][13], rows_pet[line - 1][14],
                             rows_pet[line - 1][15],
                             rows_pet[line - 1][16], rows_pet[line - 1][17], rows_pet[line - 1][18],
                             rows_pet[line - 1][19],
                             rows_pet[line - 1][20], rows_pet[line - 1][21], rows_pet[line - 1][22],
                             rows_pet[line - 1][23],
                             rows_pet[line - 1][24], rows_pet[line - 1][25], rows_pet[line - 1][26],
                             rows_pet[line - 1][27],
                             'Rank_battlePet_' + quality + str(num), rows_pet[line - 1][29], rows_pet[line - 1][30],
                             rows_pet[line - 1][31], ])
            line += 1
            last_num += 1

    ## 在PetRankAttr.csv文件中添加宠物
    pet_rank_attr_file = open('C:\ssr-config\\trunk\config\csv\PetRankAttr.csv', encoding='utf-8')
    reader_pet_rank_attr = csv.reader(pet_rank_attr_file)
    rows_pet_rank_attr = list(reader_pet_rank_attr)

    for pivot, quality in [['2000', 'B'], ['3000', 'A'], ['4000', 'S']]:
        for row in rows_pet_rank_attr:
            if row[0] < pivot:
                last_row = row
        line = 0
        for row in rows_pet_rank_attr:
            line += 1
            if row[0] == last_row[0]:
                break

        num = int(last_row[1].split(quality)[1].split('_')[0])
        last_num = int(last_row[0])

        for pet in pets:
            num += 1
            rows_pet_rank_attr.insert(line,
                                      [str(last_num + 1), 'Rank_battlePet_' + quality + str(num),
                                       'battlePet_' + quality + str(num), 'battlePet_' + quality + str(num),
                                       rows_pet_rank_attr[line - 1][4], rows_pet_rank_attr[line - 1][5],
                                       rows_pet_rank_attr[line - 1][6], rows_pet_rank_attr[line - 1][7],
                                       rows_pet_rank_attr[line - 1][8], rows_pet_rank_attr[line - 1][9],
                                       rows_pet_rank_attr[line - 1][10], rows_pet_rank_attr[line - 1][11],
                                       rows_pet_rank_attr[line - 1][12], rows_pet_rank_attr[line - 1][13],
                                       rows_pet_rank_attr[line - 1][14], rows_pet_rank_attr[line - 1][15],
                                       rows_pet_rank_attr[line - 1][16], rows_pet_rank_attr[line - 1][17],
                                       rows_pet_rank_attr[line - 1][18], rows_pet_rank_attr[line - 1][19],
                                       rows_pet_rank_attr[line - 1][20], rows_pet_rank_attr[line - 1][21],
                                       rows_pet_rank_attr[line - 1][22], rows_pet_rank_attr[line - 1][23],
                                       rows_pet_rank_attr[line - 1][24], rows_pet_rank_attr[line - 1][25],
                                       rows_pet_rank_attr[line - 1][26], rows_pet_rank_attr[line - 1][27],
                                       rows_pet_rank_attr[line - 1][28], rows_pet_rank_attr[line - 1][29],
                                       rows_pet_rank_attr[line - 1][30], rows_pet_rank_attr[line - 1][31],
                                       rows_pet_rank_attr[line - 1][32], rows_pet_rank_attr[line - 1][33],
                                       rows_pet_rank_attr[line - 1][34], rows_pet_rank_attr[line - 1][35],
                                       rows_pet_rank_attr[line - 1][36], rows_pet_rank_attr[line - 1][37],
                                       rows_pet_rank_attr[line - 1][38], rows_pet_rank_attr[line - 1][39],
                                       rows_pet_rank_attr[line - 1][40], rows_pet_rank_attr[line - 1][41],
                                       rows_pet_rank_attr[line - 1][42], rows_pet_rank_attr[line - 1][43],
                                       rows_pet_rank_attr[line - 1][44], ])
            line += 1
            last_num += 1

    ## 在PetRandomAttrBase.csv文件中添加宠物
    pet_random_attr_base_file = open('C:\ssr-config\\trunk\config\csv\PetRandomAttrBase.csv', encoding='utf-8')
    reader_pet_random_attr_base = csv.reader(pet_random_attr_base_file)
    rows_pet_random_attr_base = list(reader_pet_random_attr_base)

    quality_weight = {'S': 100, 'A': 10, 'B': 1}

    qs = []
    for q1 in ['B', 'A', 'S']:
        for q2 in ['B', 'A', 'S']:
            for q3 in ['B', 'A', 'S']:
                score = quality_weight[q1] + quality_weight[q2] + quality_weight[q3]
                qs.append([q1 + q2 + q3, score])
    qs = sorted(qs, key=lambda x: x[1])

    num = int(rows_pet_random_attr_base[-1][0])
    pet_num = int(rows_pet_random_attr_base[-1][1].split('_')[1].split('S')[0])
    for en_name, cn_name in pets:
        pet_num += 1
        for q in qs:
            if q[1] > 100:
                rarity = '超级超级稀有'
                quality = 'LV4'
            elif q[1] > 10:
                rarity = '超级稀有'
                quality = 'LV3'
            else:
                rarity = '稀有'
                quality = 'LV2'

            num += 1
            rows_pet_random_attr_base.append([num, 'petAttrBase_' + str(pet_num) + q[0], cn_name,
                                              en_name, rarity, '雄性', quality,
                                              q[0][0], q[0][1], q[0][2], 'attrtemp_battlePet_S4'])
    # print(rows_pet_random)

    with open('C:\ssr-config\\trunk\config\csv\PetType.csv', 'w', newline='', encoding='utf-8') as pet_type_file:
        writer = csv.writer(pet_type_file)
        writer.writerows(rows_pet_type)

    print('PetType.csv文件添加宠物成功！')

    with open('C:\ssr-config\\trunk\config\csv\Pet.csv', 'w', newline='', encoding='utf-8') as pet_file:
        writer = csv.writer(pet_file)
        writer.writerows(rows_pet)

    print('Pet.csv文件添加宠物成功！')

    with open('C:\ssr-config\\trunk\config\csv\PetRankAttr.csv', 'w', newline='',
              encoding='utf-8') as pet_rank_attr_file:
        writer = csv.writer(pet_rank_attr_file)
        writer.writerows(rows_pet_rank_attr)

    print('PetRankAttr.csv文件添加宠物成功！')

    with open('C:\ssr-config\\trunk\config\csv\PetRandomAttrBase.csv', 'w', newline='',
              encoding='utf-8') as pet_random_attr_base_file:
        writer = csv.writer(pet_random_attr_base_file)
        writer.writerows(rows_pet_random_attr_base)

    print('PetRandomAttrBase.csv文件添加宠物成功！')


def gen_petrandomattrbase():
    pet_type_file = open('C:\ssr-config\\trunk\config\csv\PetType.csv', encoding='utf-8')
    reader_pet_type = csv.reader(pet_type_file)
    rows_pet_type = list(reader_pet_type)
    pet_random_file = open('C:\ssr-config\\trunk\config\csv\PetRandomAttrBase.csv', encoding='utf-8')
    reader_pet_random = csv.reader(pet_random_file)
    rows_pet_random = list(reader_pet_random)
    rows_pet_random = rows_pet_random[:3]

    qs = []

    num = 100000
    n = 0
    l = [{'quality': 'B', 'group': ['B']}, {'quality': 'A', 'group': ['B', 'A']},
         {'quality': 'S', 'group': ['A', 'S']}]
    for row in rows_pet_type[3:]:
        n += 1
        for q in l:
            if q['quality'] == 'S':
                rarity = '超级超级稀有'
                quality = 'LV4'
            elif q['quality'] == 'A':
                rarity = '超级稀有'
                quality = 'LV3'
            else:
                rarity = '稀有'
                quality = 'LV2'

            for g1 in q['group']:
                for g2 in q['group']:
                    for g3 in q['group']:
                        num += 1
                        rows_pet_random.append([num, 'petAttrBase_' + str(num), row[2],
                                                row[1], rarity, '雄性', quality,
                                                g1, g2, g3, 'attrtemp_battlePet_' + q['quality'] + str(n)])

    # print(rows_pet_random)

    with open('C:\\Users\Administrator\Desktop\PetRandomAttrBase.csv', 'w', newline='',
              encoding='utf-8') as pet_random_attr_base_file:
        writer = csv.writer(pet_random_attr_base_file)
        writer.writerows(rows_pet_random)


def add_speed():
    # 读取AttrGroup-PetGenerate.csv文件
    attr_group_pet_generate_file = open('C:\ssr-config\\trunk\config\csv\AttrGroup-PetGenerate.csv', encoding='utf-8')
    reader_attr_group_pet_generate = csv.reader(attr_group_pet_generate_file)
    rows_attr_group_pet_generate = list(reader_attr_group_pet_generate)

    pet_speed = {'大嘴鸟': 1, '薮猫': 2, '蜜蜂': 1.5, '章鱼': 0, '熊': 0.5, '海豹': 1, '土拨鼠': 0.5, '野猪': 1,
                 '甲虫': 0.5, '熊猫': 0.5, '海鸥': 0.5, '卷尾猴': 0, '绿绿鹳': 0, '刺猬': 2, '狼': 2, '穿山甲': 0.5,
                 '牦牛': 1, '水豚': 0.5}
    speed_base = 200

    for row in rows_attr_group_pet_generate[3:]:
        row[22] = 'se速度_base'
        row[23] = str(int(speed_base * pet_speed[row[2]]))

    with open('C:\\Users\Administrator\Desktop\AttrGroup-PetGenerate.csv', 'w', newline='', encoding='utf-8') as attr_group_pet_generate_file:
        writer = csv.writer(attr_group_pet_generate_file)
        writer.writerows(rows_attr_group_pet_generate)


## 往AttrGropu-pet表填宠物属性系数
def pet_attr_factor():
    # 读取AttrGroup-PetGenerate.csv文件
    pet_attr_item = open('C:\ssr-config\\branches\sprint_0.6.0\config\csv\PetRandomAttrItem.csv', encoding='utf-8')
    reader_pet_attr_item = csv.reader(pet_attr_item)
    rows_pet_attr_item = list(reader_pet_attr_item)

    pets = ['海豹', '蜜蜂', '刺猬', '熊', '章鱼', '大嘴鸟', '水豚', '薮猫', '屎壳郎', '卷尾猴', '野猪', '熊猫', '狼', '海鸥',
            '土拨鼠', '绿绿鹳', '牦牛', '穿山甲']

    id = 0
    attr_quality = ['BBB', 'ABB', 'BAB', 'BBA', 'AAB', 'ABA', 'AAB', 'AAA', 'SAA', 'ASA', 'SAA', 'SSA', 'SAS', 'SSA',
                    'SSS']
    for pet in pets:

        for a_q in attr_quality:
            id += 1
            row[0] = id
            row[1] = 'battlePet_' + str(id)
            row[2] = a_q
            row[3] = str(int(int(row[3]) * pet_speed[row[2].split('A')[0]]))
            row[4] = str(int(int(row[4]) * pet_speed[row[2].split('A')[1]]))
            row[5] = str(int(int(row[5]) * pet_speed[row[2].split('A')[2]]))



    with open('C:\ssr-config\\branches\sprint_0.6.0\config\csv\PetRandomAttrItem.csv', 'w', newline='',
              encoding='utf-8') as pet_attr_item:
        writer = csv.writer(pet_attr_item)
        writer.writerows(rows_pet_attr_item)


if __name__ == '__main__':
    # 配置宠物模型资源
    # 输入格式：[[宠物1英文名，宠物1中文名], [宠物2英文名，宠物2中文名], ...]
    # add_pet_model([['panda', '狼'], ['panda', '海鸥'], ['marmot', '土拨鼠']])

    # 添加宠物
    # 输入格式：[[宠物1英文名，宠物1中文名], [宠物2英文名，宠物2中文名], ...]
    # add_pet([['pangolin', '穿山甲']])
    # gen_petrandomattrbase()
    # add_speed()
