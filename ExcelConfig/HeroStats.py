import xlwings as xw
import ExcelConfig.HeroSkillConfig as HeroSkillConfig

Hero_level = [[8, 4, 1, 0, 0, 0],
              [9, 3, 1, 0, 0, 0],
              [10, 4, 2, 1, 0, 0],
              [10, 4, 2, 2, 0, 0],
              [11, 5, 3, 3, 0, 0],
              [12, 6, 4, 4, 1, 0],
              [13, 7, 5, 5, 2, 0],
              [14, 8, 6, 6, 3, 0],
              [15, 9, 7, 7, 4, 1],
              [16, 10, 8, 8, 5, 2],
              [17, 11, 9, 9, 6, 3],
              [19, 13, 11, 10, 7, 4],
              [21, 15, 13, 11, 8, 5],
              [23, 17, 15, 12, 9, 6],
              [25, 19, 17, 13, 10, 7],
              [27, 21, 19, 14, 11, 8],
              [29, 23, 21, 15, 12, 9],
              [31, 25, 23, 16, 13, 10],
              [33, 27, 25, 17, 14, 11],
              [35, 29, 27, 18, 15, 12],
              [37, 31, 29, 19, 16, 13],
              [39, 33, 31, 20, 17, 14],
              [41, 35, 33, 21, 18, 15], ]

Hero_Skills = {
    '白板': HeroSkillConfig.Monster1_skills,
    # 蓝色
    '杰玛': HeroSkillConfig.Gem_skills,
    '东': HeroSkillConfig.Don_skills,
    '按摩师': HeroSkillConfig.Massager_skills,
    # 紫色
    '奈乔': HeroSkillConfig.Nitro_skills,
    '金鼻子': HeroSkillConfig.GoldenNose_skills,
    '苏茜': HeroSkillConfig.Susie_skills,
    '女医生': HeroSkillConfig.FemaleDoctor_skill,
    '街头艺术家': HeroSkillConfig.Artist_skill,
    '审判长': HeroSkillConfig.Judge_skill,
    # 橙色
    '华特': HeroSkillConfig.Watt_skill,
    '杰登': HeroSkillConfig.Jaden_skill,
    '大鹅': HeroSkillConfig.Singer_skill,
    '吉尔伯特': HeroSkillConfig.Gilbert_skill,
    'E-girl': HeroSkillConfig.Egirl_skill,
    # '硬汉': HeroSkillConfig.HardMan_skill,
    '南希': HeroSkillConfig.Nancy_skill,
}

Heroes_qlt = {
    '白板': 'blue',
    # 蓝色
    '杰玛': 'blue',
    '东': 'blue',
    '按摩师': 'blue',
    # 紫色
    '奈乔': 'purple',
    '金鼻子': 'purple',
    '苏茜': 'purple',
    '女医生': 'purple',
    '街头艺术家': 'purple',
    # 橙色
    '南希': 'orange',
    '华特': 'orange',
    '杰登': 'orange',
    '大鹅': 'orange',
    '吉尔伯特': 'orange',
    'E-girl': 'orange',
    '硬汉': 'orange',
    '审判长': 'orange',
}

Heroes = {
    'blue': ['杰玛', '东', '按摩师'],
    'purple': ['奈乔', '金鼻子', '苏茜', '女医生', '街头艺术家', ],
    'orange': ['审判长', ]
}

active_hero_progress = [
    [{'quality': 'orange', 'level': 20, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 3.0,
      'item_boost': 0, 'pet_qlt': 'purple', 'pet_lvl': 8, 'pet_star': 3},
     {'quality': 'purple', 'level': 20, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'orange', 'item_num': 0.0,
      'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 13, 'pet_star': 3},
     {'quality': 'blue', 'level': 20, 'star': 0, 'item_tier': 't1_power', 'item_qlt': 'orange', 'item_num': 0.0,
      'item_boost': 0, 'pet_qlt': 'blue', 'pet_lvl': 13, 'pet_star': 1}], [
        {'quality': 'orange', 'level': 22, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 4.0,
         'item_boost': 0, 'pet_qlt': 'purple', 'pet_lvl': 9, 'pet_star': 4},
        {'quality': 'purple', 'level': 22, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'orange', 'item_num': 0.0,
         'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 14, 'pet_star': 3},
        {'quality': 'blue', 'level': 22, 'star': 0, 'item_tier': 't1_power', 'item_qlt': 'orange', 'item_num': 0.0,
         'item_boost': 0, 'pet_qlt': 'blue', 'pet_lvl': 14, 'pet_star': 1}], [
        {'quality': 'orange', 'level': 22, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 10, 'pet_star': 4},
        {'quality': 'purple', 'level': 22, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'orange', 'item_num': 0.0,
         'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 15, 'pet_star': 4},
        {'quality': 'blue', 'level': 22, 'star': 0, 'item_tier': 't1_power', 'item_qlt': 'orange', 'item_num': 0.0,
         'item_boost': 0, 'pet_qlt': 'blue', 'pet_lvl': 15, 'pet_star': 1}], [
        {'quality': 'orange', 'level': 22, 'star': 0, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 11, 'pet_star': 5},
        {'quality': 'purple', 'level': 22, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 3.0,
         'item_boost': 0, 'pet_qlt': 'purple', 'pet_lvl': 16, 'pet_star': 4},
        {'quality': 'purple', 'level': 22, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 2.0,
         'item_boost': 0, 'pet_qlt': 'blue', 'pet_lvl': 16, 'pet_star': 2}], [
        {'quality': 'orange', 'level': 24, 'star': 0, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 12, 'pet_star': 5},
        {'quality': 'purple', 'level': 24, 'star': 2, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 18, 'pet_star': 5},
        {'quality': 'purple', 'level': 24, 'star': 1, 'item_tier': 't1_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 0, 'pet_qlt': 'purple', 'pet_lvl': 18, 'pet_star': 2}], [
        {'quality': 'orange', 'level': 26, 'star': 0, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 13, 'pet_star': 6},
        {'quality': 'purple', 'level': 26, 'star': 2, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 20, 'pet_star': 5},
        {'quality': 'purple', 'level': 26, 'star': 1, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 20, 'pet_star': 2}], [
        {'quality': 'orange', 'level': 28, 'star': 0, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 22, 'pet_star': 6},
        {'quality': 'purple', 'level': 28, 'star': 2, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 22, 'pet_star': 6},
        {'quality': 'purple', 'level': 28, 'star': 2, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 22, 'pet_star': 2}], [
        {'quality': 'orange', 'level': 30, 'star': 1, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 26, 'pet_star': 7},
        {'quality': 'purple', 'level': 30, 'star': 3, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 26, 'pet_star': 6},
        {'quality': 'purple', 'level': 30, 'star': 2, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'purple', 'pet_lvl': 26, 'pet_star': 3}], [
        {'quality': 'orange', 'level': 30, 'star': 1, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 30, 'pet_star': 7},
        {'quality': 'purple', 'level': 30, 'star': 3, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 30, 'pet_star': 7},
        {'quality': 'purple', 'level': 30, 'star': 2, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 30, 'pet_star': 3}], [
        {'quality': 'orange', 'level': 33, 'star': 1, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 34, 'pet_star': 8},
        {'quality': 'purple', 'level': 33, 'star': 3, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 34, 'pet_star': 7},
        {'quality': 'purple', 'level': 33, 'star': 3, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 34, 'pet_star': 4}], [
        {'quality': 'orange', 'level': 35, 'star': 1, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8},
        {'quality': 'purple', 'level': 35, 'star': 3, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8},
        {'quality': 'purple', 'level': 35, 'star': 3, 'item_tier': 't2_power', 'item_qlt': 'blue', 'item_num': 5.0,
         'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 4}]]


## 获取所有品质的英雄的标准模板属性
def fetch_hero_level_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    blue_hero_atk = [int(val) for val in wb.sheets['英雄升级数值'].range('I3:I62').value]
    purple_hero_atk = [int(val) for val in wb.sheets['英雄升级数值'].range('M3:M62').value]
    orange_hero_atk = [int(val) for val in wb.sheets['英雄升级数值'].range('Q3:Q62').value]

    blue_hero_def = [int(val) for val in wb.sheets['英雄升级数值'].range('J3:J62').value]
    purple_hero_def = [int(val) for val in wb.sheets['英雄升级数值'].range('N3:N62').value]
    orange_hero_def = [int(val) for val in wb.sheets['英雄升级数值'].range('R3:R62').value]

    blue_hero_hp = [int(val) for val in wb.sheets['英雄升级数值'].range('K3:K62').value]
    purple_hero_hp = [int(val) for val in wb.sheets['英雄升级数值'].range('O3:O62').value]
    orange_hero_hp = [int(val) for val in wb.sheets['英雄升级数值'].range('S3:S62').value]

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
    for row in wb.sheets['英雄升级数值'].range('A65:F80').value:
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


## 获取所有英雄的属性与战力的权重
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


## 获取所有英雄的装备数值
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


## 获取所有英雄的装备强化数值
def fetch_item_boost_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    # print(wb.sheets['装备强化数值'].range('B3:B22').value)
    return wb.sheets['装备强化数值'].range('C3:C22').value


## 获取所有英雄的宠物升级数值
def fetch_pet_level_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    blue_pet_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('C3:C62').value]
    purple_pet_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('M3:M62').value]
    orange_pet_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Q3:Q62').value]

    blue_pet_crit = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('D3:D62').value]
    purple_pet_crit = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('N3:N62').value]
    orange_pet_crit = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('X3:X62').value]

    blue_pet_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('E3:E62').value]
    purple_pet_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('O3:O62').value]
    orange_pet_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Y3:Y62').value]

    blue_pet_crit_res = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('F3:F62').value]
    purple_pet_crit_res = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('P3:P62').value]
    orange_pet_crit_res = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Z3:Z62').value]

    blue_pet_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('G3:G62').value]
    purple_pet_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('Q3:Q62').value]
    orange_pet_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AA3:AA62').value]

    blue_pet_slg_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('H3:H62').value]
    purple_pet_slg_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('R3:R62').value]
    orange_pet_slg_atk = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AB3:AB62').value]

    blue_pet_slg_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('I3:I62').value]
    purple_pet_slg_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('S3:S62').value]
    orange_pet_slg_def = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AC3:AC62').value]

    blue_pet_slg_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('J3:J62').value]
    purple_pet_slg_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('T3:T62').value]
    orange_pet_slg_hp = [int(val) for val in wb.sheets['宠物升级数值-标准单只'].range('AD3:AD62').value]

    return {'blue': {'atk': blue_pet_atk, 'crit': blue_pet_crit, 'def': blue_pet_def, 'crit_res': blue_pet_crit_res,
                     'hp': blue_pet_hp, 'slg_atk': blue_pet_slg_atk, 'slg_def': blue_pet_slg_def,
                     'slg_hp': blue_pet_slg_hp},
            'purple': {'atk': purple_pet_atk, 'crit': purple_pet_crit, 'def': purple_pet_def,
                       'crit_res': purple_pet_crit_res, 'hp': purple_pet_hp, 'slg_atk': purple_pet_slg_atk,
                       'slg_def': purple_pet_slg_def, 'slg_hp': purple_pet_slg_hp},
            'orange': {'atk': orange_pet_atk, 'crit': orange_pet_crit, 'def': orange_pet_def,
                       'crit_res': orange_pet_crit_res, 'hp': orange_pet_hp, 'slg_atk': orange_pet_slg_atk,
                       'slg_def': orange_pet_slg_def, 'slg_hp': orange_pet_slg_hp}}


## 获取所有英雄的宠物升阶数值
def fetch_pet_rank_attr(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    return wb.sheets['宠物升阶数值'].range('B2:B31').value


def calc_hero_power(hero):
    return int(hero.attack * 5 + hero.defense * 5 + hero.max_hp * 0.6 + hero.crit * 0 + hero.crit_res * 0 + \
               hero.eff_hit * 0 + hero.eff_res * 0 + hero.crit_damage * 0 * hero.crit + hero.crit_reduction * 0)


def get_hero_progression(filepath):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open(filepath)

    active_hero_prog = []
    for row in wb.sheets['Sheet18'].range('B3:AH12').value:
        heroes = []
        for i in range(3):
            heroes.append({'hero': row[i * 11 + 0], 'quality': int(row[i * 11 + 1]), 'level': int(row[i * 11 + 2]),
                           'star': int(row[i * 11 + 3]), 'item_tier': int(row[i * 11 + 4]),
                           'item_qlt': int(row[i * 11 + 5]), 'item_num': int(row[i * 11 + 6]),
                           'item_boost': int(row[i * 11 + 7]), 'pet_qlt': int(row[i * 11 + 8]),
                           'pet_lvl': int(row[i * 11 + 9]), 'pet_star': int(row[i * 11 + 10])})

        for hero in heroes:
            if hero['quality'] == 1:
                hero['quality'] = 'blue'
            elif hero['quality'] == 2:
                hero['quality'] = 'purple'
            else:
                hero['quality'] = 'orange'

            hero['item_tier'] = 't' + str(max(min(hero['item_tier'], 2), 1)) + '_power'

            if hero['item_qlt'] == 1:
                hero['item_qlt'] = 'blue'
            elif hero['item_qlt'] == 2:
                hero['item_qlt'] = 'purple'
            else:
                hero['item_qlt'] = 'orange'

            if hero['pet_qlt'] == 1:
                hero['pet_qlt'] = 'blue'
            elif hero['pet_qlt'] == 2:
                hero['pet_qlt'] = 'purple'
            else:
                hero['pet_qlt'] = 'orange'

        active_hero_prog.append(heroes)

    return active_hero_prog


class Numerical:
    # 初次获取养成数值数据
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
        self.hero_level_attr = {
            'blue': {
                'atk': [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 56, 59, 62, 65,
                        68,
                        71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131,
                        134,
                        137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173],
                'def': [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 56, 59, 62, 65,
                        68,
                        71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131,
                        134,
                        137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173],
                'hp': [125, 141, 158, 175, 191, 208, 225, 241, 258, 275, 291, 308, 325, 341, 358, 375, 391, 408, 425,
                       441,
                       466, 491, 516, 541, 566, 591, 616, 641, 666, 691, 716, 741, 766, 791, 816, 841, 866, 891, 916,
                       941,
                       966, 991, 1016, 1041, 1066, 1091, 1116, 1141, 1166, 1191, 1216, 1241, 1266, 1291, 1316, 1341,
                       1366,
                       1391, 1416, 1441]},
            'purple': {
                'atk': [24, 26, 28, 30, 33, 35, 37, 40, 42, 44, 47, 49, 52, 54, 57, 60, 62, 65, 67, 70, 74, 78, 82, 86,
                        90,
                        94, 98, 102, 106, 110, 114, 118, 122, 126, 130, 134, 138, 142, 146, 150, 154, 158, 162, 166,
                        170,
                        174, 178, 182, 186, 190, 194, 198, 202, 206, 210, 214, 218, 222, 226, 230],
                'def': [24, 26, 28, 30, 33, 35, 37, 40, 42, 44, 47, 49, 52, 54, 57, 60, 62, 65, 67, 70, 74, 78, 82, 86,
                        90,
                        94, 98, 102, 106, 110, 114, 118, 122, 126, 130, 134, 138, 142, 146, 150, 154, 158, 162, 166,
                        170,
                        174, 178, 182, 186, 190, 194, 198, 202, 206, 210, 214, 218, 222, 226, 230],
                'hp': [200, 216, 234, 255, 275, 295, 314, 333, 353, 374, 393, 416, 438, 457, 480, 502, 520, 543, 565,
                       587,
                       620, 653, 687, 720, 753, 786, 820, 853, 886, 919, 953, 986, 1019, 1052, 1086, 1119, 1152, 1185,
                       1219,
                       1252, 1285, 1318, 1352, 1385, 1418, 1451, 1485, 1518, 1551, 1584, 1618, 1651, 1684, 1717, 1751,
                       1784,
                       1817, 1850, 1884, 1917]},
            'orange': {
                'atk': [27, 30, 33, 37, 40, 43, 47, 50, 53, 56, 59, 62, 65, 69, 71, 74, 77, 80, 83, 86, 90, 95, 99, 104,
                        108, 113, 118, 123, 128, 132, 137, 142, 147, 152, 156, 161, 166, 171, 176, 180, 185, 190, 195,
                        200,
                        204, 209, 214, 219, 224, 228, 233, 238, 243, 248, 252, 257, 262, 267, 272, 276],
                'def': [27, 30, 33, 37, 40, 43, 47, 50, 53, 56, 59, 62, 65, 69, 71, 74, 77, 80, 83, 86, 90, 95, 99, 104,
                        108, 113, 118, 123, 128, 132, 137, 142, 147, 152, 156, 161, 166, 171, 176, 180, 185, 190, 195,
                        200,
                        204, 209, 214, 219, 224, 228, 233, 238, 243, 248, 252, 257, 262, 267, 272, 276],
                'hp': [225, 253, 282, 310, 338, 365, 392, 419, 446, 472, 498, 524, 549, 575, 599, 624, 648, 672, 696,
                       719,
                       756, 792, 826, 866, 906, 946, 986, 1026, 1066, 1106, 1146, 1186, 1226, 1266, 1306, 1346, 1386,
                       1426,
                       1466, 1506, 1546, 1586, 1626, 1666, 1706, 1746, 1786, 1826, 1866, 1906, 1946, 1986, 2026, 2066,
                       2106,
                       2146, 2186, 2226, 2266, 2306]}}

        self.hero_offset = {'白板': {'name': '白板', 'quality': 1.0, 'atk': 0.4, 'def': 0.5, 'hp': 1.2},
                            '杰玛': {'name': '杰玛', 'quality': 1.0, 'atk': 1.1, 'def': 1.0, 'hp': 0.9},
                            '按摩师': {'name': '按摩师', 'quality': 1.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '东': {'name': '东', 'quality': 1.0, 'atk': 0.75, 'def': 1.1, 'hp': 1.15},
                            '奈乔': {'name': '奈乔', 'quality': 2.0, 'atk': 1.1, 'def': 0.95, 'hp': 0.95},
                            '苏茜': {'name': '苏茜', 'quality': 2.0, 'atk': 0.85, 'def': 1.05, 'hp': 1.1},
                            '金鼻子': {'name': '金鼻子', 'quality': 2.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '街头艺术家': {'name': '街头艺术家', 'quality': 2.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '女医生': {'name': '女医生', 'quality': 2.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '审判长': {'name': '审判长', 'quality': 2.0, 'atk': 1.05, 'def': 0.95, 'hp': 1.0},
                            '南希': {'name': '南希', 'quality': 3.0, 'atk': 1.1, 'def': 0.9, 'hp': 1.0},
                            '华特': {'name': '华特', 'quality': 3.0, 'atk': 0.75, 'def': 1.1, 'hp': 1.15},
                            '杰登': {'name': '杰登', 'quality': 3.0, 'atk': 1.2, 'def': 0.9, 'hp': 0.9},
                            '大鹅': {'name': '大鹅', 'quality': 3.0, 'atk': 1.0, 'def': 1.0, 'hp': 1.0},
                            '吉尔伯特': {'name': '吉尔伯特', 'quality': 3.0, 'atk': 1.1, 'def': 0.95, 'hp': 0.95},
                            'E-girl': {'name': 'E-girl', 'quality': 3.0, 'atk': 1.15, 'def': 0.9, 'hp': 0.95},
                            '硬汉': {'name': '硬汉', 'quality': 3.0, 'atk': 0.85, 'def': 1.05, 'hp': 1.1}}

        self.hero_star = {
            'blue': {'crit': [0, 15, 30, 45, 60, 75, 90], 'crit_res': [0, 15, 30, 45, 60, 75, 90],
                     'eff_hit': [0, 0.09, 0.18, 0.27, 0.36, 0.45, 0.54],
                     'eff_res': [0, 0.06749999999999999, 0.13499999999999998, 0.20249999999999999, 0.26999999999999996,
                                 0.33749999999999997, 0.40499999999999997],
                     'base_attr': [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]},
            'purple': {'crit': [0, 18, 37, 56, 75, 93, 112], 'crit_res': [0, 18, 37, 56, 75, 93, 112],
                       'eff_hit': [0, 0.11249999999999999, 0.22499999999999998, 0.3375, 0.44999999999999996, 0.5625,
                                   0.675],
                       'eff_res': [0, 0.08437499999999999, 0.16874999999999998, 0.253125, 0.33749999999999997,
                                   0.42187499999999994, 0.50625], 'base_attr': [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]},
            'orange': {'crit': [0, 24, 48, 72, 96, 120, 144], 'crit_res': [0, 24, 48, 72, 96, 120, 144],
                       'eff_hit': [0, 0.144, 0.288, 0.43200000000000005, 0.576, 0.7200000000000001, 0.8640000000000001],
                       'eff_res': [0, 0.10799999999999998, 0.21599999999999997, 0.324, 0.43199999999999994,
                                   0.5399999999999999, 0.648], 'base_attr': [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]}
        }

        self.attr_weight = {'atk': 5.0, 'def': 5.0, 'hp': 0.6, 'crit': 5.0, 'crit_res': 5.0, 'eff_hit': 500.0,
                            'eff_res': 500.0, 'crit_dmg': 1000.0, 'crit_dmg_res': 1000.0}

        self.item_qlt_power = {'blue': {'t1_power': 180.0, 't2_power': 300.0},
                               'purple': {'t1_power': 270.0, 't2_power': 450.0},
                               'orange': {'t1_power': 360.0, 't2_power': 600.0}}

        self.item_attr_prop = {'atk_prop': 0.2, 'def_prop': 0.2, 'hp_prop': 0.2, 'crit_prop': 0.1111111111111111,
                               'crit_res_prop': 0.08888888888888889, 'eff_hit_prop': 0.1111111111111111,
                               'eff_res_prop': 0.08888888888888889}

        self.item_boost_attr = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0,
                                150.0, 160.0, 170.0, 180.0, 190.0, 200.0]

        self.pet_level_attr = {
            'blue': {
                'atk': [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 56, 59, 62, 65,
                        68,
                        71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131,
                        134,
                        137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173],
                'crit': [5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 21, 22, 23,
                         24,
                         25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33,
                         34,
                         34, 35, 36, 36, 37, 38, 39, 39, 40],
                'def': [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 56, 59, 62, 65,
                        68,
                        71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131,
                        134,
                        137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173],
                'crit_res': [5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 21, 22,
                             23,
                             24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 27, 27, 28, 29, 29, 30, 31, 32,
                             32,
                             33, 34, 34, 35, 36, 36, 37, 38, 39, 39, 40],
                'hp': [125, 141, 158, 175, 191, 208, 225, 241, 258, 275, 291, 308, 325, 341, 358, 375, 391, 408, 425,
                       441,
                       466, 491, 516, 541, 566, 591, 616, 641, 666, 691, 716, 741, 766, 791, 816, 841, 866, 891, 916,
                       941,
                       966, 991, 1016, 1041, 1066, 1091, 1116, 1141, 1166, 1191, 1216, 1241, 1266, 1291, 1316, 1341,
                       1366,
                       1391, 1416, 1441],
                'slg_atk': [4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 20,
                            21,
                            22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                            42,
                            43, 44, 45, 46, 47, 48, 49, 50, 51, 51],
                'slg_def': [4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 20,
                            21,
                            22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                            42,
                            43, 44, 45, 46, 47, 48, 49, 50, 51, 51],
                'slg_hp': [45, 51, 57, 63, 68, 75, 81, 87, 92, 99, 105, 111, 117, 122, 129, 135, 141, 147, 152, 158,
                           168,
                           177, 185, 195, 204, 213, 222, 230, 240, 249, 258, 267, 275, 285, 294, 302, 312, 321, 330,
                           339,
                           348, 356, 366, 375, 384, 393, 401, 411, 420, 429, 438, 446, 456, 465, 474, 483, 491, 501,
                           510,
                           519]},
            'purple': {
                'atk': [19, 22, 24, 27, 29, 32, 35, 37, 40, 42, 45, 48, 50, 53, 55, 58, 61, 63, 66, 68, 72, 76, 80, 84,
                        88,
                        92, 96, 100, 104, 107, 111, 115, 119, 123, 127, 131, 135, 139, 143, 146, 150, 154, 158, 162,
                        166,
                        170, 174, 178, 182, 185, 189, 193, 197, 201, 205, 209, 213, 217, 221, 224],
                'crit': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30,
                         32,
                         33, 35, 36, 37, 39, 40, 41, 43, 44, 45, 47, 48, 50, 51, 35, 35, 36, 37, 37, 39, 40, 41, 41, 42,
                         44,
                         44, 45, 46, 46, 48, 49, 50, 50, 52],
                'def': [19, 22, 24, 27, 29, 32, 35, 37, 40, 42, 45, 48, 50, 53, 55, 58, 61, 63, 66, 68, 72, 76, 80, 84,
                        88,
                        92, 96, 100, 104, 107, 111, 115, 119, 123, 127, 131, 135, 139, 143, 146, 150, 154, 158, 162,
                        166,
                        170, 174, 178, 182, 185, 189, 193, 197, 201, 205, 209, 213, 217, 221, 224],
                'crit_res': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29,
                             30,
                             32, 33, 35, 36, 37, 39, 40, 41, 43, 44, 45, 47, 48, 50, 51, 35, 35, 36, 37, 37, 39, 40, 41,
                             41,
                             42, 44, 44, 45, 46, 46, 48, 49, 50, 50, 52],
                'hp': [162, 184, 205, 227, 249, 270, 292, 314, 335, 357, 379, 400, 422, 444, 465, 487, 509, 530, 552,
                       574,
                       606, 639, 671, 704, 736, 769, 801, 834, 866, 899, 931, 964, 996, 1029, 1061, 1094, 1126, 1159,
                       1191,
                       1224, 1256, 1289, 1321, 1354, 1386, 1419, 1451, 1484, 1516, 1549, 1581, 1614, 1646, 1679, 1711,
                       1744,
                       1776, 1809, 1841, 1874],
                'slg_atk': [5, 6, 7, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20, 21, 23, 24, 25,
                            26,
                            27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 53,
                            54,
                            55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67],
                'slg_def': [5, 6, 7, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20, 21, 23, 24, 25,
                            26,
                            27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 53,
                            54,
                            55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67],
                'slg_hp': [58, 66, 74, 81, 89, 97, 105, 113, 120, 128, 136, 144, 152, 159, 167, 175, 183, 191, 198, 206,
                           218, 230, 241, 253, 265, 276, 288, 300, 312, 323, 335, 347, 358, 370, 382, 393, 405, 417,
                           429,
                           440, 452, 464, 475, 487, 499, 510, 522, 534, 546, 557, 569, 581, 592, 604, 616, 627, 639,
                           651,
                           663, 674]},
            'orange': {
                'atk': [162, 184, 205, 227, 249, 270, 292, 314, 335, 357, 379, 400, 422, 444, 465, 487, 509, 530, 552,
                        574,
                        606, 639, 671, 704, 736, 769, 801, 834, 866, 899, 931, 964, 996, 1029, 1061, 1094, 1126, 1159,
                        1191,
                        1224, 1256, 1289, 1321, 1354, 1386, 1419, 1451, 1484, 1516, 1549, 1581, 1614, 1646, 1679, 1711,
                        1744, 1776, 1809, 1841, 1874],
                'crit': [9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 25, 26, 27, 28, 30, 31, 32, 34, 36, 37, 39,
                         41,
                         43, 45, 47, 49, 50, 52, 54, 56, 58, 60, 61, 63, 65, 67, 69, 47, 47, 49, 50, 50, 52, 54, 56, 56,
                         57,
                         59, 59, 61, 63, 63, 64, 66, 68, 68, 70],
                'def': [26, 29, 33, 36, 40, 43, 47, 50, 54, 57, 61, 64, 68, 71, 75, 78, 82, 85, 89, 92, 98, 103, 108,
                        113,
                        119, 124, 129, 134, 140, 145, 150, 155, 161, 166, 171, 176, 182, 187, 192, 197, 203, 208, 213,
                        218,
                        224, 229, 234, 239, 245, 250, 255, 260, 266, 271, 276, 281, 287, 292, 297, 302],
                'crit_res': [9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 25, 26, 27, 28, 30, 31, 32, 34, 36, 37,
                             39,
                             41, 43, 45, 47, 49, 50, 52, 54, 56, 58, 60, 61, 63, 65, 67, 69, 47, 47, 49, 50, 50, 52, 54,
                             56,
                             56, 57, 59, 59, 61, 63, 63, 64, 66, 68, 68, 70],
                'hp': [218, 247, 277, 306, 335, 364, 393, 422, 452, 481, 510, 539, 568, 597, 627, 656, 685, 714, 743,
                       772,
                       816, 860, 904, 947, 991, 1035, 1079, 1122, 1166, 1210, 1254, 1297, 1341, 1385, 1429, 1472, 1516,
                       1560, 1604, 1647, 1691, 1735, 1779, 1822, 1866, 1910, 1954, 1997, 2041, 2085, 2129, 2172, 2216,
                       2260,
                       2304, 2347, 2391, 2435, 2479, 2522],
                'slg_atk': [7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 32, 34,
                            35,
                            37, 38, 40, 42, 43, 45, 46, 48, 49, 51, 53, 54, 56, 57, 59, 60, 62, 64, 65, 67, 68, 70, 71,
                            73,
                            75, 76, 78, 79, 81, 82, 84, 86, 87, 89, 90],
                'slg_def': [7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 32, 34,
                            35,
                            37, 38, 40, 42, 43, 45, 46, 48, 49, 51, 53, 54, 56, 57, 59, 60, 62, 64, 65, 67, 68, 70, 71,
                            73,
                            75, 76, 78, 79, 81, 82, 84, 86, 87, 89, 90],
                'slg_hp': [78, 89, 99, 110, 120, 131, 141, 152, 162, 173, 183, 194, 204, 215, 225, 236, 246, 257, 267,
                           278,
                           294, 309, 325, 341, 357, 372, 388, 404, 420, 435, 451, 467, 482, 498, 514, 530, 546, 561,
                           577,
                           593, 609, 624, 640, 656, 672, 687, 703, 719, 735, 750, 766, 782, 798, 813, 829, 845, 860,
                           876,
                           892, 908]}}

        self.pet_rank_attr = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8,
                              0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5]

    # 计算英雄属性
    def calc_hero_attr(self, hero, level, star, quality, item_qlt, item_tier, item_num, item_boost, pet_qlt, pet_lvl,
                       pet_star):
        # print("hero: ", self.hero_offset[hero]['atk'] * self.hero_level_attr[quality]['atk'][level - 1] * \
        #       (1 + self.hero_star[quality]['base_attr'][star]))

        # print(self.hero_offset[hero]['atk'], self.hero_level_attr[quality]['atk'][level - 1],
        #         self.hero_star[quality]['base_attr'][star])

        # print("pet: ", self.pet_level_attr[pet_qlt]['slg_atk'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)]))

        # print(self.pet_level_attr[pet_qlt]['slg_atk'][pet_lvl - 1], self.pet_rank_attr[max(pet_star - 1, 0)])

        atk = self.hero_offset[hero]['atk'] * self.hero_level_attr[quality]['atk'][level - 1] * \
              (1 + self.hero_star[quality]['base_attr'][star]) + self.item_qlt_power[item_qlt][item_tier] * \
              item_num * self.item_attr_prop['atk_prop'] / self.attr_weight['atk'] + \
              self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['atk'] + \
              self.pet_level_attr[pet_qlt]['slg_atk'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])

        _def = self.hero_offset[hero]['def'] * self.hero_level_attr[quality]['def'][level - 1] * \
               (1 + self.hero_star[quality]['base_attr'][star]) + self.item_qlt_power[item_qlt][item_tier] * \
               item_num * self.item_attr_prop['def_prop'] / self.attr_weight['def'] + \
               self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['def'] + \
               self.pet_level_attr[pet_qlt]['slg_def'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])

        # print(self.hero_offset[hero]['hp'], self.hero_level_attr[quality]['hp'][level - 1],
        #       self.hero_star[quality]['base_attr'][star - 1], self.item_qlt_power[item_qlt][item_tier],
        #       item_num, self.item_attr_prop['hp_prop'], self.attr_weight['hp'], self.item_boost_attr[item_boost - 1],
        #       self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1], self.pet_rank_attr[pet_star - 1])

        hp = self.hero_offset[hero]['hp'] * self.hero_level_attr[quality]['hp'][level - 1] * \
             (1 + self.hero_star[quality]['base_attr'][star]) + self.item_qlt_power[item_qlt][item_tier] * \
             item_num * self.item_attr_prop['hp_prop'] / self.attr_weight['hp'] + \
             self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['hp'] + \
             self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])

        crit = self.hero_star[quality]['crit'][star] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
               self.item_attr_prop['crit_prop'] / self.attr_weight['crit']

        crit_res = self.hero_star[quality]['crit_res'][star] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
                   self.item_attr_prop['crit_res_prop'] / self.attr_weight['crit_res']

        eff_hit = self.hero_star[quality]['eff_hit'][star] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
                  self.item_attr_prop['eff_hit_prop'] / self.attr_weight['eff_hit']

        eff_res = self.hero_star[quality]['eff_res'][star] + self.item_qlt_power[item_qlt][item_tier] * item_num * \
                  self.item_attr_prop['eff_res_prop'] / self.attr_weight['eff_res']

        return [atk, _def, hp, crit, crit_res, eff_hit, eff_res, hero, level]

    def pack(self, hero_info):
        attrs = self.calc_hero_attr(**hero_info)
        dict = {}
        dict['atk_base'], dict['def_base'], dict['max_hp_base'], dict['crit_base'], dict['crit_res_base'], \
            dict['eff_hit_base'], dict['eff_res_base'] = \
            attrs[0], attrs[1], attrs[2], attrs[3], attrs[4], attrs[5], attrs[6]
        dict['name'], dict['level'] = attrs[7], attrs[8]
        return dict

    def pack_monster(self, attrs):
        dict = {}
        dict['atk_base'], dict['def_base'], dict['max_hp_base'] = attrs[0], attrs[1], attrs[2]
        dict['crit_base'], dict['crit_res_base'], dict['eff_hit_base'], dict['eff_res_base'] = \
            0, 0, 0, 0
        dict['name'], dict['level'] = 'Monster', 0
        return dict


if __name__ == '__main__':
    # hero_getter = Numerical('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')
    hero_getter = Numerical()
    # print(hero_getter.calc_hero_attr(**hero_info))
    heroes_infos = get_hero_progression('E:\新建文件夹\战斗\SSR战斗养成数值7day_new.xlsx')
    print(heroes_infos[0])
    print(hero_getter.calc_hero_attr(**heroes_infos[0][0]))
