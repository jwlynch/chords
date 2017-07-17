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
            rootless_split = ch_sp.split(":")

            root = ""

            if len(rootless_split) == 1:
                # root is first note in spelling
                spelling = ch_sp.split(",")
                root = spelling[0]
            else:
                # root is to the left of the colon
                root = rootless_split[0]
                spelling = rootless_split[1].split(".")

            out_dict[root + ch_type] = spelling

        return out_dict

# func parse_member_string
#
# takes a string with chord member names, one per line
#
# returns:list of member strings

def parse_member_string(member_str):
    member_list = member_str.split()

    return member_list

class ChordVoicingSet:
    def __init__(self, spell_string, member_string, chord_type):

        # string to append to chord root
        # example: chord root C, chord_type "m7", would become "Cm7"
        self.chord_type = chord_type

        # parse the string in parameter spell_string
        # containing all chord spellings, forming a lookup table
        # of chords of this type, and set object attribute spellings
        # to this lookup table
        self.spellings = parse_spell_string(
            spell_string,
            {},
            chord_type
        )

        # parse the string in the parameter member_string
        # into a list of the chord members (like root, third, fifth)
        # and set object attribute chord_members to this list
        self.chord_members = parse_member_string(member_string)

    def prt(self):
        print("chord suffix: %s" % self.chord_type)

        c_notes = spellings["C" + chord_type]
        chord_str = ""
        chord_list = zip(c_notes, self.chord_members)

        return chord_list
