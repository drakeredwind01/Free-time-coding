import re
import win32clipboard

def get_clipboard_text():
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)  # Use CF_UNICODETEXT
        win32clipboard.CloseClipboard()
        return data
    except TypeError: # Handle potential errors if CF_UNICODETEXT is not available
        try:
            data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT) # Try CF_TEXT if UNICODETEXT fails
            win32clipboard.CloseClipboard()
            return data.decode('utf-8') # Decode byte string to string
        except TypeError: # Handle if CF_TEXT is also not available
            win32clipboard.CloseClipboard()
            return ""  # Return empty string

def set_clipboard_text(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()  # Important: Clear existing clipboard content
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text) # Use CF_UNICODETEXT
    win32clipboard.CloseClipboard()

if __name__ == "__main__":
    text = get_clipboard_text()

    cleaned_text = re.sub(r"\n", "", text, flags=re.MULTILINE)

    print(f"{cleaned_text}")
    set_clipboard_text(cleaned_text)