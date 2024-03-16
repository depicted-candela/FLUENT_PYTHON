from operator import itemgetter, attrgetter
from collections import namedtuple
import random


class MetroGetter:
    LatLon = namedtuple("LatLon", "lat lon")
    Metropolis = namedtuple("Metropolis", "name cc pop coord")
    metro_data = [
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
        ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
        ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
        ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
    ]

    metro_attrs = (
        "name",
        "cc",
        "pop",
        "coord.lat",
        "coord.lon",
    )

    def create_metro_areas(self, Metropolis=Metropolis, LatLon=LatLon):
        self.metro_areas = [
            Metropolis(name, cc, pop, LatLon(lat, lon))
            for name, cc, pop, (lat, lon) in self.metro_data
        ]

    def sorted_itemgetter_by_item(self, item_pos):
        """
        >>> metro_getter = MetroGetter()
        >>> metro_getter.sorted_itemgetter_by_item(1)
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
        """
        for city in sorted(self.metro_data, key=itemgetter(item_pos)):
            print(city)

    def sorted_lambda_by_item(self, item_pos):
        """
        >>> metro_getter = MetroGetter()
        >>> metro_getter.sorted_lambda_by_item(1)
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
        """
        for city in sorted(self.metro_data, key=lambda city: city[item_pos]):
            print(city)

    def tuples_of_certain_items(self, a, /, *c, **kwargs):
        """getting values by items with itemgetter"""
        city = itemgetter(random.randint(0, 4))
        city = city(self.metro_data)
        kvalues = tuple(kwargs.values())
        city_data = itemgetter(a, *c, *kvalues)
        city_data = city_data(city)
        print(city_data)

    def tuples_of_specific_attributes(self, a, /, *c, **kwargs):
        """getting values by attributes with attrgetter"""
        city = itemgetter(random.randint(0, 4))
        self.create_metro_areas()
        city = city(self.metro_areas)
        kvalues = tuple(kwargs.values())
        city_data = attrgetter(a, *c, *kvalues)
        city_data = city_data(city)
        print(city_data)

    def __call__(self, a, /, *c, **kwargs):
        return self.tuples_of_certain_items(a, *c, **kwargs)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    metro_getter = MetroGetter()
    for i in range(5):
        rn = random.sample(range(4), 4)
        metro_getter.tuples_of_certain_items(
            rn[0],
            rn[1],
            p3=rn[-1],
        )
        metro_getter(rn[0], p1=rn[1], p2=rn[2], p3=rn[3])
        metro_getter.tuples_of_specific_attributes(
            metro_getter.metro_attrs[rn[0]],
            metro_getter.metro_attrs[rn[1]],
            p3=metro_getter.metro_attrs[rn[-1]],
        )
