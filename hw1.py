import random

def aa(s):
    return s[::-1]

def bb(s):
    return s[0::2]

def cc(s1, s2):
    return ''.join(a + b for a, b in zip(s1, s2))

def dd(sentence):
    words = sentence.split()
    return [len(word.strip(',.')) for word in words]

def ee(sentence):
    words = sentence.split()
    indices = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    return {words[i-1][:1] if i in indices else words[i-1][:2]: i for i in range(1, len(words)+1)}

def ff(seq, n):
    return [seq[i:i+n] for i in range(len(seq)-n+1)]

def gg():
    X = set(ff("paraparaparadise", 2))
    Y = set(ff("paragraph", 2))
    return X | Y, X & Y, X - Y, "se" in X, "se" in Y

def hh(x, y, z):
    return f"{y} is {z} at {x}"

def cipher(text):
  result = ''
  for char in text:
    if 'a' <= char <= 'z':
      result += chr(219 - ord(char))
    else:
      result += char
  return result

def jj(sentence):
    def kk(word):
        if len(word) <= 4:
            return word
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    return ' '.join(kk(word) for word in sentence.split())

print(aa("stressed"))
print(bb("schooled"))
print(cc("shoe", "cold"))
print(dd("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
print(ee("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."))
print(gg())
print(hh(12, "temperature", 22.4))
print(cipher("Hello, World!"))
print(cipher(cipher("Hello, World!"))) 
print(jj("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind."))
