# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  

# for loops = execute a block of code a fixed number of times.
#               You can iterate over a range, string,sequence, etc
#               Basically anything iterable

#example

# for i in (range(1,11,2)):
# Start (inclusive), End (exclusive), Increment/Step
#     print(i)

# print("haPpy nEw yeAr ")


# credit_card = '1234-1234-1234-1234'

# for x in credit_card:
#     print(x)

for x in range(1,21):
    if x == 13:
        continue #skip over but continue
    else:
        print(x)

for x in range(1,21):
    if x == 10:
        break #stops at 10
