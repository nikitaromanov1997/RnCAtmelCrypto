from ecdsa import SigningKey, VerifyingKey, NIST256p

from random import choice
from string import ascii_uppercase

import sys
import jwt
import struct
import array
import binascii
import hashlib
import sha3
import base58

def swap32(x):
    return int.from_bytes(x.to_bytes(4, byteorder='little'), byteorder='big', signed=False)

tag_pubkey = [0xaa,0x8b,0xc7,0x74,0x64,0x6a,0xdf,0x5c,0x9b,0x75,0x36,0x52,0x37,0x9d,0xe8,0x77,0xc7,0x00,0x87,0xeb,0x71,0x1a,0x35,0x15,0x80,0xcc,0x72,0x61,0x73,0x8b,0xb6,0x5a,0xbe,0x33,0xe1,0xe3,0x70,0x19,0x0e,0xe7,0x4f,0xd7,0x94,0x21,0xc8,0xc4,0xf8,0x0f,0x93,0x75,0xce,0x2e,0x68,0x7c,0xc5,0xd1,0x55,0xc4,0x53,0xcb,0x33,0x87,0x6c,0xf7]
sig =        [0x19,0x48,0xd6,0x4c,0x60,0x3e,0x29,0x03,0x5a,0x79,0x26,0xf7,0xb3,0xcd,0x32,0x35,0xae,0xcd,0x1a,0x39,0x81,0x6e,0x74,0x93,0x22,0x87,0x81,0x4e,0xea,0x52,0xfe,0x27,0xe2,0xcc,0x4e,0xc4,0x17,0x1c,0x94,0xc3,0x72,0x87,0x0b,0x8d,0x4f,0xf4,0x33,0x37,0xad,0x12,0xd0,0x1e,0xf7,0xcf,0xd5,0x2c,0x7b,0x43,0x28,0x69,0x57,0x6c,0xad,0x97]
msg  =       [0x98,0x34,0x87,0x6d,0xcf,0xb0,0x5c,0xb1,0x67,0xa5,0xc2,0x49,0x53,0xeb,0xa5,0x8c,0x4a,0xc8,0x9b,0x1a,0xdf,0x57,0xf2,0x8f,0x2f,0x9d,0x09,0xaf,0x10,0x7e,0xe8,0xf0]


prdct_pubkey = binascii.hexlify(bytearray(tag_pubkey))

print(len(bytearray(tag_pubkey)))

print(prdct_pubkey)
prdct_pubkey = hashlib.sha3_256(prdct_pubkey).digest()
prdct_pubkey = base58.b58encode(prdct_pubkey)

print(prdct_pubkey)

vk = VerifyingKey.from_string(bytearray(tag_pubkey), curve=NIST256p)
print(vk.verify_digest(bytearray(sig),bytearray(msg)))
