"""
Module 2 — Activity: File Sorting with os and shutil
Student: [your name]
Date: [date]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


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


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
