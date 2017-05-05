from chords import common
from chords.common import parse_spell_string

chord_spellings = common.chord_spellings

maj_roots = common.maj_roots
aug_roots = common.aug_roots

# chords for 95 - 98% of pop songs
big_four_list = common.big_four_list

# Triads

triad_list = common.triad_list

maj_triads = common.maj_roots[:]
triad_list += maj_triads[:]
big_four_list += maj_triads[:]

majtriad_spellings = """
C,E,G
C#,E#,G#
Db,F,Ab
D,F#,A
Eb,G,Bb
E,G#,B
F,A,C
F#,A#,C#
G,B,D
Ab,C,Eb
A,C#,E
Bb,D,F
B,D#,F#
"""

parse_spell_string(majtriad_spellings, chord_spellings)

min_triads = []
for i in maj_roots:
    min_triads.append(i + "m")
triad_list += min_triads[:]
big_four_list += min_triads[:]

mintriad_spellings = """
C,Eb,G
C#,E,G#
Db,Fb,Ab
D,F,A
Eb,Gb,Bb
E,G,B
F,Ab,C
F#,A,C#
G,Bb,D
Ab,Cb,Eb
A,C,E
Bb,Db,F
B,D,F#
"""

parse_spell_string(mintriad_spellings, chord_spellings, "m")

dim_triads = []
for i in maj_roots:
    dim_triads.append(i + " dim")
triad_list += dim_triads[:]

dimtriad_spellings = """
C,Eb,Gb
C#,E,G
Db,Fb,Abb
D,F,Ab
Eb,Gb,Bbb
E,G,Bb
F,Ab,Cb
F#,A,C
G,Bb,Db
Ab,Cb,Ebb
A,C,Eb
Bb,Db,Fb
B,D,F
"""

parse_spell_string(dimtriad_spellings, chord_spellings, "dim")

aug_triads = []
for i in aug_roots:
    aug_triads.append(i + " aug")
triad_list += aug_triads[:]

sus_triads = []
for i in maj_roots:
    sus_triads.append(i + " sus")
triad_list += sus_triads[:]

# triad voicings

triad_voicing_list = common.triad_voicing_list

voicings = [" root on top", " 3rd on top", " 5th on top"]
maj_triad_voicings = []
min_triad_voicings = []

for root_dex in range(12):
    for voicing in voicings:
        maj_triad_voicings.append(maj_triads[root_dex] + voicing)
        min_triad_voicings.append(min_triads[root_dex] + voicing)

for maj_triad_voicing in maj_triad_voicings:
    triad_voicing_list.append(maj_triad_voicing)

for min_triad_voicing in min_triad_voicings:
    triad_voicing_list.append(min_triad_voicing)
