class Node():
    def __init__(self, name, parent, gender):
        self.name = name
        self.parent = parent
        self.gender = gender
        if gender == "Female": self.children = []

    def addChild(self, obj):
        self.children.append(obj)


def add_child(mom, child, gender):
    exec(f'''{child}=Node(child,{mom} ,gender)''', locals(), globals())
    exec(f'''{mom}.addChild({child})''', globals(), globals())


def get_relation(name, R):  # name -obj
    if R == 'Son':
        for i in name.children:
            if i.gender=="Male" : yield i.name
    if R == 'Sibling':
        _ = getattr(name, 'parent')
        for i in _.children:
            if i.name!=name.name: yield i.name
    if R == 'Daughter':
        for i in name.children:
            if i.gender != "Male": yield i.name
    if R == 'Brother-In-Law':  # Hus of Sibling
        for i in get_relation(name, 'Sibling'):
            if i.gender == "Female": yield husbands[i.name]
    if R == 'Sister-In-Law':
        for i in get_relation(name, 'Sibling'):
            if i.gender != "Female":
                for wife, hus in husbands.items():
                    if hus == i.name: yield wife
    if R == 'Maternal-Aunt':
        for i in get_relation(name.parent, 'Sibling'):
            if i.gender=="Female": yield i.name
    if R == 'Paternal-Aunt':  # child's mom husband - father
        _ = moms[husbands[name.parent.name]]  # father's mom
        exec(f'''get_relation({_},'Duaghter')''')

    if R == 'Maternal-Uncle':
        for i in get_relation(name.parent, 'Sibling'):
            if i.gender != "Female": yield i.name

    if R == 'Paternal-Uncle':
        _ = moms[husbands[name.parent.name]]  # father's mom
        exec(f'''get_relation({_},'Son')''') # to fix bug to fix their dad.


def gameplay(_):
    if _[0] == "ADD_CHILD":
        mom, child, gender = _[1:]  # important line dont remove this line
        try:
            add_child(*_[1:])
            print("CHILD_ADDITION_SUCCEEDED")
        except Exception as e:
            print("CHILD_ADDITION_FAILED")
            print(e)
    else:
        name, Relation = _[1:]  # GET_RELATIONSHIP ”Name” “Relationship”
        try:
            exec(f'''out = get_relation({name},Relation)''',locals(),globals())
            cnt=0
            for i in out:
                cnt+=1
                print(i, end=" ")
            if cnt==0:print(None)
        except Exception as e:
            print("PERSON_NOT_FOUND")
            print(e)

#--- Driver Code-----
Anga = Node("Anga", None, "Female")  ## Initializing the family tree
husbands = {"Anga":"Shan"}  # "wife:husband"
moms = {"Shan":None}  # father:mom

_ = input().split()
while _:
    gameplay(_)
    _=input().split()

