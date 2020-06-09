# Translator
Small CLI translator using [Google translation API](https://cloud.google.com/translate/docs/basic/setup-basic)

As of June 2020, there are 10,000 free API calls per month. More info [here](https://cloud.google.com/translate/pricing).

## Installation
```sh
pip install google-cloud-translate
```
Move your google API private key into `service-account-file.json`.

## Usage
```sh
./translator.py <source_language> <target_language> <string_to_convert>
```

## Exemple
```sh
$ trad en fr Simplicity is prerequisite for reliability. — Edsger Dijkstra
La simplicité est une condition préalable à la fiabilité. - Edsger Dijkstra
```
