def find_anagrams(target, candidates):
    target = target.lower()
    return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted(target) and candidate.lower() != target]