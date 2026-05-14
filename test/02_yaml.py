#! /usr/bin/eny python3
#! -*- coding: utf-8 -*-

import yaml

obj = yaml.load(
    '''
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
''', Loader=yaml.FullLoader)

print(obj)