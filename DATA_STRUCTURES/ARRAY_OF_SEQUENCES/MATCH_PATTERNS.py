class InterestedParty:

    def __init__(self, type, names: tuple, lastnames: tuple):
        self.type       = type
        self.names      = names
        self.lastnames  = lastnames

class ColombianLot:

    def __init__(self, area, condition):
        self.area                   = area
        self.condition              = condition
        self.interested_parties     = tuple()
        while(True) :
            if True if input("There are exist more interested parties? (y, n): ") == 'y' else False: break
            interested_party_type
            interested_party_type_id    = input("Input the interested party type (ti: T. identidad, cc: C. ciudadanía): ")
            if interested_party_type_id != "cc" or interested_party_type_id != "tid": None
            interested_party_names      = self.__structures_names_intuples(input("Input the names: "))
            interested_party_last_names = self.__structures_names_intuples(input("Input the last names: "))
            self.__destructures_names_intuples((interested_party_type_id,
                                              interested_party_names,
                                              interested_party_last_names))
            
    def __structures_names_in_tuples(interested_party_names: str) -> tuple:
        return tuple(interested_party_names.strip().split())
    
    def __destructures_names_in_tuples(self, interested_party_names_tuple: tuple):
        match interested_party_names_tuple:
            case (type_id, names, (first_lastname, second_lastname)) if type_id:
                self.interested_parties.append(InterestedParty(type, names, (first_lastname, second_lastname)))
            case (type, names, (first_lastname, _, second_lastname)) if type_id:
