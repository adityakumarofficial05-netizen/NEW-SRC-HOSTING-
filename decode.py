import base64, zlib, marshal

data = b"YAHAN FULL STRING DAALO"

try:
    decoded = base64.b64decode(data)
    decompressed = zlib.decompress(decoded)
    code = marshal.loads(decompressed)

    print(code)
except Exception as e:
    print("Error:", e)
