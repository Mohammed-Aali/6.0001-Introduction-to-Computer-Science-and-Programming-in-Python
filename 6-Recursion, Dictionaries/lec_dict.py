def leyrics_to_frequencies(lyrics):
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, min_times):
    result = []
    done = False
    while not done:
        tmp = most_common_words(freqs)
        if tmp[1] >= min_times:
            result.append(tmp)
            for w in tmp[0]:
                del(freqs[w])
        else:
            done = True
    return result

# efficient fib
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

