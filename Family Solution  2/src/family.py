
from .person import Person
from .utils import FUNC_MAPPER, Person404, Person403,\
    DuplicateMemberEntryError, RelationshipNotFound,\
    FEMALE, MALE

def format_output(fn):
    '''It will create a formatted output from various kind
    of object. I made this bacause i like the layerd concepts,
    so this will act something like a middleware
    '''
    def fun_wrapper(*largs, **kwargs):
        try:
            result = fn(*largs, **kwargs)
            if isinstance(result, list) and result:
                return " ".join([element.name for element in result])
            elif isinstance(result, str) and result:
                return result
            else:
                return "None"
        except Exception as e:
            if isinstance(e, Person404):
                return "PERSON_NOT_FOUND"
            if isinstance(e, Person403):
                return "CHILD_ADDITION_FAILED"
            else:
                raise (e)
    return fun_wrapper


class Family:
    '''
    Class to represent a family, each members will a Person Object
    '''

    def __init__(self, family_name):
        self.family_name = family_name
        self.members = []
        self._initilize_family_tree()

    def __str__(self):
        return "Name: {}: Members: {}".format(self.family_name, self.members)

    def __repr__(self):
        return "<{}>".format(self.family_name)

    def _initilize_family_tree(self):
        ghost_mother = Person("not family", FEMALE, None)
        self.members.extend([ghost_mother])

    @format_output
    def get_relationship(self, name, relationship):
        person = self.find_member(name)
        if not person:
            raise Person404("{} not found".format(name))
        if relationship not in FUNC_MAPPER:
            raise RelationshipNotFound("{} not found".format(relationship))
        return getattr(person, FUNC_MAPPER[relationship])

    @format_output
    def add_member(self, name, sex, mother_name, spouse_name=None):
        root = False
        if self.find_member(name):
            raise DuplicateMemberEntryError("{} already exists".format(name))

        if mother_name == "root":
            root = True
        if root:
            mother = None
        else:
            mother = self.find_member(mother_name)
            if not mother:
                raise Person404("Mother: {} not found".format(mother_name))
            if mother.sex != FEMALE:
                raise Person403("Name: {} does not have any Power".format(mother_name))

        person = Person(name, sex, mother)
        if spouse_name:
            spouse = self.find_member(spouse_name)
            spouse.link(person)

        if not root:
            mother.childrens.append(person)
            if mother.spouse:
                mother.spouse.childrens.append(person)
        self.members.append(person)
        return "CHILD_ADDITION_SUCCEEDED"

    def find_member(self, name):
        member = [person for person in self.members if person.name == name]
        if len(member) == 1:
            return member[0]
        else:
            return None

