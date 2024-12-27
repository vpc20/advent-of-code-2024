rules = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13'''

seta = set([rule.split('|')[0] for rule in rules.split()])
print(seta)
setb = set([rule.split('|')[1] for rule in rules.split()])
print(setb)
setc = seta.union(setb)
print(setc)

for n in setc:
    print(f"dot.node('{n}')")

#------------------------------------------------------------------------------

for rule in rules.split():
    tail, head = rule.split('|')  # Split the edge definition at ':'
    print(tail, head)  # Add the edge us
