def reverse_words(sentence):
  result = ""
  n = len(sentence)
  start = n-1
  end = n

  for i in range(n-1, -1, -1):
    if (i >= 0 and sentence[i] == " "):
      start = i+1
      result += sentence[start:end] + " "
      end = i
    if i == 0:
      start = 0
  return result + sentence[start:end]

ans = reverse_words("You are amazing")
print(ans)
