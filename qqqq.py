__author__ = 'iankuoli'

import networkx as nx

yearThreshold = 2000

G = nx.Graph()

with open("/Users/iankuoli/Dataset/BigDND_DBLP/tmp_dblp_coauthorship.json", 'r', encoding='utf-8') as f_graph:
#with open("/Users/iankuoli/Dataset/BigDND_DBLP/sample.txt", 'r', encoding='utf-8') as f_graph:
    for line in f_graph:
        lines = line.strip('\n').replace('\"', '').replace('[', '').replace(']', '').split(', ')

        if len(lines) < 3:
            continue

        author1 = lines[0]
        author2 = lines[1]

        year = 0
        ystr = lines[2].replace(',', '')
        if ystr is None:
            continue
        elif ystr == 'null':
            continue
        else:
            year = int(ystr)

        if year < yearThreshold:
            continue

        if G.has_edge(author1, author2):
            w = G[author1][author2]['weight']
            G[author1][author2]['weight'] = w + 1
        else:
            G.add_edge(author1, author2, weight=1)


G2 = nx.Graph()
for e in G.edges():
    author1 = e[0]
    author2 = e[1]
    w = G[author1][author2]['weight']

    if w >= 2:
        G2.add_edge(author1, author2, weight=w)


dictAuthor2ID = dict()
dictID2Author = dict()
authorID = 1

with open("/Users/iankuoli/Dataset/BigDND_DBLP/graph" + str(yearThreshold) + ".txt", 'w', encoding='utf-8') as f_w:
    for e in G2.edges():
        author1 = e[0]
        author2 = e[1]
        w = G2[author1][author2]['weight']

        if w < 2:
            continue

        if G2.degree(author1) < 2:
            continue

        if G2.degree(author2) < 2:
            continue

        if author1 not in dictAuthor2ID:
            id1 = authorID
            dictAuthor2ID[author1] = id1
            dictID2Author[id1] = author1
            authorID += 1
        else:
            id1 = dictAuthor2ID[author1]

        if author2 not in dictAuthor2ID:
            id2 = authorID
            dictAuthor2ID[author2] = id2
            dictID2Author[id2] = author2
            authorID += 1
        else:
            id2 = dictAuthor2ID[author2]

        f_w.write(str(id1) + '\t' + str(id2) + '\t' + str(w) + '\n')


with open("/Users/iankuoli/Dataset/BigDND_DBLP/author" + str(yearThreshold) + ".txt", 'w', encoding='utf-8') as f_author:
    for i in range(len(dictID2Author)):
        f_author.write(str(i+1) + "\t" + dictID2Author[i+1] + "\n")