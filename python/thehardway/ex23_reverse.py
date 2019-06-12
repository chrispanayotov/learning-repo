import sys
script, bytesfile = sys.argv


def main(language_file):
    line = language_file.readline()

    if line:
        print_line(line)
        return main(language_file)


def print_line(line):
    next_lang = line.strip()
    raw_bytes = next_lang.decode()
    #cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "end")


languages = open("languages_raw.txt", 'rb')

main(languages)
