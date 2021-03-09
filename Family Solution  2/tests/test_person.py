import pytest

from ..src.person import Person
from ..src.utils import MALE, FEMALE

def test_father(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    child_x = Person("Child_x", MALE, wife1)
    assert child_x.father == [child1]

def test_mother(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    assert child1.mother.name == mother.name

def test_siblings(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    grandChild_x = Person("GrandChild_x", MALE, wife1)
    assert grandChild_x.siblings[0] == grandChild1

def test_zero_siblings(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    assert grandChild1.siblings == []
    
def test_sister_in_laws(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup 
    assert wife1.sister_in_laws == [child2]

def test_sister_in_laws(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup 
    assert hus1.brother_in_laws == [child1]

def test_zero_sister_in_laws(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup 
    assert grandChild1.sister_in_laws == []

def test_zero_brother_in_laws(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup 
    assert grandChild1.brother_in_laws == []
    
def test_paternal_uncle(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    child_x = Person("Child_x", MALE, mother)
    mother.childrens.append(child_x)
    assert grandChild1.paternal_uncle == [child_x]

def test_maternal_uncle(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    assert grandChild2.maternal_uncle == [child1]
    
def test_paternal_aunt(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    assert grandChild1.paternal_aunt == [child2]
    
def test_maternal_aunt(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    child_x = Person("Child_x", FEMALE, mother)
    mother.childrens.append(child_x)
    assert grandChild2.maternal_aunt == [child_x]
    
def test_son(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    assert mother.son == [child1]

def test_daughter(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    assert mother.daughter == [child2]

def test_grandchild(testGroup):
    father, mother, child1, wife1, child2, hus1, grandChild1, grandChild2 = testGroup
    assert len(mother.grandchildren) == len([grandChild1, grandChild2])

def test_link():
    father = Person("father", MALE, None)
    mother = Person("mother", FEMALE, None)
    mother.link(father)
    assert mother.spouse == father
    assert father.spouse == mother
