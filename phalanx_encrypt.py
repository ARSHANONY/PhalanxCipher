# -*- coding: utf-8 -*-
import string

# لیست کامل حروف فارسی به ترتیب دقیق (۳۲ حرف)
PERSIAN_ALPHABET = [
    'ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ',
    'س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی'
]

# Bounce-back helper
def bounce_shift(index, shift, length):
    """
    
    """
    new_pos = index + shift
    if new_pos < length:
        return new_pos
    else:
        overflow = new_pos - (length - 1)
        back_pos = length - 1 - overflow
        return max(0, back_pos)

# موقعیت گرفتن  فارسی
def get_fa_index(ch):
    try:
        return PERSIAN_ALPHABET.index(ch)
    except ValueError:
        return -1

def shift_char_advanced(ch, level):
    # انگلیسی کوچک بزرگ
    if ch in string.ascii_letters:
        base = ord('A') if ch.isupper() else ord('a')
        pos = ord(ch.lower()) - ord('a')  # A=0
        shift = level * (pos + 1)
        new_pos = bounce_shift(pos, shift, 26)
        new_char = chr(base + new_pos)
        return new_char

    # فارسی
    elif ch in PERSIAN_ALPHABET:
        pos = PERSIAN_ALPHABET.index(ch)
        shift = level * (pos + 1)
        new_pos = bounce_shift(pos, shift, 32)
        return PERSIAN_ALPHABET[new_pos]

    # عدد
    elif ch.isdigit():
        pos = int(ch)
        shift = level * (pos + 1)
        new_pos = bounce_shift(pos, shift, 10)
        return str(new_pos)

    # سایر (فاصله، علامت، ...)
    else:
        return ch

def lvcoding_advanced(text, level):
    # گام ۱: ریورس کل متن
    reversed_text = text[::-1]
    # گام ۲: رمزنگاری
    return ''.join(shift_char_advanced(ch, level) for ch in reversed_text)

# اجرای 
if __name__ == "__main__":
    level = int(input("🔢 Level را وارد کن: "))
    text = input("📝 متن را وارد کن: ")
    encrypted = lvcoding_advanced(text, level)
    print("\n✅ متن رمزنگاری‌شده:")
    print(encrypted)
