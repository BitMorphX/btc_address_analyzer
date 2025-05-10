#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base58
import hashlib
import os
import platform
from termcolor import colored


def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")


def print_colored(text, color="white"):
    try:
        print(colored(text, color))
    except Exception:
        print(text)


def get_address_type(version_hex: str) -> str:
    version_map = {
        "00": "P2PKH (mainnet)",
        "05": "P2SH (mainnet)",
        "6f": "P2PKH (testnet)",
        "c4": "P2SH (testnet)"
    }
    return version_map.get(version_hex.lower(), "Unknown or non-standard")


def decode_base58_address(address: str):
    try:
        decoded = base58.b58decode(address)
        hex_full = decoded.hex()
        version = decoded[0:1].hex()
        payload = decoded[1:-4].hex()
        checksum = decoded[-4:].hex()

        calculated_checksum = hashlib.sha256(
            hashlib.sha256(decoded[:-4]).digest()
        ).digest()[:4].hex()

        print_colored("\nBase58 decoded (hex):      " + hex_full, "white")
        print_colored(f"Version byte:              {version}", "yellow")
        print_colored(f"Address type:              {get_address_type(version)}", "white")
        print_colored(f"Payload (RIPEMD-160):      {payload}", "white")
        print_colored(f"Checksum (from address):   {checksum}", "cyan")
        print_colored(f"Recalculated checksum:     {calculated_checksum}", "cyan")

        if checksum == calculated_checksum:
            print_colored("\n✔ Checksum is VALID", "green")
        else:
            print_colored("\n✘ Checksum is INVALID", "red")

    except Exception as e:
        print_colored(f"Error: {e}", "red")


def main():
    clear_screen()
    print_colored("🔍 Bitcoin Address (Base58) Analyzer", "cyan")
    print_colored("────────────────────────────────────", "cyan")
    address = input("Enter Bitcoin address (Base58): ").strip()
    decode_base58_address(address)


if __name__ == "__main__":
    main()
