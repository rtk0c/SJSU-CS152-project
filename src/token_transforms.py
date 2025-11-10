import re

def spaces_to_tabs(code_str: str) -> str:
  def replacer(match):
    spaces = match.group(0)
    return "\t" * (len(spaces) // 4)

  return re.sub(r"^( {4})+", replacer, code_str, flags=re.MULTILINE)

operator_no_space = re.compile(r" ?([()\[\]=~+-/&]|&&|\|\||\*\*?) ?")

def tokens_reduce(src: str) -> str:
  src = spaces_to_tabs(src)
  src = re.sub(operator_no_space, r"\1", src)
  return src
