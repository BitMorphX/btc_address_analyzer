# 🔍 Bitcoin Address (Base58) Analyzer

**Version:** 2.0.0

---

## 📌 Project Description

This tool is an expanded and improved version of `base58_decoder_to_hex.py`.

While the original script was capable of decoding Base58Check Bitcoin addresses and verifying checksums, this version enhances the experience with:

- Structured terminal output
- Version byte and address type detection
- RIPEMD-160 hash presentation
- Simpler cross-platform coloring via `termcolor`
- Refined, readable CLI

It serves as a hands-on tool for **educational purposes**, helping to understand how Bitcoin Base58Check addresses are structured and validated.

---

## ⚖️ Comparison Table

| Function               | base58_decoder_to_hex.py       | btc_address_analyzer.py         |
|------------------------|--------------------------------|----------------------------------|
| Base58 decoding        | Yes                            | Yes                              |
| Checksum verification  | Yes                            | Yes                              |
| Colored output         | colorama                       | termcolor (simpler)              |
| Address type analysis  | No                             | Yes                              |
| RIPEMD-160 extraction  | Yes                            | Yes                              |
| UI structure           | Basic                          | Clear and segmented              |

---

## 🔧 Features

- Base58Check decoding to HEX
- Address version and type identification
- Payload (hash160) visualization
- SHA-256 x2 checksum validation
- Cross-platform colorized output
- Clean CLI user experience

---

## 🧪 Requirements

- 🐍 Python 3.6+

Install dependencies:

```bash
pip install base58 termcolor
```

---

## 📂 Usage

### Run from terminal:

```bash
python btc_address_analyzer.py
```

Then enter a Bitcoin address (Base58 format) when prompted.

---

## 🧾 Example Output

```
🔍 Bitcoin Address (Base58) Analyzer
────────────────────────────────────

Base58 decoded (hex):      00b3a17...
Version byte:              00
Address type:              P2PKH (mainnet)
Payload (RIPEMD-160):      b3a17...
Checksum (from address):   89ab21cc
Recalculated checksum:     89ab21cc

✔ Checksum is VALID
```

---

## 📜 License

MIT License — see [LICENSE](LICENSE)

---

## ⚠️ Disclaimer

- 🚫 This tool is intended **for educational and research use only**
- ⚠️ Do not use it for live wallet operations or unauthorized purposes
- ❗ The author assumes no liability for misuse or data loss

---

## 🎁 Support

⭐ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

⭐ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

⭐ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

🫐 We also acknowledge early privacy coins like **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

---

🛡️ Licensed under MIT  
“**I morph bits not to break, but to understand.**”  
— BitMorphX
