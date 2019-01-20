# program name: __leviathan_find_and_cite.py
# required file in program folder: __leviathan.txt
# author name: Nathan Gutt
# created: August 11, 2017; revised January 19, 2019


import re
import tkinter as tk
from tkinter import simpledialog


class Chapter: 
    def __init__(self, text):
        self.name = text[:text.index('.')]
        self.text = text
        self.list = re.sub(r'\n{2,10}',
                           '\r\n\r\n',
                           text).split('\r\n\r\n')
        while '' in self.list:
            self.list.remove('')
        while ' ' in self.list:
            self.list.remove(' ')


def return_between(start, end, text):
    '''Return the string between (and including) start/end subtrings.'''
    return text[text.index(start):text.index(end)+len(end)] 


def margin_cut(text):
    '''Remove all substrings between '<' and '>' characters.'''
    new_text = text
    
    while new_text.find('<') != -1: 
        temp_text = (new_text[:new_text.index('<')]
                     + new_text[new_text.index('>')+1:])
        new_text = temp_text
        
    return new_text


def find(text,input_list):
    '''Return true iff word from user input is found in text.'''
    block = text.lower()
    found = False
    
    for string in input_list:
        word = string.lower()
        wild_start = (word.startswith('_'))
        wild_end = (word.endswith('_'))
        
        if not (wild_start or wild_end):  # no wild sides
            index = block.find(word)
            while index > -1:
                if ((index == 0 or not block[index-1].isalnum())
                    and ((len(block) <= index + len(word))
                         or not block[index + len(word)].isalnum())):
                    found = True
                index = block.find(word, index+1)
                
        elif not wild_start:              # only wild at end
            index = block.find(word[:-1])
            while index > -1:
                if (index == 0 or not block[index-1].isalnum()):
                    found = True
                index = block.find(word, index+1)
                
        elif not wild_end:                # only wild at start
            index = block.find(word[1:])
            while index > -1:
                if ((len(block) <= index + len(word)-1)
                    or not block[index + len(word)-1].isalnum()):
                    found = True
                index = block.find(word, index+1)
                
        else:                             # both sides wild
            found = word[1:-1] in block
            
    return found


def collect_and_cite(input_string):
    '''Splits text into sections and writes passages to outfile.'''
    infile = open("__leviathan.txt", "r") 
    text = infile.read()

    dedic = return_between('TO MY MOST', 'servant, Thomas Hobbes.', text)
    
    intro = return_between('THE INTRODUCTION', 'other Demonstration.', text)
    intro = margin_cut(intro)
    intro_list = intro.split('\n\n') 
    
    body = return_between('CHAPTER I.', 'my Countrey.', text).lstrip()
    body = margin_cut(body)
    body_list = body.split('CHAPTER ')
    chapter_list = []
    for ch in range(1,len(body_list)):
        chapter_list.append(Chapter(body_list[ch]))

    conc = return_between('A REVIEW,', 'welcome.', text)
    conc = margin_cut(conc)
    conc_list = conc.split('\n\n')

    input_string = input_string.replace(' ','')
    
    outfile = open('%s.txt' % input_string.replace(',',', '), 'w+')
    outfile.write(
        "[ All paragraphs in Hobbes' Leviathan containing the word(s): "
        + input_string.replace(',',', ') + " ]\n\n\n")
    
    input_list = input_string.split(',')

    if find(dedic.lower(),input_list):
        outfile.write(dedic.replace('\n',' '))
        outfile.write(' (Leviathan, Letter Dedicatory)\n\n')

    for para in intro_list[1:]:
        if find(para,input_list):
            outfile.write(para.replace('\n',' '))
            outfile.write(' (Leviathan, Introduction %s)\n\n'
                          % str(intro_list.index(para)))

    for ch in chapter_list:
        for para in ch.list[1:]:
            if find(para,input_list):
                outfile.write(para.replace('\n',' '))
                outfile.write(' (Leviathan, %s.%s)\n\n'
                              % (str(ch.name), str(ch.list.index(para))))

    for para in conc_list[1:]:
        if find(para,input_list):
            outfile.write(para.replace('\n',' '))
            outfile.write(' (Leviathan, Review and Conclusion %s)\n\n'
                          % str(conc_list.index(para)))


def main():
    root = tk.Tk()
    root.withdraw()

    window_title = "Find and Cite from Hobbes' Leviathan"
    text_for_user = [""]
    text_for_user.append(" Input words in the field below\n"
                         + " - Separate multiple words with commas "
                         + "(e.g., liberty, justice)\n"
                         + " - Use '_' for wildcards at the start or end"
                         + "of a word (e.g., oblig_)")
    
    running = True
    while(running):
        input_string = simpledialog.askstring(window_title,
                                              ''.join(text_for_user),
                                              parent=root)
        root.withdraw()

        if input_string is None:
            running = False

        else:
            error_test = input_string.replace(',','')
            error_test = error_test.replace('_','')
            error_test = error_test.replace('-','')
            error_test = error_test.replace(' ','')

            if not error_test.isalpha():
                text_for_user[0] = ("Error: input '"
                                    + input_string
                                    + "' contains unrecognized characters\n"
                                    + " - Use only a-z, A-Z, underscores, "
                                    + " dashes, and commas\n\n")
            else:
                collect_and_cite(input_string.lower())
                text_for_user[0] = ("Previous input: " + input_string.lower()
                                    + "\n - See program folder for output\n\n")


main()
