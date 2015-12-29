__author__ = 'iankuoli'

id2artist = dict()
artist2id = dict()
maxid = 0

with open("/Users/iankuoli/Dataset/LastFm2/artists.dat", 'r', encoding='utf-8') as f_graph:
    for line in f_graph:
        lines = line.strip('\n').split('\t')

        idd = int(lines[0])
        id2artist[idd] = lines[1]
        artist2id[lines[1]] = int(idd)

        if maxid < idd:
            maxid = idd

with open("/Users/iankuoli/Dataset/LastFm2/artists2.txt", 'w', encoding='utf-8') as f_out:
    for i in range(maxid):
        if i in id2artist:
            f_out.write(str(i) + '\t' + id2artist[i] + '\n')