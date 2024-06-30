# key : value
#
# 41 => kocaeli, 34 => istanbul
#
# sehirler = ['kocaeli', 'istanbul']
# plakalar = [41, 34]
#
# plakalar = {'kocaeli': 41, 'istanbul': 34}
#
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])
#
# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'
#
# print(plakalar)

users = {
    'murat': {
        'age': 42,
        'roles': ['user'],
        'email': 'admin@muratyurur.com',
        'address': 'istanbul',
        'phone': '123123123',
    },
    'omerbugra': {
        'age': 2,
        'roles': ['admin', 'user'],
        'email': 'omerbugra@muratyurur.com',
        'address': 'tuzla',
        'phone': '321321321',
    },
}

print(users['omerbugra']['roles'][0])
