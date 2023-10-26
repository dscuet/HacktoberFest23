def biggerIsGreater(w):
    w = list(w)  # Convert the string to a list for easy character manipulation
    i = len(w) - 2

    # Find the first character w[i] such that w[i] < w[i+1]
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"  # The entire string is non-increasing

    # Find the rightmost character w[j] to the right of w[i] such that w[j] > w[i]
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1

    # Swap w[i] and w[j]
    w[i], w[j] = w[j], w[i]

    # Reverse the substring to the right of w[i]
    w[i + 1:] = reversed(w[i + 1:])

    return ''.join(w)

# Read the number of test cases
t = int(input().strip())

for _ in range(t):
    w = input().strip()
    result = biggerIsGreater(w)
    print(result)
