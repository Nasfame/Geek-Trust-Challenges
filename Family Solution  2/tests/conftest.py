import pytest

from ..src import Person
from ..src import Family
from ..src import MALE, FEMALE

@pytest.fixture
def testGroup():
    unknow = Person("unknow", FEMALE, None)
    father = Person("father", MALE, None)
    mother = Person("mother", FEMALE, None)
    father.link(mother)

    child1 = Person("child1", MALE, mother)
    mother.childrens.append(child1)
    father.childrens.append(child1)
    wife1 = Person("wife1", FEMALE, unknow)
    child1.link(wife1)

    child2 = Person("child2", FEMALE, mother)
    mother.childrens.append(child2)
    father.childrens.append(child2)
    hus1 = Person("hus1", MALE, unknow)
    child2.link(hus1)

    grandChild1 = Person("grandChild1", MALE, wife1)
    wife1.childrens.append(grandChild1)
    wife1.childrens.append(grandChild1)
    grandChild2 = Person("grandChild2", FEMALE, child2)
    child2.childrens.append(grandChild2)
    child2.childrens.append(grandChild2)
    return father, mother, child1, wife1, child2, hus1, grandChild1,\
        grandChild2

@pytest.fixture
def testFamily(testGroup):
    family = Family("test_family")
    family.add_member("father", MALE, "root")
    family.add_member("mother", FEMALE, "root", "father")
    return family
