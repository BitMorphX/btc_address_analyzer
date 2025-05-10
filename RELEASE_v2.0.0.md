# RELEASE v2.0.0

## What’s New

This is a full refactor and enhancement of the previous script `base58_decoder_to_hex.py`.

### ✅ Major Improvements
- Added version byte and address type detection (e.g., P2PKH, P2SH, testnet)
- Refined terminal interface using `termcolor`
- Modular, structured function layout
- Clear segmentation of decoded values
- Cleaner UI and better feedback

### 🗑 Deprecated
- `colorama` usage replaced with `termcolor`
- Removed hardcoded formatting in favor of reusable utilities

---

## Migration Notes
This version is not backward-compatible with CLI flags from v1.0.0 (which had none by default). Interactive input remains similar.

---

## Final Note
This version reflects a more mature and extensible analyzer for Bitcoin Base58Check address decoding.
