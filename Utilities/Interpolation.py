import numpy as np
import csv
from decimal import Decimal
import scipy


def linear_interpolation(atk, _def, hp):
    lvl = [1, 5, 9, 12, 15, 17, 19, 20]
    # lvl = [1, 2]
    # atk = [1, 3]
    # _def = [1, 5]
    # hp = [1, 20]
    f_atk, f_def, f_hp = np.polyfit(lvl, atk, 1), np.polyfit(lvl, _def, 1), np.polyfit(lvl, hp, 1)
    p_atk, p_def, p_hp = np.poly1d(f_atk), np.poly1d(f_def), np.poly1d(f_hp)

    input = [i + 1 for i in range(0, 30)]
    output_atk, output_def, output_hp = p_atk(input), p_def(input), p_hp(input)

    rows = [['Level', 'Attack', 'Defense', 'HP']]
    for i in range(0, 30):
        idx = lvl.index(i + 1) if i + 1 in lvl else len(lvl)
        if idx < len(lvl):
            rows.append([i + 1, atk[idx],
                         Decimal((_def[idx] / 10)).quantize(Decimal("1"), rounding = "ROUND_HALF_UP") * 10,
                         Decimal((hp[idx] / 10)).quantize(Decimal("1"), rounding = "ROUND_HALF_UP") * 10])
        else:
            rows.append([i + 1, output_atk[i],
                         Decimal((output_def[i] / 10)).quantize(Decimal("1"), rounding = "ROUND_HALF_UP") * 10,
                         Decimal((output_hp[i] / 10)).quantize(Decimal("1"), rounding = "ROUND_HALF_UP") * 10])

    with open('C:\\Users\Administrator\Desktop\SLG Monster Attr.csv', 'w', newline='',
              encoding='utf-8') as loss:
        writer = csv.writer(loss)
        writer.writerows(rows)


# if __name__ == '__main__':
#     linear_interpolation([1], [1], [1])
