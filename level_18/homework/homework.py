#2
# or არის ლოგიკური ოპერატორი
#მისი მაგალითებია:
print(False or True)
print(True or True)
print(False or False)
print(False or True)

#3
# and-იც არის ლოგიკური ოპერატორი
#მისი მაგალითებია:
print(False and True)
print(True and True)
print(False and False)
print(False and True)




print((True or False) and (True and True))
#True and True -> True
print((True or False) and (False or False))
#True and false -> false
print((False and True) or (True and False))
#false or false -> false
print((False or False) and (True or True))
#false and True -> false
print((True and True) or (False and True))
#True or false -> True
print((False or True) and (True and False))
#True and false -> false
print((False and False) or (False or True))
#false or True -> True
print((True or False) and (False or True))
#True and True -> True
print((True and False) or (True and False))
#false or false -> false
print((True and True) or (True and False))
#True or false -> True
print((False and False) or (True or bool(5)))
#false or True -> True
print((True or True) and (False and False))
#True and false -> false
print((False or True) and (True or True))
#True and True -> True
print((True and False) or (True and False))
#false or false -> false
#გამარტივების მაგალითი:

print((True or (True and True)) and (False or False))
# (True or True) and False -> True and False -> False

# 7) 1. or
print(False or True)
print(True or True)
print(False or False)
print(False or True)
print(False or True)
print(True or True)
print(False or False)
print(False or True)
print(False or False)
print(False or True)
# 7) 2. and
print(False and True)
print(True and True)
print(False and False)
print(False and True)
print(False and True)
print(True and True)
print(False and False)
print(False and True)
print(False and False)
print(False and True)