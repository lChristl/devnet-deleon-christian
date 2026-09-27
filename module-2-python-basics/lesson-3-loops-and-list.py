"""
Module 2 — Lesson 3: Loops & Lists
Student: [De Leon, Christian F.]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
A list is like a bookshelf then the books are values inside this bookshelf.
loops are used to repeat a block of code or commands.

============================================
KEY VOCABULARY
============================================
- list: a collection of values in one variable.
- for loop: used to repeat code for each item in a collection.
- while loop: runs the code as long as the condition is true.
- index: position of an item in a list, starting from 0.
- iteration: a single loop cycle.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
wuthering_waves = ["Denia","Aemeath","Hsin"] #favorite characters
print("My favorite characters in Wuthering Waves:")
for x in wuthering_waves:
    print(x)
print("Upcoming character in Wuthering Waves:")
print(wuthering_waves[2])

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
a mistake that could be probably made here is if I were to call out specific
value in my list instead of loop is that if I write 3, I could possibly think that Hsin is the 3rd one
but it will actually return an error because the index from a list starts from 0 so it is 0,1,2
Hsin is the '2'.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
