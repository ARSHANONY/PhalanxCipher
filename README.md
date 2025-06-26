<div align="center">

# 🛡️ PhalanxCipher  
### A hybrid, multilingual, level-based encryption engine built with pure Python

<img src="https://img.shields.io/badge/Language-Python%203-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Encryption-Level%20Based-green?style=flat-square"/>
<img src="https://img.shields.io/badge/Multilingual-English%20%7C%20Persian%20%7C%20Digits-purple?style=flat-square"/>
<img src="https://img.shields.io/badge/Status-Alpha-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/Color%20Output-Terminal%20Only-red?style=flat-square"/>

</div>

---

> 🔐 **PhalanxCipher** is a smart, multilingual text cipher designed for creative obfuscation.  
> It’s more than Caesar or ROT13 — it’s Level-based, reverse-first, bounce-shifted, and Farsi‑friendly 🇮🇷

---

## ✨ Key Features

- 🔢 Level-based encryption logic
- 🔁 Reverses the full string before encoding
- 🔄 Uses bounce-back instead of wrap-around
- 🌐 Supports Persian (32), English (26), and Digits (10)
- 🎨 Color-coded decryption (Green, Yellow, Red, Purple)
- 🧠 Smart guessing engine for decryption accuracy
- 🧪 Fully educational, minimal dependencies

---

## 🔍 Language Modes

| Mode | Description                      |
|------|----------------------------------|
| `E`  | English characters only 🇬🇧        |
| `F`  | Persian (Farsi) characters only 🇮🇷 |
| `MIX`| Mixed: English + Persian + Digits 🌐 |

> ⚠️ **Note:** Colored output is only visible in terminals that support ANSI escape codes.  
> Future versions will include full GUI and web visualization.

---

## 🧠 How Encryption Works

1. Input text is **reversed**
2. For each letter:
   - Find its index in the relevant alphabet
   - Multiply that index by the selected **Level**
   - Jump forward in the alphabet
   - If it goes past the end, it **bounces back** from the edge
3. Non-alphabet characters (e.g., symbols, emojis) remain unchanged

---

## 🚀 Getting Started

### 🔧 Requirements

```bash
pip install colorama
