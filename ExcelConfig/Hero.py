import xlwings as xw


## 获取所有品质的英雄的标准模板属性
def fetch_hero_level_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    blue_hero_atk = [int(val) for val in wb.sheets['英雄升级数值'].range('I3:I42').value]
    purple_hero_atk = [int(val) for val in wb.sheets['英雄升级数值'].range('M3:M42').value]
    orange_hero_atk = [int(val) for val in wb.sheets['英雄升级数值'].range('Q3:Q42').value]

    blue_hero_def = [int(val) for val in wb.sheets['英雄升级数值'].range('J3:J42').value]
    purple_hero_def = [int(val) for val in wb.sheets['英雄升级数值'].range('N3:N42').value]
    orange_hero_def = [int(val) for val in wb.sheets['英雄升级数值'].range('R3:R42').value]

    blue_hero_hp = [int(val) for val in wb.sheets['英雄升级数值'].range('K3:K42').value]
    purple_hero_hp = [int(val) for val in wb.sheets['英雄升级数值'].range('O3:O42').value]
    orange_hero_hp = [int(val) for val in wb.sheets['英雄升级数值'].range('S3:S42').value]

    return {'blue': {'atk': blue_hero_atk, 'def': blue_hero_def, 'hp': blue_hero_hp},
            'purple': {'atk': purple_hero_atk, 'def': purple_hero_def, 'hp': purple_hero_hp},
            'orange': {'atk': orange_hero_atk, 'def': orange_hero_def, 'hp': orange_hero_hp}}


## 获取所有英雄的属性偏移量
def fetch_hero_offset(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    hero_offset = {}
    for row in wb.sheets['英雄升级数值'].range('A46:F60').value:
        hero_offset[row[0]] = {'name': row[0], 'quality': row[1], 'atk': row[2], 'def': row[3], 'hp': row[4]}
    return hero_offset


## 获取所有英雄的升星数值
def fetch_hero_star_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    blue_hero_star_crit = [int(val) for val in wb.sheets['英雄升星数值'].range('C3:C8').value]
    purple_hero_star_crit = [int(val) for val in wb.sheets['英雄升星数值'].range('J3:J8').value]
    orange_hero_star_crit = [int(val) for val in wb.sheets['英雄升星数值'].range('Q3:Q8').value]

    blue_hero_star_crit_res = [int(val) for val in wb.sheets['英雄升星数值'].range('D3:D8').value]
    purple_hero_star_crit_res = [int(val) for val in wb.sheets['英雄升星数值'].range('K3:K8').value]
    orange_hero_star_crit_res = [int(val) for val in wb.sheets['英雄升星数值'].range('R3:R8').value]

    blue_hero_star_eff_hit = [val for val in wb.sheets['英雄升星数值'].range('E3:E8').value]
    purple_hero_star_eff_hit = [val for val in wb.sheets['英雄升星数值'].range('L3:L8').value]
    orange_hero_star_eff_hit = [val for val in wb.sheets['英雄升星数值'].range('S3:S8').value]

    blue_hero_star_eff_res = [val for val in wb.sheets['英雄升星数值'].range('F3:F8').value]
    purple_hero_star_eff_res = [val for val in wb.sheets['英雄升星数值'].range('M3:M8').value]
    orange_hero_star_eff_res = [val for val in wb.sheets['英雄升星数值'].range('T3:T8').value]

    blue_hero_star_base_attr = [val for val in wb.sheets['英雄升星数值'].range('G3:G8').value]
    purple_hero_star_base_attr = [val for val in wb.sheets['英雄升星数值'].range('N3:N8').value]
    orange_hero_star_base_attr = [val for val in wb.sheets['英雄升星数值'].range('U3:U8').value]

    return {'blue': {'crit': blue_hero_star_crit, 'crit_res': blue_hero_star_crit_res,
                     'eff_hit': blue_hero_star_eff_hit, 'eff_res': blue_hero_star_eff_res,
                     'base_attr': blue_hero_star_base_attr},
            'purple': {'crit': purple_hero_star_crit, 'crit_res': purple_hero_star_crit_res,
                       'eff_hit': purple_hero_star_eff_hit, 'eff_res': purple_hero_star_eff_res,
                       'base_attr': purple_hero_star_base_attr},
            'orange': {'crit': orange_hero_star_crit, 'crit_res': orange_hero_star_crit_res,
                       'eff_hit': orange_hero_star_eff_hit, 'eff_res': orange_hero_star_eff_res,
                       'base_attr': orange_hero_star_base_attr}}


def fetch_attr_weight(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    atk = wb.sheets['战力关系'].range('B2').value
    _def = wb.sheets['战力关系'].range('B3').value
    hp = wb.sheets['战力关系'].range('B4').value
    crit = wb.sheets['战力关系'].range('B5').value
    crit_res = wb.sheets['战力关系'].range('B6').value
    eff_hit = wb.sheets['战力关系'].range('B7').value
    eff_res = wb.sheets['战力关系'].range('B8').value
    crit_dmg = wb.sheets['战力关系'].range('B9').value
    crit_dmg_res = wb.sheets['战力关系'].range('B10').value

    return {'atk': atk, 'def': _def, 'hp': hp, 'crit': crit, 'crit_res': crit_res, 'eff_hit': eff_hit,
            'eff_res': eff_res, 'crit_dmg': crit_dmg, 'crit_dmg_res': crit_dmg_res}


def fetch_hero_item_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    blue_t1_power = wb.sheets['英雄装备数值'].range('D3').value
    purple_t1_power = wb.sheets['英雄装备数值'].range('D4').value
    orange_t1_power = wb.sheets['英雄装备数值'].range('D5').value
    blue_t2_power = blue_t1_power * 5 / 3
    purple_t2_power = purple_t1_power * 5 / 3
    orange_t2_power = orange_t1_power * 5 / 3

    atk_prop = wb.sheets['英雄装备数值'].range('D42').value
    def_prop = wb.sheets['英雄装备数值'].range('D43').value
    hp_prop = wb.sheets['英雄装备数值'].range('D44').value
    crit_prop = wb.sheets['英雄装备数值'].range('D45').value
    crit_res_prop = wb.sheets['英雄装备数值'].range('D46').value
    eff_hit_prop = wb.sheets['英雄装备数值'].range('D47').value
    eff_res_prop = wb.sheets['英雄装备数值'].range('D48').value

    return {'blue': {'t1_power': blue_t1_power, 't2_power': blue_t2_power},
            'purple': {'t1_power': purple_t1_power, 't2_power': purple_t2_power},
            'orange': {'t1_power': orange_t1_power, 't2_power': orange_t2_power}}, \
        {'atk_prop': atk_prop, 'def_prop': def_prop, 'hp_prop': hp_prop, 'crit_prop': crit_prop,
         'crit_res_prop': crit_res_prop, 'eff_hit_prop': eff_hit_prop, 'eff_res_prop': eff_res_prop}


def fetch_item_boost_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    # print(wb.sheets['装备强化数值'].range('B3:B22').value)
    return wb.sheets['装备强化数值'].range('B3:B22').value


def fetch_pet_level_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    blue_pet_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('C3:C42').value]
    purple_pet_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('M3:M42').value]
    orange_pet_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Q3:Q42').value]

    blue_pet_crit = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('D3:D42').value]
    purple_pet_crit = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('N3:N42').value]
    orange_pet_crit = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('X3:X42').value]

    blue_pet_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('E3:E42').value]
    purple_pet_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('O3:O42').value]
    orange_pet_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Y3:Y42').value]

    blue_pet_crit_res = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('F3:F42').value]
    purple_pet_crit_res = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('P3:P42').value]
    orange_pet_crit_res = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Z3:Z42').value]

    blue_pet_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('G3:G42').value]
    purple_pet_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Q3:Q42').value]
    orange_pet_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AA3:AA42').value]

    blue_pet_slg_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('H3:H42').value]
    purple_pet_slg_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('R3:R42').value]
    orange_pet_slg_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AB3:AB42').value]

    blue_pet_slg_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('I3:I42').value]
    purple_pet_slg_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('S3:S42').value]
    orange_pet_slg_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AC3:AC42').value]

    blue_pet_slg_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('J3:J42').value]
    purple_pet_slg_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('T3:T42').value]
    orange_pet_slg_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AD3:AD42').value]

    return {'blue': {'atk': blue_pet_atk, 'crit': blue_pet_crit, 'def': blue_pet_def, 'crit_res': blue_pet_crit_res,
                     'hp': blue_pet_hp, 'slg_atk': blue_pet_slg_atk, 'slg_def': blue_pet_slg_def,
                     'slg_hp': blue_pet_slg_hp},
            'purple': {'atk': purple_pet_atk, 'crit': purple_pet_crit, 'def': purple_pet_def,
                       'crit_res': purple_pet_crit_res, 'hp': purple_pet_hp, 'slg_atk': purple_pet_slg_atk,
                       'slg_def': purple_pet_slg_def, 'slg_hp': purple_pet_slg_hp},
            'orange': {'atk': orange_pet_atk, 'crit': orange_pet_crit, 'def': orange_pet_def,
                       'crit_res': orange_pet_crit_res, 'hp': orange_pet_hp, 'slg_atk': orange_pet_slg_atk,
                       'slg_def': orange_pet_slg_def, 'slg_hp': orange_pet_slg_hp}}


def fetch_pet_rank_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    return wb.sheets['宠物升阶数值'].range('B2:B31').value


class Numerical:
    ## 初次获取养成数值数据
    # def __init__(self, filepath):
    #     self.filepath = filepath
    #     self.hero_level_attr = fetch_hero_level_attr(self.filepath)
    #     print('英雄升级数值读取完毕')
    #     print(self.hero_level_attr)
    #     self.hero_offset = fetch_hero_offset(self.filepath)
    #     print('英雄属性偏移量读取完毕')
    #     print(self.hero_offset)
    #     self.hero_star = fetch_hero_star_attr(self.filepath)
    #     print('英雄升星数值读取完毕')
    #     print(self.hero_star)
    #     self.attr_weight = fetch_attr_weight(self.filepath)
    #     print('属性权重读取完毕')
    #     print(self.attr_weight)
    #     self.item_qlt_power, self.item_attr_prop = fetch_hero_item_attr(self.filepath)
    #     print('英雄装备数值读取完毕')
    #     print(self.item_qlt_power)
    #     print(self.item_attr_prop)
    #     self.item_boost_attr = fetch_item_boost_attr(self.filepath)
    #     print('英雄装备强化数值读取完毕')
    #     print(self.item_boost_attr)
    #     self.pet_level_attr = fetch_pet_level_attr(self.filepath)
    #     print('宠物升级数值读取完毕')
    #     print(self.pet_level_attr)
    #     self.pet_rank_attr = fetch_pet_rank_attr(self.filepath)
    #     print('宠物升阶数值读取完毕')
    #     print(self.pet_rank_attr)

    def __init__(self):
        self.hero_level_attr = \
            {'blue': {
                'atk': [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 56, 59, 62, 65,
                        68,
                        71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113],
                'def': [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 56, 59, 62, 65,
                        68,
                        71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113],
                'hp': [125, 141, 158, 175, 191, 208, 225, 241, 258, 275, 291, 308, 325, 341, 358, 375, 391, 408, 425,
                       441,
                       466, 491, 516, 541, 566, 591, 616, 641, 666, 691, 716, 741, 766, 791, 816, 841, 866, 891, 916,
                       941]},
                'purple': {
                    'atk': [24, 26, 28, 30, 33, 35, 37, 40, 42, 44, 47, 49, 52, 54, 57, 60, 62, 65, 67, 70, 74, 78, 82,
                            86, 90,
                            94, 98, 102, 106, 110, 114, 118, 122, 126, 130, 134, 138, 142, 146, 150],
                    'def': [24, 26, 28, 30, 33, 35, 37, 40, 42, 44, 47, 49, 52, 54, 57, 60, 62, 65, 67, 70, 74, 78, 82,
                            86, 90,
                            94, 98, 102, 106, 110, 114, 118, 122, 126, 130, 134, 138, 142, 146, 150],
                    'hp': [200, 216, 234, 255, 275, 295, 314, 333, 353, 374, 393, 416, 438, 457, 480, 502, 520, 543,
                           565, 587,
                           620, 653, 687, 720, 753, 786, 820, 853, 886, 919, 953, 986, 1019, 1052, 1086, 1119, 1152,
                           1185,
                           1219, 1252]},
                'orange': {
                    'atk': [33, 35, 38, 41, 45, 48, 51, 55, 58, 61, 65, 68, 71, 75, 78, 81, 85, 89, 92, 95, 101, 106,
                            111, 117,
                            122, 127, 133, 138, 144, 149, 154, 160, 165, 171, 176, 181, 187, 192, 198, 203],
                    'def': [33, 35, 38, 41, 45, 48, 51, 55, 58, 61, 65, 68, 71, 75, 78, 81, 85, 89, 92, 95, 101, 106,
                            111, 117,
                            122, 127, 133, 138, 144, 149, 154, 160, 165, 171, 176, 181, 187, 192, 198, 203],
                    'hp': [275, 297, 319, 346, 375, 404, 432, 459, 485, 514, 542, 570, 598, 625, 652, 682, 712, 743,
                           769, 799,
                           844, 889, 930, 975, 1020, 1065, 1110, 1155, 1200, 1245, 1290, 1335, 1380, 1425, 1470, 1515,
                           1560,
                           1605, 1650, 1695]}}
        self.hero_offset = {'杰玛': {'name': '杰玛', 'quality': 1.0, 'atk': 1.1, 'def': 1.0, 'hp': 0.9},
                            '按摩师': {'name': '按摩师', 'quality': 1.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '东': {'name': '东', 'quality': 1.0, 'atk': 0.75, 'def': 1.1, 'hp': 1.15},
                            '奈乔': {'name': '奈乔', 'quality': 2.0, 'atk': 1.1, 'def': 0.95, 'hp': 0.95},
                            '苏西': {'name': '苏西', 'quality': 2.0, 'atk': 0.85, 'def': 1.05, 'hp': 1.1},
                            '金鼻子': {'name': '金鼻子', 'quality': 2.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '街头艺术家': {'name': '街头艺术家', 'quality': 2.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '女医生': {'name': '女医生', 'quality': 2.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '审判长': {'name': '审判长', 'quality': 2.0, 'atk': 1.05, 'def': 0.95, 'hp': 1.0},
                            '南希': {'name': '南希', 'quality': 3.0, 'atk': 1.1, 'def': 0.9, 'hp': 1.0},
                            '华特': {'name': '华特', 'quality': 3.0, 'atk': 0.75, 'def': 1.1, 'hp': 1.15},
                            '杰登': {'name': '杰登', 'quality': 3.0, 'atk': 1.2, 'def': 0.9, 'hp': 0.9},
                            '大鹅': {'name': '大鹅', 'quality': 3.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '吉尔伯特': {'name': '吉尔伯特', 'quality': 3.0, 'atk': 1.1, 'def': 0.95, 'hp': 0.95},
                            'E-girl': {'name': 'E-girl', 'quality': 3.0, 'atk': 1.15, 'def': 0.9, 'hp': 0.95}}
        self.hero_star = {
            'blue': {'crit': [15, 30, 45, 60, 75, 90], 'crit_res': [15, 30, 45, 60, 75, 90],
                     'eff_hit': [0.09, 0.18, 0.27, 0.36, 0.45, 0.54],
                     'eff_res': [0.06749999999999999, 0.13499999999999998, 0.20249999999999999,
                                 0.26999999999999996, 0.33749999999999997, 0.40499999999999997],
                     'base_attr': [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]},
            'purple': {'crit': [18, 37, 56, 75, 93, 112], 'crit_res': [18, 37, 56, 75, 93, 112],
                       'eff_hit': [0.11249999999999999, 0.22499999999999998, 0.3375, 0.44999999999999996,
                                   0.5625, 0.675],
                       'eff_res': [0.08437499999999999, 0.16874999999999998, 0.253125,
                                   0.33749999999999997, 0.42187499999999994, 0.50625],
                       'base_attr': [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]},
            'orange': {'crit': [24, 48, 72, 96, 120, 144], 'crit_res': [24, 48, 72, 96, 120, 144],
                       'eff_hit': [0.144, 0.288, 0.43200000000000005, 0.576, 0.7200000000000001,
                                   0.8640000000000001],
                       'eff_res': [0.10799999999999998, 0.21599999999999997, 0.324, 0.43199999999999994,
                                   0.5399999999999999, 0.648],
                       'base_attr': [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]}}
        self.attr_weight = {'atk': 5.0, 'def': 5.0, 'hp': 0.6, 'crit': 5.0, 'crit_res': 5.0, 'eff_hit': 500.0,
                            'eff_res': 500.0, 'crit_dmg': 1000.0, 'crit_dmg_res': 1000.0}
        self.item_qlt_power = {'blue': {'t1_power': 180.0, 't2_power': 300.0},
                               'purple': {'t1_power': 270.0, 't2_power': 450.0},
                               'orange': {'t1_power': 360.0, 't2_power': 600.0}}
        self.item_attr_prop = {'atk_prop': 0.2, 'def_prop': 0.2, 'hp_prop': 0.2, 'crit_prop': 0.1111111111111111,
                               'crit_res_prop': 0.08888888888888889, 'eff_hit_prop': 0.1111111111111111,
                               'eff_res_prop': 0.08888888888888889}
        self.item_boost_attr = [30.0, 60.0, 90.0, 120.0, 150.0, 180.0, 210.0, 240.0, 270.0, 300.0, 330.0, 360.0, 390.0,
                                420.0, 450.0, 480.0, 510.0, 540.0, 570.0, 600.0]
        self.pet_level_attr = {
            'blue': {
                'atk': [6, 7, 8, 9, 11, 13, 15, 16, 18, 20, 22, 24, 25, 27, 29, 31, 33, 34, 36, 38, 40, 42, 43, 45, 47,
                        49,
                        51, 52, 54, 56, 58, 60, 61, 63, 65, 67, 69, 70, 72, 74],
                'crit': [2, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 13, 14, 14, 15, 15, 16, 17, 17,
                         18,
                         18, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 25],
                'def': [6, 7, 8, 9, 11, 13, 15, 16, 18, 20, 22, 24, 25, 27, 29, 31, 33, 34, 36, 38, 40, 42, 43, 45, 47,
                        49,
                        51, 52, 54, 56, 58, 60, 61, 63, 65, 67, 69, 70, 72, 74],
                'crit_res': [2, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 13, 14, 14, 15, 15, 16, 17,
                             17,
                             18, 18, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 25],
                'hp': [240, 280, 320, 360, 440, 520, 600, 640, 720, 800, 880, 960, 1000, 1080, 1160, 1240, 1320, 1360,
                       1440,
                       1520, 1600, 1680, 1720, 1800, 1880, 1960, 2040, 2080, 2160, 2240, 2320, 2400, 2440, 2520, 2600,
                       2680,
                       2760, 2800, 2880, 2960],
                'slg_atk': [3, 4, 4, 5, 6, 7, 9, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 25, 27, 28,
                            29,
                            30, 31, 32, 33, 34, 36, 36, 37, 39, 40, 41, 42, 43, 44],
                'slg_def': [3, 4, 4, 5, 6, 7, 9, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 25, 27, 28,
                            29,
                            30, 31, 32, 33, 34, 36, 36, 37, 39, 40, 41, 42, 43, 44],
                'slg_hp': [107, 126, 144, 161, 198, 234, 270, 288, 323, 360, 396, 431, 450, 486, 522, 557, 594, 612,
                           647,
                           684, 720, 756, 774, 810, 846, 882, 917, 936, 972, 1008, 1044, 1080, 1098, 1134, 1170, 1205,
                           1242,
                           1260, 1295, 1332]}, 'purple': {
                'atk': [7, 9, 10, 11, 14, 16, 19, 20, 23, 26, 28, 31, 32, 35, 37, 40, 42, 44, 46, 49, 52, 54, 55, 58,
                        61,
                        63, 66, 67, 70, 72, 75, 78, 79, 81, 84, 87, 89, 91, 93, 96],
                'crit': [2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20, 21, 22,
                         23,
                         23, 24, 25, 26, 27, 27, 28, 29, 30, 31, 31, 32, 33],
                'def': [7, 9, 10, 11, 14, 16, 19, 20, 23, 26, 28, 31, 32, 35, 37, 40, 42, 44, 46, 49, 52, 54, 55, 58,
                        61,
                        63, 66, 67, 70, 72, 75, 78, 79, 81, 84, 87, 89, 91, 93, 96],
                'crit_res': [2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20, 21,
                             22,
                             23, 23, 24, 25, 26, 27, 27, 28, 29, 30, 31, 31, 32, 33],
                'hp': [312, 364, 416, 468, 572, 676, 780, 832, 936, 1040, 1144, 1248, 1300, 1404, 1508, 1612, 1716,
                       1768,
                       1872, 1976, 2080, 2184, 2236, 2340, 2444, 2548, 2652, 2704, 2808, 2912, 3016, 3120, 3172, 3276,
                       3380,
                       3484, 3588, 3640, 3744, 3848],
                'slg_atk': [4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19, 21, 22, 24, 25, 26, 28, 29, 31, 32, 33, 35,
                            36,
                            38, 39, 40, 42, 43, 45, 46, 47, 49, 50, 52, 53, 54, 56, 57],
                'slg_def': [4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19, 21, 22, 24, 25, 26, 28, 29, 31, 32, 33, 35,
                            36,
                            38, 39, 40, 42, 43, 45, 46, 47, 49, 50, 52, 53, 54, 56, 57],
                'slg_hp': [140, 163, 187, 210, 257, 304, 351, 374, 421, 468, 514, 561, 585, 631, 678, 725, 772, 795,
                           842,
                           889, 936, 982, 1006, 1053, 1099, 1146, 1193, 1216, 1263, 1310, 1357, 1404, 1427, 1474, 1521,
                           1567, 1614, 1638, 1684, 1731]}, 'orange': {
                'atk': [312, 364, 416, 468, 572, 676, 780, 832, 936, 1040, 1144, 1248, 1300, 1404, 1508, 1612, 1716,
                        1768,
                        1872, 1976, 2080, 2184, 2236, 2340, 2444, 2548, 2652, 2704, 2808, 2912, 3016, 3120, 3172, 3276,
                        3380, 3484, 3588, 3640, 3744, 3848],
                'crit': [3, 4, 4, 5, 6, 7, 9, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20, 20, 22, 23, 24, 25, 26, 27, 28, 30,
                         31,
                         31, 33, 34, 35, 36, 37, 38, 39, 41, 42, 42, 44, 45],
                'def': [10, 12, 14, 15, 19, 22, 26, 28, 31, 35, 38, 42, 43, 47, 50, 54, 57, 59, 63, 66, 70, 73, 75, 78,
                        82,
                        85, 89, 91, 94, 98, 101, 105, 106, 110, 113, 117, 120, 122, 126, 129],
                'crit_res': [3, 4, 4, 5, 6, 7, 9, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20, 20, 22, 23, 24, 25, 26, 27, 28,
                             30,
                             31, 31, 33, 34, 35, 36, 37, 38, 39, 41, 42, 42, 44, 45],
                'hp': [420, 490, 560, 630, 770, 910, 1050, 1120, 1260, 1400, 1540, 1680, 1750, 1890, 2030, 2170, 2310,
                       2380,
                       2520, 2660, 2800, 2940, 3010, 3150, 3290, 3430, 3570, 3640, 3780, 3920, 4060, 4200, 4270, 4410,
                       4550,
                       4690, 4830, 4900, 5040, 5180],
                'slg_atk': [6, 7, 8, 9, 11, 13, 15, 16, 18, 21, 23, 25, 26, 28, 30, 32, 34, 35, 37, 39, 42, 44, 45, 47,
                            49,
                            51, 53, 54, 56, 58, 60, 63, 64, 66, 68, 70, 72, 73, 75, 77],
                'slg_def': [6, 7, 8, 9, 11, 13, 15, 16, 18, 21, 23, 25, 26, 28, 30, 32, 34, 35, 37, 39, 42, 44, 45, 47,
                            49,
                            51, 53, 54, 56, 58, 60, 63, 64, 66, 68, 70, 72, 73, 75, 77],
                'slg_hp': [188, 220, 252, 283, 346, 409, 472, 504, 566, 630, 693, 755, 787, 850, 913, 976, 1039, 1071,
                           1133,
                           1197, 1260, 1323, 1354, 1417, 1480, 1543, 1606, 1638, 1701, 1764, 1827, 1890, 1921, 1984,
                           2047,
                           2110, 2173, 2205, 2267, 2331]}}
        self.pet_rank_attr = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8,
                              0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5]

    def calc_hero_attr(self, hero, level, star, quality, item_qlt, item_tier, item_num, item_boost, pet_qlt, pet_lvl, pet_star):
        atk = self.hero_offset[hero]['atk'] * self.hero_level_attr[quality]['atk'][level - 1] * \
              (1 + self.hero_star[quality]['base_attr'][star - 1]) + self.item_qlt_power[item_qlt][item_tier] * \
              item_num * self.item_attr_prop['atk_prop'] / self.attr_weight['atk'] + \
              self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['atk'] + \
              self.pet_level_attr[pet_qlt]['slg_atk'][pet_lvl - 1] * (1 + self.pet_rank_attr[pet_star - 1])

        _def = self.hero_offset[hero]['def'] * self.hero_level_attr[quality]['def'][level - 1] * \
               (1 + self.hero_star[quality]['base_attr'][star - 1]) + self.item_qlt_power[item_qlt][item_tier] * \
               item_num * self.item_attr_prop['def_prop'] / self.attr_weight['def'] + \
               self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['def'] + \
               self.pet_level_attr[pet_qlt]['slg_def'][pet_lvl - 1] * (1 + self.pet_rank_attr[pet_star - 1])

        print(self.hero_offset[hero]['hp'], self.hero_level_attr[quality]['hp'][level - 1],
              self.hero_star[quality]['base_attr'][star - 1], self.item_qlt_power[item_qlt][item_tier],
              item_num, self.item_attr_prop['hp_prop'], self.attr_weight['hp'], self.item_boost_attr[item_boost - 1],
              self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1], self.pet_rank_attr[pet_star - 1])
        hp = self.hero_offset[hero]['hp'] * self.hero_level_attr[quality]['hp'][level - 1] * \
             (1 + self.hero_star[quality]['base_attr'][star - 1]) + self.item_qlt_power[item_qlt][item_tier] * \
             item_num * self.item_attr_prop['hp_prop'] / self.attr_weight['hp'] + \
             self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['hp'] + \
             self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1] * (1 + self.pet_rank_attr[pet_star - 1])

        crit = self.hero_star[quality]['crit'][star - 1] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
               self.item_attr_prop['crit_prop'] / self.attr_weight['crit']

        crit_res = self.hero_star[quality]['crit_res'][star - 1] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
                   self.item_attr_prop['crit_res_prop'] / self.attr_weight['crit_res']

        eff_hit = self.hero_star[quality]['eff_hit'][star - 1] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
                  self.item_attr_prop['eff_hit_prop'] / self.attr_weight['eff_hit']

        eff_res = self.hero_star[quality]['eff_res'][star - 1] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
                  self.item_attr_prop['eff_res_prop'] / self.attr_weight['eff_res']

        return atk, _def, hp, crit, crit_res, eff_hit, eff_res


if __name__ == '__main__':
    hero_info = {'hero': '奈乔', 'level': 40, 'star': 5, 'quality': 'orange', 'item_qlt': 'orange',
                 'item_tier': 't2_power', 'item_num': 5,
                 'item_boost': 10, 'pet_qlt': 'orange', 'pet_lvl': 40, 'pet_star': 11}
    # hero_getter = Numerical('E:\游戏设计\SSR\SSR战斗养成数值（7day）.xlsx')
    hero_getter = Numerical()
    print(hero_getter.calc_hero_attr(**hero_info))
