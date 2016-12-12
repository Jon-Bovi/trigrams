"""Program that uses creates trigram text."""


import io
import re
import random


def main(src, num):
    """Main function."""
    tri_dict = parse_into_dict(src)
    return gen_text(tri_dict, num)


def parse_into_dict(src):
    """Take file and return trigram dictionary."""
    text_file = io.open(src, encoding="utf-8")
    text = cleanup(text_file.read()).split()
    text_file.close()
    tri_dict = {}
    for i in range(len(text) - 2):
        next_two = text[i] + ' ' + text[i + 1]
        tri_dict.setdefault(next_two, []).append(text[i + 2])
    return tri_dict


def gen_text(dict, num):
    """Return trigram text."""
    key = random.choice(list(dict.keys()))
    text = '...\n' + key
    for i in range(num - 2):
        word = random.choice(dict[key])
        text += " " + word
        key = key.split()[-1] + " " + word
        if key not in dict:
            key = random.choice(list(dict.keys()))
    return text + '\n...'


def cleanup(text):
    """Remove unwanted punctuation."""
    clean_text = re.sub('[^a-zA-Z0-9.\- ]', ' ', text)
    return clean_text

if __name__ == '__main__':
    """Run main function when trigrams run on commmand line."""
    import sys
    user_input1 = sys.argv[1]
    user_input2 = sys.argv[2]
    print(main(user_input1, int(user_input2)))
