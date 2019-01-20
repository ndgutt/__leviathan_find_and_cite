===== Program Description =====

From user input, saves to a .txt file any paragraph within Hobbes'
Leviathan containing that input, with proper citation. Input can be a
single word, several words separated by commas, or the beginnings or
ends of words designated by the wildcard character '_'. For example:

'deliberate' returns all instances of: 'deliberate'

'deliberate_' returns all instances of: 'deliberate', 'deliberates', and
    'deliberately'

'_liber_' returns all instances of: 'liberty', 'libertie', 'libertas',
    'libertatis', 'liberality', 'liberall', 'libertines',
    'deliberation', 'deliberate', 'deliberates', deliberately', and
    'deliberatly'.


===== Text Version Used / Project Gutenberg Limitations =====

The initial plan was to use the text file of Hobbes' Leviathan directly
from <http://www.gutenberg.org/cache/epub/3207/pg3207.txt>, but there
were so many formatting irregularities that most of the code consisted
of calling secondary functions just to bring over 107 indivitual and
randomly-distributed lines of text into conformity with the rest - all
before calling the collect_and_cite function. Due to the variety and
severity of some of the irregularities, it seemed most sensible to
modify the file manually before use.

This manual approach revealed the fact that entire paragraphs were
missing from the Project Gutenberg version of the text. This program not
only made their omission obvious, but it also made their location easy
to discover. The missing paragraphs have been added manually from a
paper copy of the text. The quantity of errors seen in this process
suggests that any citation produced from this version of the text should
be double-checked before being used for publication.


===== Additional Features to Implement =====

1. Indicate to user when input words are not found.
2. Allow user to limit sections/chapters for search.
3. Accept phrases as inputs.
4. Create and incorporate a modern-to-antiquated spelling dictionary,
which will accept inputs in modern spelling (e.g., 'money') and output
passages that contain antiquated spellings (e.g., 'mony') as well.