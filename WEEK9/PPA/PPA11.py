def collection_to_file(scores_dataset):
    f = open('scores.csv', 'w')
    f.write('SeqNo,Name,Gender,City,Mathematics,Physics,Chemistry\n')
    for stud in scores_dataset:
        sno = stud['SeqNo']
        name = stud['Name']
        gender = stud['Gender']
        city = stud['City']
        ma = stud['Mathematics']
        phy = stud['Physics']
        chm = stud['Chemistry']
        line = f'{sno},{name},{gender},{city},{ma},{phy},{chm}\n'
        if stud['SeqNo'] == scores_dataset[-1]['SeqNo']:
            line = line.strip()
        f.write(line)
    f.close()