import xlwings as xw


# 获取所有品质的英雄的标准模板属性
def fetch_hero_attr():
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

    return blue_hero_atk, purple_hero_atk, orange_hero_atk, blue_hero_def, purple_hero_def, orange_hero_def, \
        blue_hero_hp, purple_hero_hp, orange_hero_hp


# 获取所有英雄的属性偏移量
def fetch_hero_offset():
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('E:\新建文件夹\战斗\SSR战斗养成数值7day.xlsx')

    hero_offset = {}
    for row in wb.sheets['英雄升级数值'].range('A46:F60').value:
        hero_offset[row[0]] = {'name': row[0], 'quality': row[1], 'atk': row[2], 'def': row[3], 'hp': row[4]}
    return hero_offset


if __name__ == '__main__':
    print(fetch_hero_offset())
