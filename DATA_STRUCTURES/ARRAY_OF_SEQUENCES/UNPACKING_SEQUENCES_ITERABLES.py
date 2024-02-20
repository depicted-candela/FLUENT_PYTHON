import math

class NestedUnpackingMetropolitanAreas:
    """Nested Unpacking for Metropolitan Areas
    """
    def __init__(self, METRO_AREAS):
        """Initialization of the class for Unpacking Nested data about Metropolitan Areas
        """
        self.METRO_AREAS = METRO_AREAS
        self.LENGTH_METRO_AREAS = len(self.METRO_AREAS)

    def metropolitan_areas_in_weast(self):
        """Prints info about metropolitan areas in the world's weast part
        """
        ## Make an example per each subtle
        # Exact 15 spaces for names of cities
        # More than 9 spaces for latitudes and longitudes, the same number to have the same size
        print("All metropolitan areas in Weast")
        print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
        # The _ symbols are for Country's name abbreviation and the number for the metropolitan area. Lat and long comes from
        # a tuple and they should be rendered as a tuple
        for name, _, _, (lat, long) in self.METRO_AREAS:
            if long <= 0:
                # For strings a integer value, for doubles, maximum size (9) understood them as
                # strings but the string could have empty spaces since the restriction is 4 as
                # the decimal places
                print(f'{name:15} | {lat:9.4f} | {long:9.4f}')
        print("")
        print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
        # This variation is also possible (where the pos var is a tuple that can be used by using
        # the special method __getitem__ with the built-in capability []) but worst in the idiomatic sense.
        for name, _, _, pos in self.METRO_AREAS:
            if pos[1] <= 0:
                print(f'{name:15} | {pos[0]:9.4f} | {pos[1]:9.4f}')
    
    def distance_metropolitan_areas_dict(self):
        """Calculates the distance between metropolitan areas and saved them in a dictionary

        Returns:
            dict: A dictionary with distances between metropolitan areas, where keys are tuples of pairs of countries and cities and values are the distances
        """
        distance_dict_metro_areas = dict()
        for city1, abbrv_country_column, _, (lat_column, long_column) in self.METRO_AREAS:
            for city2, abbrv_country_row, _, (lat_row, long_row) in self.METRO_AREAS:
                if abbrv_country_column > abbrv_country_row: ## This because data in METRO_AREAS is organized by country
                    # Calculates the Cartesian distance between two points
                    distance_column_row_metros = math.sqrt(abs(lat_column - lat_row)**2 + abs(long_column - long_row)**2)
                    # Saves such distance in a dictionary where it key is a unique tuple of two countries
                    key_cities_countries = (city1 + " (" + abbrv_country_column + ")",
                                            city2 + " (" + abbrv_country_row + ")")
                    distance_dict_metro_areas[key_cities_countries] = distance_column_row_metros
        return distance_dict_metro_areas
    
    def sort_dict_distance_metropolitan_areas_tuple(self):
        """Sorts (in a tuple) the dictionary generated in distance_metropolitan_areas_dict by distances and returns the result

        Returns:
            tuple: A ordered tuple by distance between metropolitan areas
        """
        distance_list_metro_areas = self.distance_metropolitan_areas_dict()
        return tuple(sorted(distance_list_metro_areas.items(), key=lambda item: item[1]))
        
    def closest_metropolitan_areas(self):
        """Prints the closest metropolitan areas using the sorted tuple created in sort_dict_distance_metropolitan_areas_tuple
        """
        # Extracts the first three distances
        three_closest_metropolitan_areas = self.sort_dict_distance_metropolitan_areas_tuple()[:3]
        # Formatted printing of closest metropolitan areas
        print("Three closest metropolitan areas")
        print(f'{"Cities":43} | {"Distance":>9}')
        for (citycountry1, citycountry2), distance in three_closest_metropolitan_areas:
            print(f'{citycountry1:20} - {citycountry2:20} | {distance:9.4f}')
        print("\n")
        # Using * to print with less code but uglier our data
        print(f'{"Cities":46} | {"Distance":>9}')
        for *citiescountries, distance in three_closest_metropolitan_areas:
            print(f'{str(citiescountries):46} | {distance:9.4f}')

def main():
    ## Ordered by country
    METRO_AREAS = (
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
        ('Bogota', 'COL', 5.235, (4.627739, -74.124005)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    )
    nu = NestedUnpackingMetropolitanAreas(METRO_AREAS)
    nu.metropolitan_areas_in_weast()
    print("\n")
    nu.closest_metropolitan_areas()


if __name__ == '__main__':
    main()