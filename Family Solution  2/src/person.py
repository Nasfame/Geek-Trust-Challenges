
from .utils import MALE, FEMALE

class Person:
    '''
    Class to represent a person
    used @property for better code readability
    '''
    def __init__(self, name, sex, mother):
        self.name = name
        self.sex = sex
        self.mother = mother
        self.spouse = None
        self.childrens = []

    def __str__(self):
        return "Name: {}: Mother: {}".format(self.name, self.mother)

    def __repr__(self):
        return "<{}>".format(self.name)

    @property
    def father(self):
        return [self.mother.spouse]

    @property
    def siblings(self):
        return [sibling for sibling in self.mother.childrens
                if sibling.name != self.name]

    @property
    def brother_in_laws(self):
        bro_in_laws = []
        if self.spouse:
            bro_in_laws.extend(self.spouse.brothers)
        # bro_in_laws.extend([sister.spouse for sister in self.sisters if sister.spouse]) // omitting sisters spouse
        return bro_in_laws

    @property
    def sister_in_laws(self):
        sis_in_laws = []
        if self.spouse:
            sis_in_laws.extend(self.spouse.sisters)
        # sis_in_laws.extend([brother.spouse for brother in self.brothers if brother.spouse]) // omitting brothers spouse
        return sis_in_laws

    @property
    def paternal_uncle(self):
        return self.mother.spouse.brothers

    @property
    def paternal_aunt(self):
        return self.mother.spouse.sisters
    
    @property
    def maternal_uncle(self):
        return self.mother.brothers

    @property
    def maternal_aunt(self):
        return self.mother.sisters
    
    @property
    def son(self):
        return [child for child in self.childrens
                if child.sex == MALE]

    @property
    def daughter(self):
        return [child for child in self.childrens
                if child.sex == FEMALE]

    @property
    def sibilings(self):
        return [sibling for sibling in self.mother.childrens
                if sibling.name != self.name]
    
    @property
    def brothers(self):
        return [sibling for sibling in self.mother.childrens
                if sibling.sex == MALE and sibling.name != self.name]

    @property
    def sisters(self):
        return [sibling for sibling in self.mother.childrens
                if sibling.sex == FEMALE and sibling.name != self.name]
    @property
    def grandchildren(self):
        grands = []
        for child in self.childrens:
            grands.extend(child.childrens)
        return grands
        
    def link(self, spouse):
        '''Marry one person with another
        '''
        if spouse:
            self.spouse = spouse
            spouse.spouse = self
        else:
            self.spouse = None
