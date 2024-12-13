quip = "VRCOYVRCQTQRZM ORFY CAQYU QZ FRQZ CB COQM URH CB UQMTBFYA MBVY BAUYA QZ COY MYLEYZTY BW XAQVY ZEVSYAM, RZU KY ORFY AYRMBZ CB SYPQYFY CORC QC QM R VHMCYAH QZCB KOQTO COY OEVRZ VQZU KQPP ZYFYA XYZYCARCY."
reverse_map = {"R":"a", "Z":"n","U":"d", "Q":"i", "F":"v", "O":"h"
               , "Y":"e", "C":"t", "A":"r", "B":"o", "X":"p", "V":"m"
               , "M":"s", "T":"c", "H":"y", "L":"q", "E":"u", "W":"f"
               , "S":"b", "K":"w", "P":"l"}
forward_map = {v: k for k, v in reverse_map.items()}

def apply(string, mapping):
    output = ""
    for chr in string:
        print(chr)
        if chr in mapping.keys():
            output += mapping[chr]
        else:
            output += chr
    print(output)
    return output

apply(quip, reverse_map)