
#Author: Abdul Sabur
#URL: https://www.hackerrank.com/challenges/the-time-in-words
def number_to_words(n):
    words_less_than_twenty = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    
    tens_words = [
        "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    if n == 0:
        return "o' clock"
    
    if n < 20:
        return words_less_than_twenty[n - 1]
    
    tens_digit = n // 10
    ones_digit = n % 10
    if ones_digit == 0:
        return tens_words[tens_digit - 2]
    else:
        return tens_words[tens_digit - 2] + " " + words_less_than_twenty[ones_digit - 1]

def timeInWords(h, m):
    if m == 0:
        return number_to_words(h) + " o' clock"
    elif m == 1:
        return "one minute past " + number_to_words(h)
    elif m == 15:
        return "quarter past " + number_to_words(h)
    elif m == 30:
        return "half past " + number_to_words(h)
    elif m == 45:
        return "quarter to " + number_to_words((h + 1) % 12)
    elif m < 30:
        return number_to_words(m) + " minutes past " + number_to_words(h)
    else:
        return number_to_words(60 - m) + " minutes to " + number_to_words((h + 1) % 12)
