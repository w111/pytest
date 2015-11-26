import zlib
import binascii

original_data = 'This is the original text. бла бла бла' \
                '<script type="meta/js" id="res"><script>' \
                '<script type="meta/py2" id="res"><script>' \
                '<script type="meta/py3" id="res"><script>' \
                '<script type="meta/js" id="res"><script>' \
                '<script type="meta/js" id="res"><script>'
print('Original     :', len(original_data), original_data)

compressed = zlib.compress(original_data.encode('utf-8'))

print('Compressed   :', len(compressed), binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed).decode('utf-8')
print('Decompressed :', len(decompressed), decompressed)