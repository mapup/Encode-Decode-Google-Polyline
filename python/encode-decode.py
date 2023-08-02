import polyline

def encode(coords):
    return polyline.encode(coords, 5)

def decode(encoded):
    return polyline.decode(encoded, 5)

encoded = encode([(37.7749, -122.4194), (34.0522, -118.2437)])
print("Encoded: ", encoded)

decoded = decode(encoded)
print("Decoded: ", decoded)