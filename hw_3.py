with open('1.txt', 'rt', encoding='utf-8') as f1,\
        open('2.txt', 'rt', encoding='utf-8') as f2,\
        open('3.txt', 'rt', encoding='utf-8') as f3,\
        open('res.txt', 'w', encoding='utf-8') as res:

    length = {}

    files = [f1, f2, f3]

    for f in files:
        data = f.read()
        lines = data.count('\n') + 1
        length[lines] = [f.name, data]

    sorted_tuple = sorted(length.items(), key=lambda x: x[0])
    length = dict(sorted_tuple)

    for k, v in length.items():
        res.write(str(k) + '\n')
        res.write(str(v[0]) + '\n')
        res.write(v[1] + '\n')
