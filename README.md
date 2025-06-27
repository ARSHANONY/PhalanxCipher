
<div align="center">

<h1>🛡️ PhalanxCipher</h1>
<h3>A military-grade, one-way, multilingual hashing system — handcrafted with precision</h3>

<img src="https://img.shields.io/badge/Language-Python%203.10+-blue.svg?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Encryption-Level%20Based%20Shift-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Hash-Type%20One--Way-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Output-25%20Characters-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Persian%20Support-Full-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Security-Non%20Reversible-black?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Made%20By-Arshan%20Khalili-yellow?style=for-the-badge"/>

</div>

---

> 🔐 **PhalanxCipher** isn’t just a hash function. It’s a philosophy of secure, irreversible, and multilingual encryption.  
> Designed from scratch without relying on existing cryptographic algorithms — PhalanxCipher is your secret weapon for one-way data protection.

---

## 💡 What Makes It Special?

| Feature                       | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 🔁 Reverse-first Obfuscation | Disorients predictable patterns & prevents dictionary attacks               |
| 🔄 Level-based Shifting      | Each character is multiplied by a level × position — personalized per user |
| 🔃 Circular Shift Logic      | Ensures infinite entropy flow; no "wrap-around" failures                    |
| 🧬 Language-aware Design     | Native support for **Farsi**, **English**, and **Digits**                   |
| 🔒 Fixed-length Output       | Exactly 25 characters every time — ideal for tokens and identity hashes     |
| 🧠 Custom Compression Table  | Final step uses a private 48-char mapping table (non-standard)              |
| 🚫 Zero Dependencies         | No libraries, no frameworks, no SHA or MD5 — pure logic                     |

---

## 🔍 How It Works (Behind the Scenes)

1. **Input Reversal** — Every message is flipped to destroy input structure.
2. **Indexed Character Shifting** —  
   - Each character’s index is multiplied by the encryption `level`
   - Circular shifting applies per character set (English: 26, Persian: 32, Digits: 10)
3. **Custom Table Mapping** —  
   - The transformed string + level number is converted to a large number
   - That number is broken into 25 characters using a **non-public** 48-symbol table

🧠 This layered approach ensures:
- High entropy
- Irreversibility
- Language flexibility
- Unique final outputs per user, per text, per level

---

## 🚨 Why It’s Unbreakable (Practically)

| Attack Type          | Result                                                                 |
|----------------------|------------------------------------------------------------------------|
| 🔓 Brute-force       | Requires guessing level + matching custom mapping manually             |
| 🧠 Dictionary attack | Useless — input reversal + custom table ensures mismatch                |
| 🔍 Reverse-engineer  | Not possible without full understanding of shift logic & table encoding |
| 🧪 Hash collisions   | Extremely rare due to personalized shifting                            |
| 🛑 Decryption        | There is no decryption — it’s a **one-way black box**                  |

> ✅ PhalanxCipher is mathematically deterministic but computationally irreversible.  
> That’s the power of custom cryptography.

---

## 🧪 Example Session

```bash
$ python phalanxH.py

🔢 Enter level: 777
📝 Enter text: arshan2025

✅ Final Hash: @9ZJ#U6LMPX0R9&KQWA#9OFAZ
````

* No matter how many times you hash this text with same level → same result
* Change even **1 letter** or **1 level** → completely different 25-character hash

---

## 🧰 Use Cases

* 🔐 Password Hashing (non-reversible storage)
* 🆔 Token/Session ID Generator
* 📁 Database Field Obfuscation
* 📜 Digital Watermarking
* 🧾 Signature for Mixed-Language Documents
* 🛠️ Anywhere you need fast, fixed, irreversible hash

---

## 🔧 Installation

```bash
https://github.com/ARSHANONY/PhalanxCipher.git
cd PhalanxCipher
python phalanxH.py
```

> ✅ Compatible with Python 3.10 and above
> 📦 Requires zero dependencies. No pip install needed.

---

## 📁 File Structure

```
PhalanxCipher/
├── PhalanxH.py       # The main hash function logic
└── README.md            # You are here
```

---

## 📄 License

This project is open-sourced under the **MIT License**.
You are free to use, modify, distribute, or extend — with attribution.

---

## ✍️ Creator

**Arshan Khalili**
🧠 Designer of secure, experimental cryptographic structures

> "Real encryption doesn’t rely on standard formulas. It builds new rules from scratch."

---

## 🌟 Show Your Support

If you find PhalanxCipher useful or inspiring:

* ⭐ Star the repo
* 🍴 Fork for your own use
* 🛠️ Contribute ideas
* 🔐 Add it to your own security projects

---

## 💬 Final Thought

> "In a world flooded with copied ciphers and common crypto,
> PhalanxCipher dares to be different — and that’s what makes it powerful."

```

PhalanxCipher


```
