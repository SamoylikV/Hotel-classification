import xlsxwriter
import parser_ as p

workbook = xlsxwriter.Workbook('table.xlsx')
main = []
bad_ids = []
worksheet = workbook.add_worksheet()
c = 2

for region in p.get_region_list()[4:5]:
    rasd = p.get_data(region)
    main += rasd[0]
    bad_ids += rasd[1]

data_ = '123'
worksheet.set_column(0, 0, 17)
worksheet.set_column(1, 1, 9.5)
worksheet.set_column(2, 2, 52)
worksheet.set_column(3, 3, 74)
worksheet.set_column(4, 4, 15)
worksheet.set_column(5, 5, 22.34)
worksheet.set_column(6, 6, 21)
worksheet.set_column(7, 7, 21)
worksheet.set_column(8, 8, 23)
worksheet.set_column(9, 9, 23)
worksheet.set_column(10, 10, 23)
worksheet.set_column(11, 11, 23)
worksheet.set_column(12, 12, 23)
worksheet.set_column(13, 13, 22)
worksheet.set_column(14, 14, 23)
worksheet.set_column(15, 15, 112)
worksheet.set_column(16, 16, 53)
worksheet.set_column(17, 17, 11)
worksheet.set_column(18, 18, 14)

data_format1 = workbook.add_format({'bg_color': '#B0FAA2'})
format6 = workbook.add_format({'num_format': 'd mmm yyyy'})
worksheet.write('A1', 'Регион')
worksheet.write('B1', 'Вид')
worksheet.write('C1', 'Cокращенное наименование классифицированного объекта')
worksheet.write('D1', 'Полное наименование классифицированного объекта')
worksheet.write('E1', 'Кол-во номеров')
worksheet.write('F1', 'Присвоенная категория')
worksheet.write('G1', 'Дата', data_format1)
worksheet.write('H1', 'Дата выдачи', data_format1)
worksheet.write('I1', 'Срок действия до', data_format1)
worksheet.write('J1', 'Телефон')
worksheet.write('K1', 'Факс')
worksheet.write('L1', 'E-mail')
worksheet.write('M1', 'Адрес сайта')
worksheet.write('N1', 'Регистрационный номер свидетельства')
worksheet.write('O1', 'Регистрационный номер')
worksheet.write('P1', 'Наименование')
worksheet.write('Q1', 'Адрес места нахождения')
worksheet.write('R1', 'ИНН')
worksheet.write('S1', 'ОГРН/ОГРНИП')

for i in (main):
    vid = i["Вид"][0:i["Вид"].find(',')]
    worksheet.write('A' + str(c), i['Регион'])
    worksheet.write('B' + str(c), vid)
    worksheet.write('C' + str(c), i['Cокращенное наименование классифицированного объекта'])
    worksheet.write('D' + str(c), i['Полное наименование классифицированного объекта'])
    worksheet.write('E' + str(c), i['Количество номеров'])
    worksheet.write('F' + str(c), i['Присвоенная категория'])
    worksheet.write('G' + str(c), i['Регистрационный номер свидетельства'][0:-3], format6)
    worksheet.write('H' + str(c), i['Срок действия до'][0:-3], format6)
    worksheet.write('I' + str(c), i['Наименование'][0:-3], format6)
    worksheet.write('J' + str(c), i['Телефон'])
    worksheet.write('K' + str(c), i['Факс'])
    worksheet.write('L' + str(c), i['E-mail'])
    if i["Адрес сайта"] == 'Информация':
        worksheet.write('M' + str(c), ' ')
    else:
        worksheet.write('M' + str(c), i['Адрес сайта'])
    worksheet.write('N' + str(c), i['Дата выдачи'])
    worksheet.write('O' + str(c), i['Регистрационный номер'])
    worksheet.write('P' + str(c), i['Контактные данные'])
    worksheet.write('Q' + str(c), i['Адрес места нахождения'])
    worksheet.write('R' + str(c), i['ИНН'])
    worksheet.write('S' + str(c), i['ОГРН/ОГРНИП'])
    c += 1
worksheet.set_row(0, cell_format=data_format1)

print(bad_ids)
workbook.close()
