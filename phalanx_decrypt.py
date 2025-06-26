# -*- coding: utf-8 -*-
import string

PERSIAN_ALPHABET = [
    'ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ',
    'س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ی'
]

def bounce_shift(index, shift, length):
    new_pos = index + shift
    if new_pos < length:
        return new_pos
    else:
        overflow = new_pos - (length - 1)
        back_pos = length - 1 - overflow
        return max(0, back_pos)

def find_possible_originals(ch, level):
    candidates = []

    # انگلیسی
    if ch in string.ascii_letters:
        base = ord('A') if ch.isupper() else ord('a')
        ch_pos = ord(ch) - base
        for i in range(26):
            shift = level * (i + 1)
            new_pos = bounce_shift(i, shift, 26)
            if new_pos == ch_pos:
                candidates.append(chr(base + i))
        return candidates

    # فارسی
    elif ch in PERSIAN_ALPHABET:
        ch_pos = PERSIAN_ALPHABET.index(ch)
        for i in range(32):
            shift = level * (i + 1)
            new_pos = bounce_shift(i, shift, 32)
            if new_pos == ch_pos:
                candidates.append(PERSIAN_ALPHABET[i])
        return candidates

    # عدد
    elif ch.isdigit():
        ch_pos = int(ch)
        for i in range(10):
            shift = level * (i + 1)
            new_pos = bounce_shift(i, shift, 10)
            if new_pos == ch_pos:
                candidates.append(str(i))
        return candidates

    else:
        return [ch]  # علائم و فاصله‌ها

def decrypt_limited(encrypted_text, level):
    result = []
    for ch in encrypted_text:
        possible = find_possible_originals(ch, level)
        if len(possible) == 1:
            result.append(possible[0])
        elif len(possible) == 0:
            result.append('?')  # هیچ گزینه‌ای پیدا نشد
        else:
            result.append(f"[{''.join(possible)}]")  # چند کاندیدا 
    reversed_result = ''.join(result)[::-1]
    return reversed_result

# اجرا
if __name__ == "__main__":
    level = int(input("🔢 Level را وارد کن: "))
    text = input("🔒 متن رمزنگاری‌شده را وارد کن: ")

    output = decrypt_limited(text, level)
    print("\n🧩 متن احتمالی (با حروف جایگزین اگر لازم بود):")
    print(output)
