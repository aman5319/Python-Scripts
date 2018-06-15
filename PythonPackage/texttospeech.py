#!/usr/bin/python3

import argparse
import textwrap

from gtts import gTTS
import os
import re
import threading
import requests


def lang_dictt():
    lang_dict = {'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali',
                 'ca': 'Catalan', 'zh': 'Chinese', 'zh-cn': 'Chinese (Mandarin/China)',
                 'zh-tw': 'Chinese (Mandarin/Taiwan)', 'zh-yue': 'Chinese (Cantonese)', 'hr': 'Croatian',
                 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English',
                 'en-au': 'English (Australia)', 'en-uk': 'English (United Kingdom)',
                 'en-us': 'English (United States)', 'eo': 'Esperanto',
                 'fi': 'Finnish', 'fr': 'French', 'de': 'German', 'el': 'Greek', 'hi': 'Hindi',
                 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'it': 'Italian',
                 'ja': 'Japanese', 'km': 'Khmer (Cambodian)', 'ko': 'Korean', 'la': 'Latin',
                 'lv': 'Latvian', 'mk': 'Macedonian', 'no': 'Norwegian', 'pl': 'Polish',
                 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian',
                 'sr': 'Serbian', 'si': 'Sinhala', 'sk': 'Slovak', 'es': 'Spanish',
                 'es-es': 'Spanish (Spain)', 'es-us': 'Spanish (United States)', 'sw': 'Swahili',
                 'sv': 'Swedish', 'ta': 'Tamil', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian',
                 'vi': 'Vietnamese', 'cy': 'Welsh'}
    return lang_dict


def speak(text, lang="en", save=""):
    tts = gTTS(text=str(text), lang=lang)
    tts.save("hi.mp3")
    os.system("mpg321 -q hi.mp3")
    if save.strip() == "":
        os.remove('hi.mp3')
    else:
        os.rename("hi.mp3", str(save))


def speakParallel(text, lang='en'):
    for data in text:
        tts = gTTS(text=data, lang=lang)
        print(data.strip("\n"))
        tts.save("hi.mp3")
        os.system("mpg321 -q hi.mp3")
        os.remove("hi.mp3")


def main():
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = textwrap.dedent('''\
             This is utility tool for text to speech
             --------------------------------
                 [-h /--help] [--tts / -t] [--lang_list / -ll]
                 [--search_lang /-sl]    [{-t | -l}] 
                 [-t | -l | -s] [-f]
                 Sample code 
                 hearit --tts "नमस्ते अमन अपका स्वगत है" --save "man.mp3" --lang "hi"
                 hearit -f "abc.txt"
                 hearit -sl "English"
                                 
             '''))
    parser.add_argument("--tts" ,"-t", help="Enter the text to speak")
    parser.add_argument("--lang" ,"-l", help="enter the specific language code default english(en)")
    parser.add_argument("--lang_list","-ll" ,nargs='?', help="see the language list and code", const='c')
    parser.add_argument("--search_lang","-sl", type=str, help="search the language and code")
    parser.add_argument("--file","-f", help="enter the file which you want to be read")
    parser.add_argument("--save","-s", help="use with --tts option to save it with any file format")
    args = parser.parse_args()

    if args.tts and args.lang is None and args.save is None:
        speak(args.tts)

    if args.tts and args.lang and args.save is None:
        speak(args.tts, str(args.lang))

    if args.lang_list:
        for key, value in lang_dictt().items():
            print("Code " + key + " Language " + value)
        print("Total language support is ", len(lang_dictt()))

    if args.search_lang:
        found = 0
        lang = lang_dictt()
        search = str(args.search_lang).strip()
        for key, value in lang.items():
            value = value.strip()
            search_result = re.search(search, value, re.M | re.I)
            if search_result:
                print("Code " + key + " Language " + value)
                found += 1
        if found == 0:
            print("Not found ")

    if args.file:
        try:
            with open(str(args.file), "r") as file_read:
                list_data = file_read.read().split(". ")
                speakParallel(list_data)
        except Exception as e:
            print("File read Error")

    if args.tts and args.save and args.lang is None:
        speak(args.tts, save=args.save)

    if args.tts and args.save and args.lang:
        speak(args.tts, lang=args.lang, save=args.save)


if __name__ == "__main__":
    try:
        requests.get("https://www.google.com", timeout=2)
        main()
    except Exception as e:
        print("Requires Internet" + e)
