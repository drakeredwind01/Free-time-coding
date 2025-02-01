import re
import win32clipboard # for clipboard

win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

text = """
knowledge builds Empires and today
you'll build yours use this brain hack
to become 50% smarter and gain the power
you've always dreamed
Intelligence Is A Weapon
"""

cleaned_text = re.sub(r"\n", "", text, flags=re.MULTILINE)

if __name__ == "__main__":
    print(f"{cleaned_text}")
    win32clipboard.OpenClipboard()
    win32clipboard.SetClipboardText(cleaned_text)
    win32clipboard.CloseClipboard()
'''
problem: it doesn't save to the clipboard
'''


'''
match
^   anchor begin
/d+ digit or more ('/' is backward)
:   colon
/n  new line ('/' is backward)
'''