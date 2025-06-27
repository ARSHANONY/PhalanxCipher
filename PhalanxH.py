# -*- coding: utf-8 -*-
import string

# لیست کامل حروف فارسی به ترتیب دقیق (۳۲ حرف)
PERSIAN_ALPHABET = [
    'ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ',
    'س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی'
]

# جدول سفارشی برای هش نهایی (قابل شخصی‌سازی)
MY_CUSTOM_TABLE = 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789@#$&*+-='  # 48 کاراکتر یونیک

# تابع circular shift
def circular_shift(index, shift, length):
    return (index + shift) % length

def shift_char_advanced(ch, level):
    if ch in string.ascii_letters:
        base = ord('A') if ch.isupper() else ord('a')
        pos = ord(ch.lower()) - ord('a')
        shift = level * (pos + 1)
        new_pos = circular_shift(pos, shift, 26)
        return chr(base + new_pos)
    elif ch in PERSIAN_ALPHABET:
        pos = PERSIAN_ALPHABET.index(ch)
        shift = level * (pos + 1)
        new_pos = circular_shift(pos, shift, 32)
        return PERSIAN_ALPHABET[new_pos]
    elif ch.isdigit():
        pos = int(ch)
        shift = level * (pos + 1)
        new_pos = circular_shift(pos, shift, 10)
        return str(new_pos)
    else:
        return ch

def lvcoding_advanced(text, level):
    reversed_text = text[::-1]
    encrypted = ''.join(shift_char_advanced(ch, level) for ch in reversed_text)
    return encrypted

def custom_hash_25_chars(encrypted_text, level):
    table = MY_CUSTOM_TABLE
    table_len = len(table)

    combined = encrypted_text + str(level)
    total = 0

    for i, ch in enumerate(combined):
        total += (ord(ch) * (i + 1) * level)

    chars = []
    for i in range(25):
        index = (total + i * level) % table_len
        chars.append(table[index])

    return ''.join(chars)

# اجرای نهایی
if __name__ == "__main__":
    level = int(input("🔢 Level را وارد کن: "))
    text = input("📝 متن را وارد کن: ")

    encrypted_text = lvcoding_advanced(text, level)
    final_hash = custom_hash_25_chars(encrypted_text, level)

    print("\n✅ هش نهایی (۲۵ کاراکتر، پایدار، غیرقابل برگشت):")
    print(final_hash)

    #example:

#lv: 666 text: arshan hash: @-TAJV28*EOGX06$QUDLN4@-T         test: @-TAJV28*EOGX06$QUDLN4@-T
#lv: 667 text: arshan hash: &EPJB4#QIGC29-YDZ07*RAKN5         test: &EPJB4#QIGC29-YDZ07*RAKN5
