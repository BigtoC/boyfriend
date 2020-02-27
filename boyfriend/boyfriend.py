import random


__all__ = ['say']


def say():
    text = [
        "親愛的今天過得好嗎？",
        "吃飽了嗎？",
        "天氣冷多穿點唷～",
        "寶貝晚安~",
        "老婆我愛你！"
    ]
    print(random.choice(text))

def main():
    say()


if __name__ == '__main__':
    main()
