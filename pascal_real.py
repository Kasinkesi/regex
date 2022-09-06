"""
Pascal requires that real constants have either a decimal point, or an exponent (starting with the letter e or E, and
officially called a scale factor), or both, in addition to the usual collection of decimal digits. If a decimal point
is included it must have at least one decimal digit on each side of it. As expected, a sign (+ or -) may precede the
entire number, or the exponent, or both. Exponents may not include fractional digits. Blanks may precede or follow the
real constant, but they may not be embedded within it. Note that the Pascal syntax rules for real constants make no
assumptions about the range of real values, and neither does this problem. Your task in this problem is to identify
legal Pascal real constants.
"""

import re


def pascal_real(text):
    res = []
    dp = "\.\d+"  # dot_pattern
    ep = "[eE][+-]\d+\.?"  # e_pattern
    regex = "[+-]?\d+(?:" + dp + ep + "|(?:" + dp + "|" + ep + r"))\b"
    matchs_with_last_dot = re.findall(regex, text)
    # matchs_with_last_dot = re.findall(r"[+-]?\d+(?:\.\d+[eE][+-]\d+\.?|(?:\.\d+|[eE][+-]\d+\.?))\b", text)
    for match in matchs_with_last_dot:
        if match.endswith('.'):
            continue
        else:
            res.append(match)
    return res


if __name__ == '__main__':
    text = """
    1.2 
      1. 
        1.0e-55  
          e-12   
      6.5E 
            1e-12  
      +4.1234567890E-99999           
      7.6e+12.5 
       99 
    """
    print(pascal_real(text))
