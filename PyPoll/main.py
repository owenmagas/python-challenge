import csv
from os import path

basepath=path.dirname(__file__)
filepath = path.abspath(path.join(basepath,'Resources/election_data.csv'))
filepath1 = path.abspath(path.join(basepath,'analysis/text_file.txt'))
with open(filepath, 'r') as ed:
    csv_reader = csv.reader(ed)
    next(csv_reader)
    voter_id=set()
    county=[]
    candidate=[]
    for line in csv_reader:
        voter_id.add(line[0])
        county.append(line[1])
        candidate.append(line[2])
    
    
    cand = set(candidate)
    dict={}
    for i in cand:
        dict[i] = candidate.count(i) 
        #print('{}: {}'. format(i, candidate.count(i)))
        # print(dict)
    
    def get_key(val):
        for key, value in dict.items():
            if val== value:
                return key
        return 'key does not exist'
    
    khan = dict['Khan']
    correy = dict['Correy']
    li = dict['Li']
    otooley = dict["O'Tooley"]
    khan_perc = dict['Khan']/len(voter_id)*100
    correy_perc = dict['Correy']/len(voter_id)*100
    li_perc = dict['Li']/len(voter_id)*100
    otooley_perc = dict["O'Tooley"]/len(voter_id)*100
    print("Election Results\n---------------------------------\n"
    "Total Votes: {}\n"
    "Khan: {:.4f}% ({})\n"
    "Correy: {:.4f}% ({})\n"
    "Li: {:.4f}% ({})\n"
    "O'Tooley: {:.4f}% ({})\n"
    "---------------------------------\n"
    "Winner: {}\n"
    "---------------------------------". format(len(voter_id), khan_perc, khan,
    correy_perc, correy, li_perc, li, otooley_perc, otooley,
    get_key(max(dict.values()))))

    with open(filepath1, 'w') as o:
        o.write("Election Results\n---------------------------------\n"
    "Total Votes: {}\n"
    "Khan: {:.4f}% ({})\n"
    "Correy: {:.4f}% ({})\n"
    "Li: {:.4f}% ({})\n"
    "O'Tooley: {:.4f}% ({})\n"
    "---------------------------------\n"
    "Winner: {}\n"
    "---------------------------------". 
    format(len(voter_id), khan_perc, khan,
    correy_perc, correy, li_perc, li, otooley_perc, otooley,
    get_key(max(dict.values()))))
