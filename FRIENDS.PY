def common_friends(list1, list2):
    return sorted(set(list1) & set(list2))
def only_first(list1, list2):
    return sorted(set(list1) - set(list2))
ali = ["Aysel", "Murad", "Leyla", "Elvin"]
vali = ["Leyla", "Nigar", "Aysel", "Kamal"]
print(common_friends(ali, vali))
print(only_first(ali, vali))    