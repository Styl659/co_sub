mapping = {'zero': 0, 'ra': 1,  'sp': 2,   'gp': 3, 'tp': 4,   't0': 5,  't1': 6,   't2': 7,
    's0': 8,   's1': 9,  'a0': 10,  'a1': 11, 'a2': 12,  'a3': 13, 'a4': 14,  'a5': 15,
    'a6': 16,  'a7': 17, 's2': 18,  's3': 19, 's4': 20,  's5': 21, 's6': 22,  's7': 23,
    's8': 24,  's9': 25, 's10': 26, 's11': 27, 't3': 28,  't4': 29, 't5': 30,  't6': 31,}

def rs(value):
    global mapping
    init=value.find('(')
    fin=value.find(')')
    if init != -1 and fin != -1:
        if fin > init:
            return mapping.get(value[init+1:fin])
    return mapping.get(value)

def type_s(inst,rs2,rs1):
    if inst.upper() == 'SW':
        imm11_5='1111111'
        fun3='010'
        imm4_0='11010'
    elif inst.upper() == 'SH':
        imm11_5='0000000'
        fun3='001'
        imm4_0='10111'

    elif inst.upper() == 'SB':
        imm11_5='0000001'  
        fun3='000'
        imm4_0='01101'
    op='0100011'

    if rs2.upper().startswith("X") and rs2[1:].isdigit():
        rs2=format(int(rs2[1:]), '05b')
    else:
        rs2=format(rs(rs2), '05b')

    if rs1.upper().startswith("X") and rs1[1:].isdigit():
        rs1=format(int(rs1[1:]), '05b')
    else:
        rs1=format(rs(rs1), '05b')

    return imm11_5+rs2+rs1+fun3+imm4_0+op

inst,rs2,rs1=' '.join(input().replace(',', ' ').split()).split()
decimal=int(type_s(inst, rs2, rs1), 2)
print(type_s(inst, rs2, rs1))
print(hex(decimal)[2:])

#Example input -> sw t2 -6(s3)
# or  sw x7 -6(x19)