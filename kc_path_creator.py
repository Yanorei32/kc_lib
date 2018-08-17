class KCPathCreator:
    @classmethod
    def _create_key(cls, target_str):
        key = 0
        for c in list(target_str):
            key += ord(c)
        return key

    @classmethod
    def _create_later_key(cls, ship_id, target_str):
        magic_number__resource = [
            6657, 5699, 3371, 8909, 7719, 6229, 5449, 8561,
            2987, 5501, 3127, 9319, 4365, 9811, 9927, 2423,
            3439, 1865, 5925, 4409, 5509, 1517, 9695, 9255,
            5325, 3691, 5519, 6949, 5607, 9539, 4133, 7795,
            5465, 2659, 6381, 6875, 4019, 9195, 5645, 2887,
            1213, 1815, 8671, 3015, 3147, 2991, 7977, 7045,
            1619, 7909, 4451, 6573, 4545, 8251, 5983, 2849,
            7249, 7449, 9477, 5963, 2711, 9019, 7375, 2201,
            5631, 4893, 7653, 3719, 8819, 5839, 1853, 9843,
            9119, 7023, 5681, 2345, 9873, 6349, 9315, 3795,
            9737, 4633, 4173, 7549, 7171, 6147, 4723, 5039,
            2723, 7815, 6201, 5999, 5339, 4431, 2911, 4435,
            3611, 4423, 9517, 3243
        ]

        try:
            _ = str(ship_id)
        except ValueError:
            return 0

        target_key = cls._create_key(target_str)

        return str(
            17 * (ship_id + 7) * magic_number__resource[
                (target_key + ship_id * len(target_str)) % 100
            ] % 8973 + 1000
        )

    @classmethod
    def create(cls, ship_id, is_damage, image_size, is_enemy):
        if image_size is 'album_status':
            e = False
        else:
            e = is_enemy

        if is_damage:
            image_size += '_dmg'

        later_key = cls._create_later_key(ship_id, 'ship_' + image_size)

        return '/kcs2/resources/ship/{}/{:04d}_{}.png'.format(
            image_size, ship_id, later_key
        )

