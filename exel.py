import xlsxwriter
import parser_ as p
from datetime import datetime

data, bad_ids = p.get_data()

workbook = xlsxwriter.Workbook('table.xlsx')
worksheet = workbook.add_worksheet()

# print(p.get_info_from_id('23608'))

widths = [15, 52, 52, 74, 20, 20, 21, 60, 23, 23, 27, 23, 23, 22, 23, 33, 17, 17, 75, 75, 22, 15]
for index, width in enumerate(widths):
    worksheet.set_column(index, index, width)


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
format1 = workbook.add_format({'bg_color': '#e4ffad'})
format2 = workbook.add_format({'num_format': 'dd/mm/yyyy'})
worksheet.set_row(0, cell_format=format1)
for index, name in enumerate(p.good_keys):
    if name == '':
        pass
    else:
        # print(f'{letters[index]}1')
        worksheet.write(f'{letters[index]}1', name)

print('Заполняем таблицу...')
for hotel_index, hotel in enumerate(data):
    for param_index, param in enumerate(hotel):
        if param == 'Дата' or param == 'Дата выдачи' or param == 'Срок действия до':
            worksheet.write_datetime(f'{letters[p.good_keys.index(param)]}{hotel_index + 2}', hotel[param], format2)
        else:
            worksheet.write(f'{letters[p.good_keys.index(param)]}{hotel_index + 2}', hotel[param])

print('Готово')

workbook.close()
