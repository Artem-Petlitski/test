import json
data ={
    "fname":"Artem",
    "lastname":"Petlitski"
}
with open("result.json", 'w', encoding='utf-8') as json_file:
    json.dump(data,json_file)
with open("result.json", "r", encoding="utf-8")as json_file:
    user = json.load(json_file)
print(user)
# with open("input.txt", "r", encoding="utf-8") as file, open("output.txt", 'w', encoding="utf-8") as file2:
#     lst = [line.strip() for line in file]
#     file2.write("\n".join(lst))
# print(lst)