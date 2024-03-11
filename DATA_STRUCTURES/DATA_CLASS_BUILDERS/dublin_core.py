# Demonstrates Decomposition principles: for dynamic data or for not hierarchized modelling
# For example:  - science is well now for it use of hiearchized and static models
#               - globalized problems like commerce tends to be highly-dynamic
# This is an intuitive example (Despite sience is dynamic in neuro science, biology, chemistry, etc., and that globalized problems is hierarchized some times)
# THis composition was created in Python in accordance to the Dublin Core metadata model - follow it

from dataclasses import dataclass, field, fields
from typing import Optional
from enum import Enum, auto
from datetime import date

class ProductType(Enum):
    """Class for types of products (tends to grow)

    Args:
        Enum (Enum): Class that defines and manages enumerated data types
    """
    SHOE    = auto() # automatic value assignment for enum members
    PANT    = auto()
    RING    = auto()

@dataclass
class Product:
    """Composed product
    >>> identifier  = 'i09_0d9ufas'
    >>> reference   = 'model 4 of Spring Prada 2024'
    >>> materials   = ['leather', 'carbon', 'plastic']
    >>> type        = ProductType.SHOE
    >>> description = 'wonderful blue Prada shoe'
    >>> prada_shoe  = Product(identifier, reference, materials, type, description)
    >>> prada_shoe
    Product(
        identifier = 'i09_0d9ufas',
        reference = 'model 4 of Spring Prada 2024',
        materials = ['leather', 'carbon', 'plastic'],
        type = <ProductType.SHOE: 1>,
        description = 'wonderful blue Prada shoe',
        creation_date = None,
    )
    >>> creation_date =  date(2018, 11, 19)
    >>> prada_shoe  = Product(identifier, reference, materials, type, description, creation_date)
    >>> prada_shoe
    Product(
        identifier = 'i09_0d9ufas',
        reference = 'model 4 of Spring Prada 2024',
        materials = ['leather', 'carbon', 'plastic'],
        type = <ProductType.SHOE: 1>,
        description = 'wonderful blue Prada shoe',
        creation_date = datetime.date(2018, 11, 19),
    )
    """
    identifier      : str                                               # rigidly unexpected
    reference       : str               = '<untitled>'                  # rigid
    materials       : list[str]         = field(default_factory=list)   # rigid mutability
    type            : ProductType       = ProductType.SHOE              # composed product type
    description     : str               = 'nice product'                # rigid
    creation_date   : Optional[date]    = None                          # rigid optionality (should be last as **kwargs)

    def __repr__(self):
        """Customization of string representation of class instances

        Returns:
            string: customized string representation
        """
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')
        res.append(')')
        return '\n'.join(res)

if __name__ == "__main__":
    import doctest
    doctest.testmod()