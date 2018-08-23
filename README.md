# kclib
Python kancolle library

## Function refs

### KCPathCreator

```Python
from kc_path_creator import KCPathCreator
KCPathCreator.create(ship_id, is_damage, image_size, is_enemy)
```

|type|name|description|example|
|:--|:--|:--|:--|
|int|ship_id|Kancolle ship id. (not 図鑑No.)|1, 2, 6, 7, 9, etc...|
|bool|is_damage|Is damage.|True or False|
|string|image_size|Image size.|'full', 'banner', etc...|
|bool|is_enemy|Is enemy.|True or False|

### KCRandomServerSelector

```Python
from kc_random_server_selector import KCRandomServerSelector
ret = KCRandomServerSelector.select()
```

Return random server URL. (example: `'http://203.104.209.39'`)

## Example

```Python
>>> from kc_random_server_selector import KCRandomServerSelector
>>> from kc_path_creator import KCPathCreator
>>> KCRandomServerSelector.select() + KCPathCreator.create(116, False, 'full', False)
'http://203.104.209.39/kcs2/resources/ship/full/0116_7213.png'
>>>
```

Enjoy!

