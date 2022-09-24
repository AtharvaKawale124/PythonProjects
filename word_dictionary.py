import json
data = json.load(open("data.json"))
x='y'
while(x=='y'):

    def meaning(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        else:
            print("Wrong input.")

    word = input("Enter the word to search :")
    output = meaning(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    x=input("Do you want to search again(y/n) :")