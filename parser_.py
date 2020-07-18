import requests as r
from urllib.parse import urlencode
import re

base_url = r'https://xn----7sba3acabbldhv3chawrl5bzn.xn--p1ai/displayAccommodation/index?'
base_url_s = r'https://xn----7sba3acabbldhv3chawrl5bzn.xn--p1ai/displayAccommodation/'
ptrn1 = r'href=\"/displayAccommodation/([0-9]{1,5})\"'
ptrn2 = r'([\n\r\t«»]|<.*?>|&#[0-9]{1,};|&[a-z]{1,};|\ufeff)'
ptrn3 = r'[\s]{2,}'
data1 = []


def get_rooms_sum(arr):
    rooms_sum = 0
    a = 0
    for i in arr:
        if i.isdigit() and a == 0:
            a += 1
            rooms_sum += int(i)
        else:
            a = max(a - 1, 0)
    return str(rooms_sum)


def get_region_list():
    res = r.get(base_url).content.decode('utf-8')
    res = res.split('<datalist id="regions">')[1].split('</datalist>')[0]
    regions = [i.split('</option>')[0] for i in res.split('<option>')[1:]]
    return regions


def get_data(region):
    request_params = {'Accommodation[Region]': region, 'Accommodation[Key]': ''}
    request_params = urlencode(request_params)
    c = 0
    data0 = []
    old_ids = []
    bad_ids = []
    while True:
        c += 1
        url = base_url + request_params + '&Accommodation_page=' + str(c)
        res = r.get(url).content.decode('utf-8')
        ids = re.findall(ptrn1, res)[::2]
        if ids == old_ids:
            break
        for i in ids:
            try:
                ofs = 0
                print(i)
                url0 = base_url_s + i
                res0 = r.get(url0).content.decode('utf-8')
                res0 = res0.split(r'<div class="detail-fields">')[1].split(r'<!--content-->')[0] \
                    .split(r'<div class="detail-field">')
                res0 = [re.sub(ptrn3, ' ', re.sub(ptrn2, ' ', j)).strip() for j in res0]
                data = [res0[1].split('Вид: ')[1], res0[2].split('объекта: ')[1], res0[3].split('объекта: ')[1],
                        res0[4].split('предпринимателя: ')[1], res0[5].split('Регион: ')[1],
                        res0[6].split('ИНН: ')[1], res0[7].split('ОГРНИП: ')[1], res0[8].split('нахождения: ')[1],
                        res0[9][9:], res0[10][5:], res0[11][8:],
                        res0[12].split('сайта: ')[1].split(' ')[0],
                        res0[13].split('категория: ')[1].split(' Решение')[0],
                        res0[14].split('номер: ')[1], res0[15].split('Дата: ')[1].split(' Свидетельство')[0],
                        res0[16].split('свидетельства: ')[1],
                        res0[17].split('выдачи: ')[1],
                        res0[18].split('до: ')[1].split(' Аккредитованная')[0]]
                try:
                    data.append(res0[19].split('Наименование: ')[1])
                except:
                    data.append(res0[20].split('Наименование: ')[1])
                    ofs = 1

                data.append(get_rooms_sum(res0[20+ofs].split('Количество мест ')[-1].split(' ')))
                if data[4] == 'Информация':
                    data[4] = ''
                print(data)

                data = {'Вид': data[0], 'Полное наименование классифицированного объекта': data[1],
                        'Cокращенное наименование классифицированного объекта': data[2],
                        'Наименование юридического лица/индивидуального предпринимателя': data[3],
                        'Регион': data[4], 'ИНН': data[5], 'ОГРН/ОГРНИП': data[6], 'Адрес места нахождения': data[7],
                        'Телефон': data[8], 'Факс': data[9], 'E-mail': data[10], 'Адрес сайта': data[11],
                        'Присвоенная категория': data[12], 'Регистрационный номер': data[13],
                        'Регистрационный номер свидетельства': data[14], 'Дата выдачи': data[15],
                        'Срок действия до': data[16], 'Наименование': data[17], 'Контактные данные': data[18],
                        'Количество номеров': data[19]}
                data0.append(data)

            except:
                print('bad id(')
                bad_ids.append(i)

        old_ids = ids
    print(bad_ids)
    return data0, bad_ids





# with open('all.json', 'w', encoding='utf-8') as f:
#     json.dump(data1, f, ensure_ascii=False, indent=4)
