from tkinter.filedialog import askopenfilename

#Lees_Inhoud. Aangepaste openfile.
def lees_inhoud(amount=1):
    seqlist = []
    headers = []
    for x in range(0, amount):
        seq = askopenfilename()
        with open(seq, "r") as f:
            seq = ''
            header = ''
            for line in f.readlines():
                if '>' in line[:1]:
                    tempheader = line.replace('\n', '')
                    headers.append(tempheader)
                    if seq:
                        seqlist.append(seq)
                        seq = ''
                else:
                    seq = "{}{}".format(seq,line)
            seqlist.append(seq)
    return headers, seqlist

#nieuwe manier van sequenties filteren, nadeel van aangepaste openfile.
def filterseq(seqs):
    seqlist = []
    for x in range(0, len(seqs)):
        seqsingle = seqs[x]
        seqsingle = seqsingle.replace('\n','').replace(' ', '')
        seqlist.append(seqsingle)
        seqsingle = ''
        
    return seqlist

#Kijk of het wel dna/mrna is.
def is_dna(seqlist):
    true = 0
    for x in range(0, len(seqlist)):
        A = seqlist[x].count('A')
        T = seqlist[x].count('T')
        C = seqlist[x].count('C')
        G = seqlist[x].count('G')
        atcglen = A+T+C+G
        if atcglen == len(seqlist[x]):
            true += 1
    if true == len(seqlist):
        return True
    else:
        return False
    
#controleer waar het knipt.
def knipt(seqlist, headers, knip='', naam1='No_name_entered'):
    naam = []
    sequentiedeel = []
    if knip == '':
        with open('enzymen.txt') as f:
            for line in f.readlines():
                restrictie = line.replace('^', '').replace('\n','')
                naam1, sequentiedeel1 = restrictie.split(' ')
                print(naam1, sequentiedeel1)
                naam.append(naam1)
                sequentiedeel.append(sequentiedeel1)
    else:
        sequentiedeel.append(knip)
        naam.append(naam1)
#Fix ff dat die header maar 1x print. 
#Jaja moeie ik, gefikst. 
    for y in range(0, len(seqlist)):
        for x in range(0, len(sequentiedeel)):
            locatie = seqlist[y].find(sequentiedeel[x])
            if locatie >= 0:
                print('-'*80)
                if headers[y] != '':
                    print('|'*80)
                    print(headers[y])
                    print('|'*80)
                    print('')
                headers[y] = ''
                print('Match met',naam[x],'op locatie',locatie)
                print(seqlist[y][locatie-15:locatie+30])
                print(' '*14, sequentiedeel[x])
        #else:
            #print('Geen match gevonden.')

        
#Main functie. Wat debug dingen laten zitten zodat ik ooit nog kan checken
#Hoe ik het heb gedaan.
def main():
    headers, seqlist = lees_inhoud()
    seqlist = filterseq(seqlist)
    #print(headers, seqlist)
    if is_dna(seqlist) == True:
        print('Dit is DNA/mRNA')
    else:
        print('Dit is geen DNA/mRNA, geen garantie dat het script nog werkt.')
    print()
    #resen = input('Welk enzym wil je op controleren? Geef de sequentie: ')
    #seq = seqlist[0]
    #print(seqlist)
    knipt(seqlist, headers, "ATCG", "ATCG_TEST" )
    
main()
