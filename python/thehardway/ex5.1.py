name = 'Chris Z. Panayotov'
age = 35
height = 180 # centimeters
height_inch = height / 2.54 #inches
weight = 70 # kilos
weight_pounds = weight * 2.20462 #pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d inches tall." % height_inch
print "He's %d killos heavy." % weight
print "He's %d pounds heavy." % weight_pounds
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# Simple addition of age, height and weight in kg and cm
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight)
# Simple addition of age, height and weight in pounds and inches
print "If I add %d, %d, and %d I get %d." % (
    age, height_inch, weight_pounds, age + height_inch + weight_pounds)
