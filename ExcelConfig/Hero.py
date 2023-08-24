import xlwings as xw


## 获取所有品质的英雄的标准模板属性
def fetch_hero_level_attr():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

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
def fetch_hero_offset():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

    hero_offset = {}
    for row in wb.sheets['英雄升级数值'].range('A46:F60').value:
        hero_offset[row[0]] = {'name': row[0], 'quality': row[1], 'atk': row[2], 'def': row[3], 'hp': row[4]}
    return hero_offset


## 获取所有英雄的升星数值
def fetch_hero_star_attr():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

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


def fetch_attr_weight():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

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


def fetch_hero_item_attr():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

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


def fetch_item_boost_attr():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

    # print(wb.sheets['装备强化数值'].range('B3:B22').value)
    return wb.sheets['装备强化数值'].range('B3:B22').value


def fetch_pet_level_attr():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

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


def fetch_pet_rank_attr():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

    return wb.sheets['宠物升阶数值'].range('B2:B31').value


class Numerical:
    def __init__(self):
        self.hero_level_attr = fetch_hero_level_attr()
        print('英雄升级数值读取完毕')
        self.hero_offset = fetch_hero_offset()
        print('英雄属性偏移量读取完毕')
        self.hero_star = fetch_hero_star_attr()
        print('英雄升星数值读取完毕')
        self.attr_weight = fetch_attr_weight()
        print('属性权重读取完毕')
        self.item_qlt_power, self.item_attr_prop = fetch_hero_item_attr()
        print('英雄装备数值读取完毕')
        self.item_boost_attr = fetch_item_boost_attr()
        print('英雄装备强化数值读取完毕')
        self.pet_level_attr = fetch_pet_level_attr()
        print('宠物升级数值读取完毕')
        self.pet_rank_attr = fetch_pet_rank_attr()
        print('宠物升阶数值读取完毕')

    def calc_hero_attr(self, hero, level, star, quality, item_qlt, item_num, item_boost, pet_qlt, pet_lvl, pet_star):
        atk = self.hero_offset[hero]['atk'] * self.hero_level_attr[quality]['atk'][level - 1] * \
              (1 + self.hero_star[quality]['base_attr'][star - 1]) + self.item_qlt_power[item_qlt]['t1_power'] * \
              item_num * self.item_attr_prop['atk_prop'] / self.attr_weight['atk'] + \
              self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['atk'] + \
              self.pet_level_attr[pet_qlt]['slg_atk'][pet_lvl - 1] * (1 + self.pet_rank_attr[pet_star - 1])

        _def = self.hero_offset[hero]['def'] * self.hero_level_attr[quality]['def'][level - 1] * \
               (1 + self.hero_star[quality]['base_attr'][star - 1]) + self.item_qlt_power[item_qlt]['t1_power'] * \
               item_num * self.item_attr_prop['def_prop'] / self.attr_weight['def'] + \
               self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['def'] + \
               self.pet_level_attr[pet_qlt]['slg_def'][pet_lvl - 1] * (1 + self.pet_rank_attr[pet_star - 1])

        print(self.hero_offset[hero]['hp'], self.hero_level_attr[quality]['hp'][level - 1],
              self.hero_star[quality]['base_attr'][star - 1], self.item_qlt_power[item_qlt]['t1_power'],
              item_num, self.item_attr_prop['hp_prop'], self.attr_weight['hp'], self.item_boost_attr[item_boost - 1],
              self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1], self.pet_rank_attr[pet_star - 1])
        hp = self.hero_offset[hero]['hp'] * self.hero_level_attr[quality]['hp'][level - 1] * \
             (1 + self.hero_star[quality]['base_attr'][star - 1]) + self.item_qlt_power[item_qlt]['t1_power'] * \
             item_num * self.item_attr_prop['hp_prop'] / self.attr_weight['hp'] + \
             self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['hp'] + \
             self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1] * (1 + self.pet_rank_attr[pet_star - 1])

        crit = self.hero_star[quality]['crit'][star - 1] + self.item_qlt_power[item_qlt]['t1_power'] * item_num * \
                self.item_attr_prop['crit_prop'] / self.attr_weight['crit']

        crit_res = self.hero_star[quality]['crit_res'][star - 1] + self.item_qlt_power[item_qlt]['t1_power'] * item_num * \
                     self.item_attr_prop['crit_res_prop'] / self.attr_weight['crit_res']

        eff_hit = self.hero_star[quality]['eff_hit'][star - 1] + self.item_qlt_power[item_qlt]['t1_power'] * item_num * \
                        self.item_attr_prop['eff_hit_prop'] / self.attr_weight['eff_hit']

        eff_res = self.hero_star[quality]['eff_res'][star - 1] + self.item_qlt_power[item_qlt]['t1_power'] * item_num * \
                        self.item_attr_prop['eff_res_prop'] / self.attr_weight['eff_res']

        return atk, _def, hp, crit, crit_res, eff_hit, eff_res


if __name__ == '__main__':
    hero_info = {'hero': '奈乔', 'level': 30, 'star': 3, 'quality': 'purple', 'item_qlt': 'purple', 'item_num': 5,
                 'item_boost': 6, 'pet_qlt': 'purple', 'pet_lvl': 30, 'pet_star': 3}
    hero_getter = Numerical()
    print(hero_getter.calc_hero_attr(**hero_info))

