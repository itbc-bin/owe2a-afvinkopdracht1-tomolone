from tkinter.filedialog import askopenfilename
'''
Errorhandling todo:
    Eerste regel geen header
'''


def openfile(amount=1):
    '''
    Openfile functie.
    Leest een bestand in en geeft een header- en sequentielijst terug.

    Input: -
    Output: Sequentielijst en Headerlijst.
    Errorhandling: Geen bestand gevonden, bestand is geen .FASTA.
    '''    
    seqlist = []
    headers = []
    seq = ''
    header = ''
    for x in range(0, amount):
        filename = askopenfilename()
        try:
            if filename == '' or (filename.lower())[-5:] != "fasta":
                raise FileNotFoundError
            with open(filename) as file:
                for line in file.readlines():
                    if '>' in line[:1]:
                        tempheader = line.strip('\n')
                        headers.append(tempheader)
                        if seq:
                            seq = seq.strip()
                            seqlist.append(seq)
                            seq = ''
                    else:
                        line = line.strip()
                        seq = "{}{}".format(seq,line)
            seqlist.append(seq)
        except FileNotFoundError:
            print("Er is geen bestand gevonden of het bestand is geen .FA of .FASTA bestand.\nProbeer het opnieuw.")
            return False, False
    return headers, seqlist

def is_dna(seqlist):
    '''
    Kijkt of de sequentielijst vol staat met DNA sequenties.

    Input: Sequentielijst
    Output: Boolean True of False
    '''
    for x in range(len(seqlist)):
        dna_chars = 'ATCG'
        dna_set = set(seqlist[x])
        for c in dna_set:
            if c in dna_chars:
                pass
            else:
                return False
    return True

def knipt(seqlist, headers, zoek):
    '''
    Kijkt waar een ingevoerd zoekwoord matched met de te scannen sequentie.

    input: Sequentielijst, Headerslijst, Zoekwoord
    Output: Als er een match is print deze functie de Header en Matchindex.
    '''
    for x in range(len(seqlist)):
        if seqlist[x].find(zoek) > -1:
            print("*"*40)
            print(headers[x],'\n\nDe sequentie',zoek,'is gevonden op index',seqlist[x].find(zoek))


def main():
    '''
    Main functie, roept alles aan.
    Geeft een waarschuwing en vraagt om input als is_dna False returned.
    '''
    headers, seqlist = openfile()
    if headers == False:
        return
    if is_dna(seqlist) == False:
        doorgaan = input('Een van de gegeven sequenties is mogelijk geen DNA/mRNA.\nToch doorgaan? Ja/Nee: ')
        if (doorgaan.lower())[0] != 'j':
            print("Programma stopt.")
            return
    zoek = (input("Waar wil je op zoeken?: ")).upper()
    if zoek == '':
        print("Geef een sequentie om te zoeken.")
    knipt(seqlist, headers, zoek)
    
main()
