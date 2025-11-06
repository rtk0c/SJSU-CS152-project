import re

operator_no_space = re.compile(r" ?([()\[\]=~+-/&]|&&|\|\||\*\*?) ?")

def tokens_reduce(src: str) -> str:
  src = re.sub(operator_no_space, r"\1", src)
  return src
