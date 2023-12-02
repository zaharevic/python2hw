def longest_words(file):
    flag = True
    max_len = -1
    max_len_words = []

    while (flag):
        string = file.readline()
        strin = string.split()
        if string != "":
            for i in range(len(strin)):
                for j in range(len(str(i))):
                    if len(str(strin[j])) > max_len:
                        max_len_words = [strin[j]]
                        max_len = len(str(strin[j]))
                    elif i == max_len:
                        max_len_words.append(strin[j])
        else:
            flag = False
    print(*max_len_words)


def main():
    with open("article.txt", "r", encoding="utf-8") as file:
        longest_words(file)


if __name__ == "__main__":
    main()
