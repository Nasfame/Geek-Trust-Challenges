import os
import sys


def str_to_class(s):
    if s in globals():
        return globals()[s]
    return None


def get_key(dict, val):
    for key, value in dict.items():
        if value == val: return key


def inializer(dict, gender):
    sys.stdout = open(os.devnull, 'w')  # block print  or  sys.stdout = tempfile.TemporaryFile()
    for mom in dict:
        for child in dict[mom]:
            try:
                exec(f'''_={mom}.name''', globals(), globals())
            except:
                exec(f'''{mom}=Node(mom,None,"Female")''', locals(), globals())
            exec(f'''{child}=Node(child,{mom},gender)''', locals(), globals())
            exec(f'''{mom}.addChild({child})''', globals(), globals())

    sys.stdout = sys.__stdout__  # enable prin


class Node():
    def __init__(self, name, parent, gender):
        self.name = name
        self.parent = parent
        self.gender = gender
        if gender == "Female": self.children = []

    def addChild(self, obj):
        self.children.append(obj)


def add_child(mom, child, gender):
    exec(f'''{child}=Node(child,{mom},gender)''', locals(), globals())
    exec(f'''{mom}.addChild({child})''', globals(), globals())


def get_relation(name, R):  # name -obj
    if R == 'Son':
        if name.gender == "Male":  # Father
            wife = str_to_class(get_key(husbands, name.name))
            get_relation(wife, 'Son')
        else:
            for i in name.children:
                if i.gender == "Male": yield i

    elif R == 'Siblings':
        _ = getattr(name, 'parent')
        for i in _.children:
            if i.name != name.name: yield i
    elif R == 'Daughter':
        if R == 'Duaghter':
            if name.gender == "Male":  # Father
                wife = str_to_class(get_key(husbands, name.name))
                get_relation(wife, 'Duaghter')
            else:
                for i in name.children:
                    if i.gender != "Male": yield i
    elif R == 'Brother-In-Law':  # Hus of Siblings or brother of spouse
        brother_in_laws = []
        if name.gender == "Female":
            try:
                hus = str_to_class(husbands[name.name])
                for i in get_relation(hus, 'Siblings'):
                    if i.gender == "Male": brother_in_laws.append(i)
            except:
                pass
            try:
                for i in get_relation(name, 'Siblings'):
                    if i in husbands: brother_in_laws.append(str_to_class(husbands[i]))
            except:
                pass
        else:
            try:
                wife = str_to_class(get_key(husbands, name.name))
                for i in get_relation(wife, 'Siblings'):
                    if i.gender == "Male": brother_in_laws.append(i)
            except:
                pass
            try:
                for i in get_relation(name, 'Siblings'):
                    if i in husbands: brother_in_laws.append(str_to_class(husbands[i]))
            except:
                pass

        for in_laws in brother_in_laws: yield in_laws

    elif R == 'Sister-In-Law':
        sister_in_laws = []
        if name.gender == "Female":
            try:
                hus = str_to_class(husbands[name.name])
                for i in get_relation(hus, 'Siblings'):
                    if i.gender != "Male": sister_in_laws.append(i)
            except:
                pass
            try:
                for i in get_relation(name, 'Siblings'):
                    if i.name in husbands.values(): sister_in_laws.append(str_to_class(get_key(husbands, i.name)))
            except:
                pass
        else:
            try:
                wife = str_to_class(get_key(husbands, name.name))
                for i in get_relation(wife, 'Siblings'):
                    if i.gender != "Male": sister_in_laws.append(i)
            except:
                pass
            try:
                for i in get_relation(name, 'Siblings'):
                    if i in husbands.values(): sister_in_laws.append(str_to_class(get_key(husbands, i.name)))
            except:
                pass
        for in_laws in sister_in_laws: yield in_laws
    elif R == 'Maternal-Aunt':
        for i in get_relation(name.parent, 'Siblings'):
            if i.gender == "Female": yield i
    elif R == 'Maternal-Uncle':
        for i in get_relation(name.parent, 'Siblings'):
            if i.gender == "Male": yield i
    elif R == 'Paternal-Aunt':  # father's sisters
        father = husbands[name.parent.name]
        outi = []
        exec(f'''outi.append(get_relation({father},'Siblings'))''', locals(), globals())
        for x in outi:
            for i in x:
                if i.gender != "Male": yield i
    elif R == 'Paternal-Uncle':  # father's bros
        father = husbands[name.parent.name]
        outi = []
        exec(f'''outi.append(get_relation({father},'Siblings'))''', locals(), globals())
        for x in outi:
            for i in x:
                if i.gender == "Male": yield i


def gameplay(_):
    if _[0] == "ADD_CHILD":
        mom, child, gender = _[1:]  # important line dont remove this line
        try:
            add_child(*_[1:])
            print("CHILD_ADDITION_SUCCEEDED")
        except Exception as e:
            print("CHILD_ADDITION_FAILED")
    else:
        name, Relation = _[1:]  # GET_RELATIONSHIP ”Name” “Relationship”
        try:
            exec(f'''out = get_relation({name},Relation)''', locals(), globals())
            cnt = [i.name for i in out]
            if len(cnt) > 0:
                print(*cnt)
            else:
                print("NONE")
        except Exception as e:
            print("PERSON_NOT_FOUND")


'''Inializing the Family Tree'''

husbands = {"Anga": "Shan", "Amba": "Chit", "Lika": "Vich", "Chitra": "Aras", "Satya": "Vyan", "Dritha": "Jaya",
            "Jnki": "Arit", "Satvy": "Asva", "Krpi": "Vyas"}  # "wife:husband"
female_children = {'Anga': ['Satya'], 'Amba': ['Dritha', 'Tritha'], 'Lika': ['Villa', 'Chikka'], 'Chitra': ['Jnki'],
                   'Satya': ['Atya'], 'Jnki': ['Lavnya'], 'Krpi': ['Krithi']}  # mom:children
male_children = {'Anga': ['Chit', 'Ish', 'Vinch', 'Aras'], 'Amba': ['Vritha'], 'Chitra': ['Ahit'],
                 'Satya': ['Vyas', 'Asva'], 'Dritha': ['Yodhan'], 'Jnki': ['Laki'], 'Satvy': ['Vasa'],
                 'Krpi': ['Kriya']}


def main():
    inializer(female_children, 'Female')
    inializer(male_children, 'Male')

    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = "input_family.txt"
    finally:
        with open(input_file, 'r') as f1:
            content = f1.readlines()
            content = [i.strip() for i in content]  # to remove\n in readlines()
            for _ in content: gameplay(_.split())


if __name__ == "__main__":
    main()
