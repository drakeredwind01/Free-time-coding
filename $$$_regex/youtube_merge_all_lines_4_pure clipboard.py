import re
import win32clipboard # for clipboard

'''
only grabed one line from gemini
win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text) # Use CF_UNICODETEXT
still wrong because it said to put 'text' and not 'cleaned_text'
'''

win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

text = """
0:00
knowledge builds Empires and today
0:01
you'll build yours use this brain hack
0:04
to become 50% smarter and gain the power
0:06
you've always dreamed
Intelligence Is A Weapon
"""

cleaned_text = re.sub(r"\n", "", text, flags=re.MULTILINE)

if __name__ == "__main__":
    print(f"{cleaned_text}")
    win32clipboard.OpenClipboard()
    # win32clipboard.SetClipboardText(cleaned_text)
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, cleaned_text)  # Use CF_UNICODETEXT
    win32clipboard.CloseClipboard()



'''
match
^   anchor begin
/d+ digit or more ('/' is backward)
:   colon
/n  new line ('/' is backward)
'''