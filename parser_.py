import requests as r
from datetime import datetime
from urllib.parse import urlencode
import re

base_url = r'https://xn----7sba3acabbldhv3chawrl5bzn.xn--p1ai/displayAccommodation/index?'
base_url_s = r'https://xn----7sba3acabbldhv3chawrl5bzn.xn--p1ai/displayAccommodation/'
id_pattern = r'href=\"/displayAccommodation/([0-9]{1,5})\"'
trash_eraser1 = r'([\n\r\t«»]|<.*?>|&#[0-9]{1,};|&[a-z]{1,};|\ufeff)'
trash_eraser2 = r'[\s]{2,}'
info_pattern1 = r'<div class="detail-field">[\d\D]*?(?:<\/div>|<\/a>[\s]*<\/span>)'
costyl_pattern = r'<span class="detail-label">Контактные данные:<\/span>([\d\D]*?)<\/div>'
good_keys = ['Вид', 'Полное наименование классифицированного объекта',
             'Cокращенное наименование классифицированного объекта',
             'Наименование юридического лица/индивидуального предпринимателя', 'Регион', 'ИНН',
             'ОГРН/ОГРНИП', 'Адрес места нахождения', 'Телефон', 'Факс', 'E-mail', 'Адрес сайта',
             'Присвоенная категория', 'Регистрационный номер', 'Дата', 'Регистрационный номер свидетельства',
             'Дата выдачи', 'Срок действия до', 'Наименование', 'Контактные данные', 'Количество номеров', 'ID']

print('Собираем ID гостиниц...')


def count_rooms_from_res(res):
    n = 0
    c = 0
    a = res.split('<td>Количество мест</td>')[1].split(' <!--content-->')[0]
    a = re.sub(trash_eraser2, ' ', re.sub(trash_eraser1, '', a))
    for i in a.split(' '):
        if i.isdigit() and c == 0:
            c += 1
            n += int(i)
        else:
            c = max(c - 1, 0)
    return str(n)


def get_info_from_id(hotel_id):
    data = []
    res = r.get(base_url_s + hotel_id).content.decode('utf-8')
    data = re.findall(info_pattern1, res)
    data = [re.sub(trash_eraser2, ' ', re.sub(trash_eraser1, '', i)).strip() for i in data]
    data.append('Количество номеров: ' + count_rooms_from_res(res))
    #print(data)
    data = data[:12] + data[-9:]
    data0 = dict()
    for i in data:
        i = i.split(':')
        if type(i) != list:
            data0.update({i[0]: ''})
        else:
            data0.update({i[0]: i[1].strip()})
    data0.update({'ID': hotel_id})
    if list(data0.keys()) != good_keys:
        # print(hotel_id)
        #print(list(data0.keys()))
        return 0
    try:
        data0['Вид'] = data0['Вид'].split(',')[0]
    except:
        pass
    data_ = data0['Дата'].split(' ')
    data_.pop()
    if data_[1] == 'янв.':
        data_[1] = '01'
    elif data_[1] == 'февр.':
        data_[1] = '02'
    elif data_[1] == 'марта':
        data_[1] = '03'
    elif data_[1] == 'апр.':
        data_[1] = '04'
    elif data_[1] == 'мая':
        data_[1] = '05'
    elif data_[1] == 'июня':
        data_[1] = '06'
    elif data_[1] == 'июля':
        data_[1] = '07'
    elif data_[1] == 'авг.':
        data_[1] = '08'
    elif data_[1] == 'сент.':
        data_[1] = '09'
    elif data_[1] == 'окт.':
        data_[1] = '10'
    elif data_[1] == 'нояб.':
        data_[1] = '11'
    elif data_[1] == 'дек.':
        data_[1] = '12'
    data_[0] = int(data_[0])
    data_[1] = int(data_[1])
    data_[2] = int(data_[2])
    # print(datetime(data_[2], data_[1], data_[0]))
    data0['Дата'] = datetime(int(data_[2]), int(data_[1]), (data_[0]))
    # data0['Дата'] = ''.join(data_)

    data_ = data0['Дата выдачи'].split(' ')
    data_.pop()
    if data_[1] == 'янв.':
        data_[1] = '01'
    elif data_[1] == 'февр.':
        data_[1] = '02'
    elif data_[1] == 'марта':
        data_[1] = '03'
    elif data_[1] == 'апр.':
        data_[1] = '04'
    elif data_[1] == 'мая':
        data_[1] = '05'
    elif data_[1] == 'июня':
        data_[1] = '06'
    elif data_[1] == 'июля':
        data_[1] = '07'
    elif data_[1] == 'авг.':
        data_[1] = '08'
    elif data_[1] == 'сент.':
        data_[1] = '09'
    elif data_[1] == 'окт.':
        data_[1] = '10'
    elif data_[1] == 'нояб.':
        data_[1] = '11'
    elif data_[1] == 'дек.':
        data_[1] = '12'
    data_[0] = int(data_[0])
    data_[1] = int(data_[1])
    data_[2] = int(data_[2])
    data0['Дата выдачи'] = datetime(int(data_[2]), int(data_[1]), (data_[0]))

    data_ = data0['Срок действия до'].split(' ')
    data_.pop()
    if data_[1] == 'янв.':
        data_[1] = '01'
    elif data_[1] == 'февр.':
        data_[1] = '02'
    elif data_[1] == 'марта':
        data_[1] = '03'
    elif data_[1] == 'апр.':
        data_[1] = '04'
    elif data_[1] == 'мая':
        data_[1] = '05'
    elif data_[1] == 'июня':
        data_[1] = '06'
    elif data_[1] == 'июля':
        data_[1] = '07'
    elif data_[1] == 'авг.':
        data_[1] = '08'
    elif data_[1] == 'сент.':
        data_[1] = '09'
    elif data_[1] == 'окт.':
        data_[1] = '10'
    elif data_[1] == 'нояб.':
        data_[1] = '11'
    elif data_[1] == 'дек.':
        data_[1] = '12'
    data_[0] = int(data_[0])
    data_[1] = int(data_[1])
    data_[2] = int(data_[2])
    data0['Срок действия до'] = datetime(int(data_[2]), int(data_[1]), (data_[0]))

    # print(data0)
    return data0


def get_data():
    old_ids = []
    bad_ids = []
    ids = [1]
    ids_all = []
    page = 1
    data = []
    while True:
        url = base_url + '&Accommodation_page=' + str(page)
        page += 1
        res = r.get(url).content.decode('utf-8')
        ids = re.findall(id_pattern, res)[::2]
        if old_ids == ids:
            break
        ids_all += ids
        old_ids = ids
        if len(ids_all) >= 100:  # для тестов, удалить
            break  # для тестов, удалить
    # print(ids_all)
    c = 0
    c1 = 1
    print('ID гостиниц собраны')
    print('Собираем информацию о гостиницах...')
    percent = len(ids_all) // 100
    for hotel_id in ids_all:
        if c % percent == 0:
            c1 += 1
            print(f'{c1}%', end='')
        try:
            tmp = get_info_from_id(hotel_id)
            if not tmp:
                bad_ids.append(hotel_id)
            else:
                data.append(tmp)
        except:
            bad_ids.append(hotel_id)
        c += 1
    print('100%')

    return data, bad_ids
# get_data()
