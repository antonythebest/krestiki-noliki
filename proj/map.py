
a = ["это", "маленький", "текст", "обидно"]

print(list(map(lambda x:str(x).upper(),a)))
print(list(map(str.upper,a)))
print('')