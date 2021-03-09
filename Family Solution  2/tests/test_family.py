import pytest

from ..src.family import Family
from ..src.utils import MALE, FEMALE, DuplicateMemberEntryError, Person403, Person404

def test_find_members(testFamily):
    father = testFamily.find_member("father")
    assert father.name == "father"

def test_find_members_zero(testFamily):
    person = testFamily.find_member("x_man")
    assert person == None
    
def test_add_member(testFamily):
    response = testFamily.add_member("child", MALE, "mother")
    assert response == "CHILD_ADDITION_SUCCEEDED"
    members = [member.name for member in testFamily.members]
    assert "child" in members

def test_duplicate_add(testFamily):
    with pytest.raises(DuplicateMemberEntryError) as e:
        response = testFamily.add_member("father", MALE, "root")
    assert "already exists" in str(e.value)

def test_person404(testFamily):
    response = testFamily.add_member("child3", MALE, "x_man")
    assert response == "PERSON_NOT_FOUND"

def test_person403(testFamily):
    response = testFamily.add_member("child4", MALE, "father")
    assert response == "CHILD_ADDITION_FAILED"

def test_get_relationship(testFamily):
    respose = testFamily.add_member("child4", MALE, "mother")
    testFamily.add_member("wife1", FEMALE, "not family", "child4")
    testFamily.add_member("grand1", MALE, "wife1", "")
    person = testFamily.get_relationship("wife1", "Son")
    assert person.strip() == "grand1"
