maj_roots = ['C','F','Bb','Eb','Ab','Db','F#','B','E','A','D','G']
aug_roots = ['C','F','Bb','Eb','Ab','Db','Gb','Cb','E','A','D','G']

triad_list = []

triad_voicing_list = []

seventh_voicing_list = []

big_four_list = []

# Chord spellings: is a dict whose keys are chord names,
# and whose values are the lists of notes in those chords.
#
# the possible triad chord types are:
#  "" (e.g., nothing, for example, C, Eb): Major Triad
#  "m" (e.g., Cm, Dbm): Minor Triad
#  "dim" (e.g., Abdim): Diminished Triad
#  "#5" (e.g., G#5): Augmented Triad
#  "sus" (e.g., Fsus): Major Triad with a Suspended Fourth
#
# the possible 7th chord types are:
#  "maj7" (e.g., Cmaj7): Major seventh_list
#  "maj7sus" (e.g., F#maj7sus): Major Seventh Chord with a Suspended Fourth
#  "7" (e.g., Ab7): Dominant Seventh Chord
#  "7sus" (e.g., Bb7sus) Dominant Seventh CHord with a Suspended Fourth
#  "m7" (e.g., Em7): Minor Seventh Chord
#  "m7b5" (e.g., Bm7b5): Minor Seventh Chord with a Flatted Fifth
#  "dim7" (e.g., Adim7): Fully Diminished Seventh Chord

chord_spellings = {}

# func parse_spell_string
# parses spelling string into (chordname, chord spelling) pairs,
# then adds them to output dict with chordname as the key
#  takes:
#   spelling String
#   output dict
#   optionally, chord type string (like m, 7, 7sys, m7)
#  returns: output dict

def parse_spell_string(*args):
    if len(args) < 2:
        print("parse_spell_string: too few args")
        return {}
    elif len(args) > 3:
        print("parse_spell_string: too many args")
        return {}
    else:
        spell_str = args[0]
        out_dict = args[1]

        ch_type = ""
        if len(args) == 3:
            ch_type = args[2]

        spell_list = spell_str.split()
        for ch_sp in spell_list:
            spelling = ch_sp.split(",")
            root = spelling[0]

            out_dict[root + ch_type] = spelling

        return out_dict
