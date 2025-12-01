def get_num_words_in_string(input_string):
    return len(input_string.split())

def get_character_frequencies(input_string):
    frequencies = {}
    for c in input_string:
        c = c.lower()
        if c not in frequencies.keys():
            frequencies[c] = 1
        else:
            frequencies[c] += 1
    
    return frequencies

def sort_on(items):
    return items["num"]

def get_sorted_list_of_dicts(input_dict):
    report = []
    for k,v in input_dict.items():
        if k.isalpha():
            report.append({"char": k, "num": v})
    report.sort(reverse=True, key=sort_on)
    return report
