# Kata: Title Case
# Rank: 6 kyu
# Solved: 2026-05-02
# Source: https://www.codewars.com/kata/title-case
# -----------------------------------------------

def title_case(title, minor_words=''):
    if not title:
        return ""
    
    minor_words_list = [word.lower() for word in minor_words.split()]
    title_words = title.lower().split()
    
    result = [title_words[0].capitalize()]
    
    for word in title_words[1:]:
        if word in minor_words_list:
            result.append(word)
        else:
            result.append(word.capitalize())
            
    return " ".join(result)