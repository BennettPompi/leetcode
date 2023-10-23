from textEncode import Solution as S


arr = ["The","quick","brown","fox","ju9721982&*@!()mped","over","the","lazy","cat" ]
print(arr)
encoded = S.encode(S, arr)
print(encoded)
decoded = S.decode(S, encoded)
print(decoded)
