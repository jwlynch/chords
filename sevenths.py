
from chords import common
from chords.common import parse_spell_string

chord_spellings = common.chord_spellings

maj_roots = common.maj_roots
big_four_list = common.big_four_list

# Seventh chords

seventh_list = []

maj7s = []
for i in maj_roots:
    maj7s.append(i + "maj7")
seventh_list += maj7s[:]

maj7_spellings = """
C,E,G,B
C#,E#,G#,B#
Db,F,Ab,C
D,F#,A,C#
Eb,G,Bb,D
E,G#,B,D#
F,A,C,E
F#,A#,C#,E#
G,B,D,F#
Ab,C,Eb,G
A,C#,E,G#
Bb,D,F,A
B,D#,F#,A#
"""

parse_spell_string(maj7_spellings, chord_spellings, "maj7")

maj7suss = []
for i in maj_roots:
    maj7suss.append(i + "maj7sus")
    seventh_list += maj7suss[:]

maj7sus_spellings = """
C,F,G,B
C#,F#,G#,B#
Db,Gb,Ab,C
D,G,A,C#
Eb,Ab,Bb,D
E,A,B,D#
F,Bb,C,E
F#,B,C#,E#
G,C,D,F#
Ab,Db,Eb,G
A,D,E,G#
Bb,Eb,F,A
B,E,F#,A#
"""

parse_spell_string(maj7sus_spellings, chord_spellings, "maj7sus")

dom7s = []
for i in maj_roots:
    dom7s.append(i + "7")
    seventh_list += dom7s[:]
big_four_list += dom7s[:]

dom7_spellings = """
C,E,G,Bb
C#,E#,G#,B
Db,F,Ab,Cb
D,F#,A,C
Eb,G,Bb,Db
E,G#,B,D
F,A,C,Eb
F#,A#,C#,E
G,B,D,F
Ab,C,Eb,Gb
A,C#,E,G
Bb,D,F,Ab
B,D#,F#,A
"""

parse_spell_string(dom7_spellings, chord_spellings, "7")

dom7suss = []
for i in maj_roots:
    dom7suss.append(i + "7sus")
seventh_list += dom7suss[:]

dom7sus_spellings = """
C,F,G,Bb
C#,F#,G#,B
Db,Gb,Ab,Cb
D,G,A,C
Eb,Ab,Bb,Db
E,A,B,D
F,Bb,C,Eb
F#,B,C#,E
G,C,D,F
Ab,Db,Eb,Gb
A,D,E,G
Bb,Eb,F,Ab
B,E,F#,A
"""

parse_spell_string(dom7sus_spellings, chord_spellings, "7sus")

min7s = []
for i in maj_roots:
    min7s.append(i + "m7")
seventh_list += min7s[:]
big_four_list += min7s[:]

min7_spellings = """
C,Eb,G,Bb
C#,E,G#,B
Db,Fb,Ab,Cb
D,F,A,C
Eb,Gb,Bb,Db
E,G,B,D
F,Ab,C,Eb
F#,A,C#,E
G,Bb,D,F
Ab,Cb,Eb,Gb
A,C,E,G
Bb,Db,F,Ab
B,D,F#,A
"""

parse_spell_string(min7_spellings, chord_spellings, "m7")

min7b5s = []
for i in maj_roots:
    min7b5s.append(i + "m7b5")
seventh_list += min7b5s[:]

min7b5_spellings = """
C,Eb,Gb,Bb
C#,E,G,B
Db,Fb,Abb,Cb
D,F,Ab,C
Eb,Gb,Bbb,Db
E,G,Bb,D
F,Ab,Cb,Eb
F#,A,C,E
G,Bb,Db,F
Ab,Cb,Ebb,Gb
A,C,Eb,G
Bb,Db,Fb,Ab
B,D,F,A
"""

parse_spell_string(min7b5_spellings, chord_spellings, "m7b5")

dim7s = []
for i in maj_roots:
    dim7s.append(i + "dim7")
seventh_list += dim7s[:]

dim7_spellings = """
C,Eb,Gb,A
C#,E,G,Bb
Db,E,G,Bb
D,F,Ab,B
Eb,Gb,A,C
E,G,Bb,Db
F,Ab,B,D
F#,A,C,Eb
G,Bb,Db,E
Ab,B,D,F
A,C,Eb,Gb
Bb,Db,E,G
B,D,F,Ab
"""

parse_spell_string(dim7_spellings, chord_spellings, "dim7")

# seventh voicings

seventh_voicing_list = common.seventh_voicing_list

voicings = [" root on top", " 3rd on top", " 5th on top", " 7th on top"]
dom7_voicings = []
min7_voicings = []

for root_dex in range(12):
    for voicing in voicings:
        dom7_voicings.append(dom7s[root_dex] + voicing)
        min7_voicings.append(min7s[root_dex] + voicing)

for dom7_voicing in dom7_voicings:
    seventh_voicing_list.append(dom7_voicing)

for min7_voicing in min7_voicings:
    seventh_voicing_list.append(min7_voicing)
