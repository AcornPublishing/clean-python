from collections import Counter

contries  = ["Belarus", "Albania", "Malta", "Ukrain", "Belarus", "Malta", "Kosove", "Belarus"]
contries_count = Counter(contries)
"""
>>> Counter({'Belarus': 3, 'Malta': 2, 'Albania': 1, 'Ukrain': 1, 'Kosove': 1})
"""
contries_count.most_common(1)
"""
>>> [('Belarus', 3)]
"""
