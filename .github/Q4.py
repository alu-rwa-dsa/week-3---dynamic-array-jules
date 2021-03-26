
list = dict()

class our_list:
    def __init__(self):

        print("Hello")

    def add(self, name, age, faculty, country):
        list["name"] = name
        list["age"] = age
        list["Faculty"] = faculty
        list["country"] = country
        return list

    def a_remove(self, key):
        del list[key]
        return list

    def a_modify(self, name, faculty, country):
        list.update({"name":name})
        list.update({"Faculty": faculty})
        list.update({"country":country})
        return list

    def a_lookup(self, i):
        for key in list.keys():
            if key == i:
                return "found"
            else:
                return "not found"


if __name__ == "__main__":
    p = our_list()

    print(p.add("IRADUKUNDA", 26, "CS", "Rwanda"))

    print(p.a_remove("Faculty"))

    print(p.a_modify("JULES", "CS", "IBT"))

    print(p.a_lookup("name"))