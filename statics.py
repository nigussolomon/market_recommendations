from enum import Enum

class AgeEnum(str, Enum):
    none = 'None'
    under_18 = 'Under 18'
    between_18_and_28 = '18 - 28'
    between_29_and_38 = '29 - 38'
    between_39_and_48 = '39 - 48'
    between_49_and_58 = '49 - 58'
    above_59 = '59 above'

class GenderEnum(str, Enum):
    none = 'None'
    male = 'Male'
    female = 'Female'

class CategoryEnum(str, Enum):
    clothing = 'Clothing'
    electronics = 'Electronics Products'
    toys = 'Toys'
    beauty = 'Beauty Products'
    books = 'Books'


ages = {
    'Under 18': 1,
    '18 - 28': 2,
    '29 - 38': 3,
    '39 - 48': 4,
    '49 - 58': 5,
    '59 above': 6,
    'None': None
}

genders = {
    'Male': 1,
    'Female': 2,
    'None': None
}

categories = {
    'Electronics Products': 1,
    'Beauty Products': 2,
    'Books': 3,
    'Clothing': 4,
    'Toys': 5,
}