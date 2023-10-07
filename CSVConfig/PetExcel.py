import xlwings as xw
import csv


def pet_attr_cfg(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    pet_attr = open('C:\ssr-config\\branches\sprint_0.6.0\config\csv\AttrGroup-pet.csv', encoding='utf-8')
    reader_pet_attr = csv.reader(pet_attr)
    rows_pet_attr = list(reader_pet_attr)

    pet_atk = [int(val) for val in wb.sheets['AttrGroup-pet'].range('F1:F18').value]
    pet_def = [int(val) for val in wb.sheets['AttrGroup-pet'].range('F19:F36').value]
    pet_hp = [int(val) for val in wb.sheets['AttrGroup-pet'].range('F37:F54').value]
    pet_crt = [int(val) for val in wb.sheets['AttrGroup-pet'].range('H1:H18').value]
    pet_crt_res = [int(val) for val in wb.sheets['AttrGroup-pet'].range('H19:H36').value]
    pet_slg_hp = [int(val) for val in wb.sheets['AttrGroup-pet'].range('H37:H54').value]
    pet_slg_atk = [int(val) for val in wb.sheets['AttrGroup-pet'].range('J1:J18').value]
    pet_slg_def = [int(val) for val in wb.sheets['AttrGroup-pet'].range('J19:J36').value]

    attr_offset = {'B': 1.0, 'A': 1.15, 'S': 1.4}
    power_offset = {'B': 0, 'A': 500, 'S': 1300}

    pets = ['海豹', '蜜蜂', '刺猬', '熊', '章鱼', '大嘴鸟', '水豚', '薮猫', '屎壳郎', '卷尾猴', '野猪', '熊猫', '狼',
            '海鸥', '土拨鼠', '绿绿鹳', '牦牛', '穿山甲']
    pets_speed = [0, 0.5, 1, -0.5, -1, 0, 0, 1, -1, -1, 0, -0.5, 0, -0.5, -0.5, -1, 0, -0.5]

    attr_ctgr_quality = ['B', 'A', 'S']
    attr_ctgr = ['_Attr1_', '_Attr2_', '_Attr3_']
    map_attr_ctgr = {'_Attr1_': ['攻击_multi', '暴击率_multi', '宠物提供的攻击_multi'],
                     '_Attr2_': ['防御_multi', '暴击抵抗_multi', '宠物提供的防御_multi'],
                     '_Attr3_': ['血量_multi', '宠物提供的血量_multi', 'se速度_multi']}
    id = 6710000

    for i in range(len(pets)):
        for a_c in attr_ctgr:
            for k in range(len(attr_ctgr_quality)):
                id += 1
                row = []
                row.append(id)
                row.append('battlePet_' + str(i + 1) + a_c + attr_ctgr_quality[k])
                row.append('')
                row.append('Factor')

                if a_c == '_Attr1_':
                    row.append('攻击_multi')
                    row.append((pet_atk[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('暴击率_multi')
                    row.append((pet_crt[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('宠物提供的攻击_multi')
                    row.append((pet_slg_atk[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('战力_multi')
                    row.append(power_offset[attr_ctgr_quality[k]])
                elif a_c == '_Attr2_':
                    row.append('防御_multi')
                    row.append((pet_def[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('暴击抵抗_multi')
                    row.append((pet_crt_res[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('宠物提供的防御_multi')
                    row.append((pet_slg_def[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('战力_multi')
                    row.append(power_offset[attr_ctgr_quality[k]])
                elif a_c == '_Attr3_':
                    row.append('血量_multi')
                    row.append((pet_hp[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('宠物提供的血量_multi')
                    row.append((pet_slg_hp[i] / 100.0 * attr_offset[attr_ctgr_quality[k]] - 1) * 10000)
                    row.append('se速度_multi')
                    row.append(pets_speed[i] * 10000)
                    row.append('战力_multi')
                    row.append(power_offset[attr_ctgr_quality[k]])

                for l in range(2 * (30 - len(map_attr_ctgr[a_c]))):
                    row.append('')

                rows_pet_attr.append(row)

    with open('C:\\Users\Administrator\Desktop\AttrGroup-pet.csv', 'w', newline='',
              encoding='utf-8') as pet_attr_item:
        writer = csv.writer(pet_attr_item)
        writer.writerows(rows_pet_attr)


if __name__ == '__main__':
    pet_attr_cfg('C:\\Users\Administrator\Desktop\AttrGroup-pet.xlsx')
