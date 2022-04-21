# BEGIN
def sort_pair(pair):
    (first, second) = pair
    if first > second:
        return (second, first)
    return pair
# END