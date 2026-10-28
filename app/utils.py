BASE62_ALPHABET="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

BASE=len(BASE62_ALPHABET)

def encode_base62(num:int)->str:
    # Encodes a non-negative integer into a Base62 string

    if num==0:
        return BASE62_ALPHABET[0]

    digits=[]

    while num>0:
        remainder=num%BASE
        digits.append(BASE62_ALPHABET[remainder])
        num//=BASE

    return "".join(reversed(digits))


def decode_base62(key:str)->int:
    # Decodes a Base62 string back into a non-negative integer

    num=0

    for char in key:
        idx=BASE62_ALPHABET.find(char)

        if idx==-1:
            raise ValueError(f"Invalid Base62 character: {char}")
        num=num*BASE+idx
    return num    