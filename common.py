from random import shuffle

maj_roots = ['C','F','Bb','Eb','Ab','Db','F#','B','E','A','D','G']
aug_roots = ['C','F','Bb','Eb','Ab','Db','Gb','Cb','E','A','D','G']

triad_list = []

triad_voicing_list = []

seventh_voicing_list = []

big_four_list = []

# dict to hold the voicing sets for the various
# chord types, keyed by their chord name suffix
voicing_objects = {}

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
#
# format:
#
# each line is one chord, possibly with enharmonic spellings,
# separated with |.
#
# in each enharmonic spelling, chords that have the root
# among the chord members, simply consist of notes, the first
# of which is the root, and the rest are nonroot chord tones.
#
# chords which are rootless still list the root, only with a
# colon char (:) separating the root from the chird tones.
#
# examples
#
# C triad: C,E,G; C#/Db triad: C#,E#,G#|Db,F,Ab
#
# One possible altered rootless dominant: C:E,Bb,D#
# on Db/C#: C#:E#,B,Dx|Db:F,Cb,E

def parse_spell_string(*args):
    if len(args) < 2:
        print("parse_spell_string: too few args")
        return {}
    elif len(args) > 4:
        print("parse_spell_string: too many args")
        return {}
    else:
        spell_str = args[0]
        out_dict = args[1]

        ch_type = ""
        if len(args) >= 3:
            ch_type = args[2]

        out_rootList = []
        if len(args) >= 4:
            out_rootList = args[3]

        spell_list = spell_str.split()
        for spell_line in spell_list:
            enharmonic_list = spell_line.split("|")

            roots = []

            for ch_sp in enharmonic_list:
                rootless_split = ch_sp.split(":")

                root = ""

                if len(rootless_split) == 1:
                    # root is first note in spelling
                    spelling = ch_sp.split(",")
                    root = spelling[0]
                else:
                    # root is to the left of the colon
                    root = rootless_split[0]
                    spelling = rootless_split[1].split(",")

                out_dict[root + ch_type] = spelling
                roots.append(root)

            if len(roots) > 1:
                out_rootList.append(roots)
            elif len(roots) == 1:
                out_rootList.append(roots[0])

        return out_dict

# func parse_member_string
#
# takes a string with chord member names, one per line
#
# returns:list of member strings

def parse_member_string(member_str):
    member_list = member_str.split()

    return member_list

# takes a list, shuffles it, then pops the front off

def shufflepick(l):
    result = None

    if len(l) > 0:
        shuffle(l)
        result = l.pop()

    return result

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

        # make voicing strings from chord members
        self.voicings = []
        for member in self.chord_members:
            self.voicings.append(member + " on top")

        # holds list of randomly choosable chords

        self.choosable_chords = None

    def choose_chord(self):
        if (
            self.choosable_chords is None
            or
            self.choosable_chords == []
        ):
            self.choosable_chords = self.chordname_list()

        result = shufflepick(self.choosable_chords)

        return result

    def chordname_list(self):
        return list(self.spellings.keys())

    def prt(self):
        print("chord suffix: %s" % self.chord_type)
        print("voicings: %s" % ", ".join(self.voicings))

        c_notes = self.spellings["C" + self.chord_type]
        chord_list = list(zip(c_notes, self.chord_members))
        note_list = []

        for item in chord_list:
            note_list.append("%s (%s)" % item)

        note_str = ", ".join(note_list)

        print("the members are " + note_str)
