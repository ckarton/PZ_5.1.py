# Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

msg = "--msg-template=$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"
punctuation_chars = string.punctuation
result = "".join([char for char in msg if char in punctuation_chars])

print(result)