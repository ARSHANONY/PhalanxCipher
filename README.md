<div align="center">

# 🛡️ PhalanxCipher
### A hybrid, multilingual, level-based encryption engine built with pure Python

<img src="https://img.shields.io/badge/Status-Alpha-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/Language-Python%203-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/Encryption-Level%20Based-green?style=flat-square"/>
<img src="https://img.shields.io/badge/Multilingual-English%20%7C%20Persian%20%7C%20Digits-purple?style=flat-square"/>
<img src="https://img.shields.io/badge/Color%20Output-Terminal%20Only-red?style=flat-square"/>

</div>

---

## ✨ What is PhalanxCipher?

**PhalanxCipher** is an experimental encryption algorithm designed to protect mixed-language text using layered, reversible obfuscation.

Instead of just rotating letters, it:
- Reverses the entire string
- Applies a mathematical *position × level* jump
- Uses a **bounce-back** system for overflow
- Supports Persian 🇮🇷, English 🇬🇧 and Numbers 🔢
- Is designed for future extensions like GUI, Telegram Bot, or API mode

> 🧪 No cryptographic libraries are used — this is an educational and creative cipher, not a secure cryptographic replacement.

---

## 🔐 How Encryption Works

### For each character:

1. The input text is first **reversed**
2. Each letter's position in its alphabet is multiplied by the **encryption level**
3. A jump is made forward by this amount
4. If the jump exceeds the end of the alphabet:
   - Instead of wrapping to the start (like Caesar),
   - It **bounces backward** from the end (Z → Y → X ...)

#### Example:  
```txt
Original:    Apple
Reversed:    elppA
Level:       2
Encrypt:     ozzxM
