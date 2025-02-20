mapping = {'zero': 0, 'ra': 1,  'sp': 2,   'gp': 3, 'tp': 4,   't0': 5,  't1': 6,   't2': 7,
    's0': 8,   's1': 9,  'a0': 10,  'a1': 11, 'a2': 12,  'a3': 13, 'a4': 14,  'a5': 15,
    'a6': 16,  'a7': 17, 's2': 18,  's3': 19, 's4': 20,  's5': 21, 's6': 22,  's7': 23,
    's8': 24,  's9': 25, 's10': 26, 's11': 27, 't3': 28,  't4': 29, 't5': 30,  't6': 31,}

def type_j(inst,rd,imm):
    if inst.upper() == 'JAL':
        immbin=format(int(imm, 0), '020b')
    op='1101111'

    if rd.upper().startswith("X") and rd[1:].isdigit():
        rd=format(int(rd[1:]), '05b')
    else:
        rd=format(mapping.get(rd), '05b')

    return immbin+rd+op

inst,rd,imm=' '.join(input().replace(',', ' ').split()).split()
decimal=int(type_j(inst, rd, imm), 2)
print(type_j(inst, rd, imm))
print(hex(decimal)[2:])

#Example input -> jal ra, 0xA67F8
# or  jal x1,0xA67F8