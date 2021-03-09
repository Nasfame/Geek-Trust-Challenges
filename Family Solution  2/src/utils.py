''' Helper function
'''

FUNC_MAPPER = {"Paternal-Uncle": "paternal_uncle",    #This is a relation input string To Function name mapper,
               "Maternal-Uncle": "maternal_uncle",    # Used for getattr 
               "Paternal-Aunt": "paternal_aunt",
               "Maternal-Aunt": "maternal_aunt",
               "Sister-In-Law": "sister_in_laws",
               "Brother-In-Law": "brother_in_laws",
               "Son": "son",
               "Daughter": "daughter",
               "Siblings": "siblings",
               }

INPUT_FUNC_MAPPER = {"ADD_CHILD": "add_member",
                     "GET_RELATIONSHIP": "get_relationship"}

FEMALE = "Female"
MALE = "Male"

#Custom Errors
class DuplicateMemberEntryError(ValueError):
    def __init__(self, message):
        self.message = message

class Person404(ValueError):
    def __init__(self, message):
        self.message = message

class Person403(ValueError):
    def __init__(self, message):
        self.message = message

class RelationshipNotFound(ValueError):
    def __init__(self, message):
        self.message = message

class InvalidParameters(ValueError):
    def __init__(self, message):
        self.message = message
