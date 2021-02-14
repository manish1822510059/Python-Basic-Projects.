def encode(string):
    binaries = [f'{ord(x):08b}' for x in string]
    return ''.join(binaries)

name = input()
print(f'--- Welcome {name} ----')
print(f"--- Your name in Binary ---")
print(f'{encode(name)}')