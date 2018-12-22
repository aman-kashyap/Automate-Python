#Default function

def select_sex(sex='Unknown'):
    if sex is 'm':
        print("Male")
    elif sex is 'f':
        print("female")
    else:
        print(sex)

select_sex()
select_sex('m')
select_sex('f')

#default function with keyword argument

def sentence(name="aman", action="study", item="college"):
    print(name,action,item)

sentence()
sentence("abhishek","goes","home")
sentence(name="jhummi",item="school")

