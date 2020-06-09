#!/usr/bin/env python3
"""Translates text from source language into the target language.

Source and target must be language codes.
"""
from google.cloud import translate_v2
from google.oauth2 import service_account
import sys

ACCOUNT_FILE = "service-account-file.json"


def translate(source: str, target: str, text: str) -> None:
    """Main function."""
    cred = service_account.Credentials.from_service_account_file(ACCOUNT_FILE)
    translate_client = translate_v2.Client(credentials=cred)
    result = translate_client.translate(text, target, source_language=source)

    if "translatedText" not in result:
        print(result)
        return

    print(result["translatedText"])


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <source_language> <target_language> <string_to_convert>")
        exit()

    translate(sys.argv[1], sys.argv[2], " ".join(sys.argv[3:]))
