maj_roots = ['C','F','Bb','Eb','Ab','Db','F#','B','E','A','D','G']
aug_roots = ['C','F','Bb','Eb','Ab','Db','Gb','Cb','E','A','D','G']

triad_list = []

triad_voicing_list = []

seventh_voicing_list = []

big_four_list = []

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
