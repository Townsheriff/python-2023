import lcm

counter = lcm.LetterCounter("this is a text")

print(f'Text {counter.text} repeats letter "t" {counter.count_same_letters("t")} times')
