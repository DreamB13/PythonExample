#딕셔너리의 items()함수와 반복문 조합
example_dictionary = {
    "A":"1",
    "B":"2",
    "C":"3"
}

print("#딕셔너리의 items()함수")
print("items(): ", example_dictionary.items())
print()

print("#딕셔너리의 items()와 반복문 조합")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key,element))
    