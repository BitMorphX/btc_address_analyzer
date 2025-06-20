<p align="center">
  <img src="assets/banner.png" alt="btc_address_analyzer banner" width="100%" />
</p>

# 🔍 BTC ADDRESS ANALYZER

**btc_address_analyzer** is a powerful, educational CLI tool for decoding and analyzing Bitcoin Base58Check addresses, including checksum validation, payload parsing, and address-type detection.

It helps understand how Bitcoin addresses are constructed and verified.

---

## ⚙️ Features

- 🔍 Decodes Base58Check Bitcoin addresses
- 🧩 Extracts and displays version, payload (hash160), and checksum
- 📊 Identifies address type (P2PKH/P2SH, mainnet/testnet)
- ✅ Validates double SHA‑256 checksum
- 🎨 Colorized terminal output with `termcolor`
- 🧪 Ideal for hands-on learning

---

## 🧪 Comparison Table

| Feature                | base58_decoder_to_hex.py | btc_address_analyzer.py     |
|------------------------|---------------------------|-----------------------------|
| Base58 decoding        | ✅ Yes                    | ✅ Yes                      |
| Checksum verification  | ✅ Yes                    | ✅ Yes                      |
| Colored output         | ☑️ colorama               | ✅ termcolor (simpler)      |
| Address type analysis  | ❌ No                     | ✅ Yes                      |
| RIPEMD-160 extraction  | ✅ Yes                    | ✅ Yes                      |
| UI structure           | Basic                    | Structured and readable     |

---

## 📁 File Overview

- `btc_address_analyzer.py` – Main decoding and analysis script  
- `btc_address_analyzer.bat` – Windows launcher for WSL/Ubuntu  
- `.vscode/`  
  - `settings.json` – Editor preferences  
  - `launch.json` – Debug configuration  
  - `tasks.json` – Task runner  
  - `extensions.json` – Recommended extensions  
- `assets/`  
  - `banner.png` – Project banner  
- `README.md` – This documentation  
- `LICENSE` – Apache 2.0 License  
- `NOTICE` – Notices and attribution  
- `ETHICS.md` – Responsible use notice  
- `requirements.txt` – Python dependencies  
- `project.yml` – Project metadata  
- `RELEASE_v1.0.0.md` – First release notes  
- `RELEASE_v2.0.0.md` – Latest release notes

---

## 🛠️ Dependencies

```
base58
termcolor
```

Install with:

```bash
pip install -r requirements.txt
```

> Python 3.8+ is recommended.

---

## 🚀 Usage

### Option 1 – via Python:
```bash
python btc_address_analyzer.py
```

### Option 2 – via `.bat` launcher (for WSL/Ubuntu users on Windows):
```cmd
btc_address_analyzer.bat
```

Then input a Base58-encoded Bitcoin address when prompted.

---

## 📦 Example Output

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

## 📂 Project Structure

```text
btc_address_analyzer/
├── assets/
│   └── banner.png
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   ├── tasks.json
│   └── extensions.json
├── btc_address_analyzer.py
├── btc_address_analyzer.bat
├── LICENSE
├── NOTICE
├── ETHICS.md
├── README.md
├── requirements.txt
├── project.yml
├── RELEASE_v1.0.0.md
└── RELEASE_v2.0.0.md
```

---

## ⚠️ DISCLAIMER

This software is provided strictly for **educational, analytical, and research purposes only**.

The author **does not promote or condone** any unethical behavior, unauthorized access, or abuse of blockchain systems or cryptographic tools.

This project **does not include or generate any real private keys** linked to actual cryptocurrency holdings.  
It is designed to operate in **offline environments** or for simulation/testing purposes.

**The author accepts no liability** for any damages, losses, or illegal use resulting from this software.  
All responsibility lies solely with the end user.

> **Use responsibly. Learn ethically. Contribute honestly.**

---

## ⚖️ Ethical Use

This tool is created strictly for **research and educational purposes**.  
See [`ETHICS.md`](./ETHICS.md) for the full statement.

---

## 📜 License

Licensed under the [Apache 2.0 License](./LICENSE)

---

## 📣 NOTICE

See [`NOTICE`](./NOTICE) for important information about attribution, DMCA protection, and reuse permissions.

---

## 🍱 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

**We also value early privacy coins such as:**  
★ **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

## 👤 Author & Contact

🔗 GitHub: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
