def is_possible_encoding(arr, S):
  seen_chars = set()
  char_map = {}

  for char in arr + list(S):
    if char in char_map:
      if char_map[char] != len(seen_chars):
        return False
    else:
      char_map[char] = len(seen_chars)
      seen_chars.add(char)  # Add character to seen set
  return True

# Example usage
arr = ["SEND", "MORE"]
S = "MONEY"

if is_possible_encoding(arr, S):
  print("Yes (Simple Encoding)")
else:
  print("No (Simple Encoding may not be possible)")
