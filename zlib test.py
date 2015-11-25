import zlib

original_data = 'This is the original text.'
t = zlib.compress(original_data)
print(str(t))