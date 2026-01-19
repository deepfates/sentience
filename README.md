# Sentience

A procedural generator for sentient objects, built with [Tracery](http://tracery.io/) in 2017.

## What it does

Generates descriptions of self-aware magical items that have names, alignments, purposes, powers, and opinions about their own consciousness.

```
You come upon a chest.
Within, you find a Sassy Wings Of Flying, Lesser!
This Chaotic neutral object calls itself Bereg,
and it hires you to do butt stuff.
By the way, this item can use prying eyes
and just wants a friend
```

## The numbers

**53,805,634,631,400,960** unique sentient objects.

That's 53.8 quadrillion — about 1/8th the number of seconds since the Big Bang.

### Breakdown

| Category | Count | Source |
|----------|-------|--------|
| Objects | 4,064 | Pathfinder/D&D magic items |
| Names | 595 | Tolkien's legendarium |
| Deities | 365 | D&D, Lovecraft, Norse, Egyptian, Greek pantheons |
| Powers | 76 | D&D 3.5e intelligent item abilities + jokes |
| Intelligence descriptors | 34 | "Sentient" to "Self-Driving" to "Vorpal" |
| Purposes | 23 | Violence, religion, mail delivery, chores |
| Missions | 21 | "is sworn to" → "wanna" → "might as well" |
| Creature types | 23 | D&D creature categories |
| Races | 18 | D&D playable races + undead |
| Consciousness claims | 11 | Existential statements |
| Alignments | 9 | The classic 3x3 grid |

The Purpose field contains nested references that expand to 4,142 distinct possibilities when combined with Creatures, Races, Deities, and Names.

## Grammar structure

```
origin
├── Int (intelligence descriptor)
├── Object (the item itself)
├── Alignment (moral/ethical stance)
├── Name (what it calls itself)
├── mission (verb phrase)
├── Purpose (its goal)
│   ├── Creature
│   ├── Race
│   ├── Deity
│   ├── Name
│   └── Addressees → Deity | Name
├── Power (what it can do)
└── conscious (existential status)
```

## Data sources

All data was hand-collected and curated in 2017. Sources include:

- **Objects** (4,064): D&D/Pathfinder SRD magic items
- **Names** (595): Tolkien's legendarium
- **Deities** (365): D&D, Lovecraft's Cthulhu Mythos, Norse, Egyptian, Greek pantheons
- **Powers** (76): D&D 3.5e intelligent item properties + original additions

The grammar structure, missions, consciousness statements, and comedic elements are original.

## Highlights from the data

### Intelligence descriptors include:
Intelligent, Sentient, Self-Driving, Vorpal, Overqualified, Perspicacious, Egghead, Sassy, Smartass

### Missions range from solemn to absurd:
- "is sworn to"
- "took a solemn vow to"
- "wanna"
- "might as well"
- "remembers a past life where a witch told it that you would help it"

### Consciousness statements:
- "is completely self-aware"
- "deserves human rights"
- "may be the only non-human sentient life in the universe"
- "would like you to have a nice day but can't stop talking about how it will die as soon as you 'drop item'"
- "wants to be 'more than friends'"

### Purposes:
- "slay the servants of [Deity]"
- "find the Great White [Creature]"
- "deliver mail to [Name]"
- "do butt stuff"
- "clean its room this weekend"

### Powers end with:
- "this item can 'do butt stuff'"
- "this item sounds nervous"

## Running it

With [uv](https://github.com/astral-sh/uv):

```bash
uv run tracer.py
```

Or with any Python environment:

```bash
pip install tracery
python tracer.py
```

## Why

In 2017 I was exploring procedural generation and hand-curating datasets. The question was: what happens when you give inanimate objects consciousness, personality, and purpose? The answer is comedy through combinatorics — the juxtaposition of serious fantasy elements with absurdist goals creates emergent humor at scale.

Every one of these 53 quadrillion objects is technically unique. Most of them are ridiculous. Some of them might be profound. The generator doesn't know the difference.

## License

The grimoire data is compiled from various SRD (System Reference Document) sources which are released under the Open Game License. The Tracery grammar and original additions are public domain.
