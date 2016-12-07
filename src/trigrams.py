"""Program that uses creates trigram text."""


import io


def main(src, num):
    """Main function."""
    tri_dict = parse_into_dict(src)
    return gen_text(tri_dict, num)


def parse_into_dict(src):
    """Take file and return trigram dictionary."""
    text = io.open(src, encoding="utf-8").read()
    text = cleanup(text).split(' ')
    tri_dict = {}
    for i in range(len(text) - 2):
        next_two = text[i] + ' ' + text[i + 1]
        try:
            tri_dict[next_two].append(text[i + 2])
        except:
            tri_dict.setdefault(next_two, [text[i + 2]])
    return tri_dict


def cleanup(text):
    text = text.replace('\n', ' ')
    text = text.replace('--', ' ')
    text = text.lower().replace('[^a-z0-9.\-]', ' ')
    text = text.replace(',', '')
    text = text.replace(')', ' ')
    text = text.replace('(', ' ')
    return text
