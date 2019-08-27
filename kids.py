running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

# For example, Jay ran like a fool! or Chantelle slid down the slide!

# def hide_and_seek(name):
#     return "{name} hides from the other kids."

# hide_kid = ""

for name in hiding_kids:
    hide_kid = (f"{name} hides from the other kids.")
    print(hide_kid)

# print(hide_kid)
# kid = hide_and_seek(hide_kid)
# print(kid)

for name in running_kids:
    run_kid = (f"{name} runs from the other kids.")
    print(run_kid)

for name in swinging_kids:
    swing_kid = (f"{name} swings from the other kids.")
    print(swing_kid)

for name in sliding_kids:
    slide_kid = (f"{name} slides from the other kids.")
    print(slide_kid)