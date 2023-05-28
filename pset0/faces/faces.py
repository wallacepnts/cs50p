def main():
    convert(input())


def convert(emoticon):
    # Essa função transforma os antigos emoticon em emoji
    emoji = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    print(emoji)


main()
