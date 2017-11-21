import tracery
from tracery.modifiers import base_english
import json

# use json.loads() and open() to read in a JSON file as a Python data structure
rules = json.loads(open("grimoire.json").read())

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

# print ten random outputs
for i in range(1):
    print(grammar.flatten("#origin#"))
