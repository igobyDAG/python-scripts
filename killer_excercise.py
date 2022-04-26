# def killer(suspect_info, dead):
#     for suspect in suspect_info.keys():
#         killed = []
#         seen = suspect_info[suspect]
#         for i in seen:
#             if i in dead:
#                 killed.append(i)
#         if len(killed) == len(dead):
#             return suspect


# test.assert_equals(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']), 'James')
# test.assert_equals(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan')


def killer(suspect_info, dead):
    for suspect, witness in suspect_info.items():
        if set(dead) <= set(witness):
            return suspect

kira = killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['David','Kyle'])
print(kira)