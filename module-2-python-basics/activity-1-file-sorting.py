"""
Module 2 — Activity: File Sorting with os and shutil
Student: [De Leon, Christian F.]
Date: [9/27/2027]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]
I made an automatic file sorter inside folders with a python script.
basically I used a for loop to find filenames within my directory
then used multiple if conditions to manually categorize my file extensions.
Basically these files will automatically join the folder I stated in my parameters
based on what file type they have using filename.endswith.


============================================
KEY VOCABULARY
============================================
- os module: Imports the module to allow me to interact with my operating system
- shutil module: A tool used to manage these files and folders.
- file path: The location of a file or folder in my computer.
- directory: A folder that contains my files or even more folders.

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- paste your existing code here ---
list_of_files = os.listdir()
print(list_of_files)





# if os.path.exists("img"):
    
# os.mkdir("img")
# os.mkdir("doc")
# os.mkdir("vid")
# os.mkdir("other")

filename = input("enter file: ")
if os.path.exists(filename):
    print("it exists")

else:
    print("it does not exist")


#counter
img = 0
doc = 0
vid = 0
other = 0

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
        doc +=1
    elif filename.endswith(".pptx"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
        doc +=1
    elif filename.endswith(".png"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
        img += 1
    elif filename.endswith(".jpeg"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
        img += 1
    elif filename.endswith(".mp4"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")
        vid +=1
    elif filename.endswith(".mov"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")
        vid +=1

print(f"="*30)
print("Folder Summary")
print(f"Images moved: {img}")
print(f"Documents moved: {doc}")
print(f"Videos moved: {vid}")
print(f"Others moved: {other}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
Mistakes that I made when doing this activity was that at first I kept recreating my directories again and again.
so I commented those after making my directories.

Then I prioritized thinking on how to make the file sorter work first.

So the problem I was thinking of while developing this file sorter was how do I make that folder summary as instructed?
It was actually just a simple +=1 so that It increases the counter that I would lateron summarize at the end.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
This could probably have helped me alot in my Senior High days because
I often download all of the presentations from my teachers from all subjects an
manually organize it by semester, then subjects.
"""
