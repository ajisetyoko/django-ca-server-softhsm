"""
PoC script to test how [Key Generation, Signing, and Verifiation]
works against softhsmv2 with PKCS11 library
"""

import pkcs11
from pkcs11 import Attribute, ObjectClass
from pkcs11.util.rsa import encode_rsa_public_key
from cryptography.hazmat.primitives import serialization, hashes

# Login
loadlib = pkcs11.lib("/usr/local/lib/softhsm/libsofthsm2.so")
token = loadlib.get_token(token_label="this_is_token_label")
print(token)
with token.open(rw=True, user_pin=str("192837")) as session:
    pass

# Create Key
list_key = []
with token.open(rw=True, user_pin="192837") as session:
    for keys in session.get_objects():
        key = {}
        key["id"] = keys[Attribute.ID].decode()
        list_key.append(key)
print(list_key)

with token.open(rw=True, user_pin="192837") as session:
    pub_key, priv_key = session.generate_keypair(
        pkcs11.KeyType.RSA,
        key_length=2048,
        store=True,
        private_template={
            Attribute.LABEL: "Example_Label_Private",
            Attribute.ID: "Example_Label_Private".encode(),
        },
        public_template={
            Attribute.LABEL: "Example_Label_Public",
            Attribute.ID: "Example_Label_Public".encode(),
        },
    )
    public_key_val = encode_rsa_public_key(pub_key)

# print(public_key_str)
pub_key = serialization.load_der_public_key(public_key_val)
print(pub_key)
publicKeyPem = pub_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
print(publicKeyPem)

list_key = []
with token.open(rw=True, user_pin="192837") as session:
    for keys in session.get_objects():
        key = {}
        key["id"] = keys[Attribute.ID].decode()
        list_key.append(key)
print(list_key)

## Signing Message
message = "This is example message"
with token.open(rw=True, user_pin="192837") as session:
    for priv_key in session.get_objects(
        {
            Attribute.CLASS: ObjectClass.PRIVATE_KEY,
            Attribute.ID: "Example_Label_Private".encode(),
        }
    ):
        priv_key = priv_key

    hash_obj = hashes.Hash(hashes.SHA256())
    hash_obj.update(message.encode())
    hashed_message = hash_obj.finalize()

    signed_data = priv_key.sign(hashed_message).hex()
    print(signed_data)

# Logout
loadlib = pkcs11.lib("/usr/local/lib/softhsm/libsofthsm2.so")
loadlib.reinitialize()
token = loadlib.get_token(token_label="this_is_token_label")

session = token.open(rw=True, user_pin=str("192837"))
session.close()
print(session)
