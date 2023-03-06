# Function that prints all the days of the week
def print_days_of_week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    print(", ".join(days))


print_days_of_week()


# Function that asks user to input a sentence and then replaces every second word with "Hello"
def replace_word():
    sentence = input("PLease enter a sentence: ")
    new_sentence = ""
    index = 0
    for word in sentence.split():
        if index % 2 == 1:
            new_sentence += "Hello "
        else:
            new_sentence += word + " "
        index += 1
    return new_sentence


print(replace_word())
