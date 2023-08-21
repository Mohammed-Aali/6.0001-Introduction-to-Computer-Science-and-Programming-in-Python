def get_data(a_tuple):
    nums = ()
    words = ()
    for t in a_tuple:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

# applying to data
tsweft = ((2014, 'Katy'),
          (2014, 'Harry'),
          (2012, 'Jake'),
          (2010, 'Taylor'),
          (2008, 'Joe'))

(min_year, max_year, num_people) = get_data(tsweft)
print('From', min_year,'to', max_year, 'Taylor Swift wrote songs about', num_people, 'people')