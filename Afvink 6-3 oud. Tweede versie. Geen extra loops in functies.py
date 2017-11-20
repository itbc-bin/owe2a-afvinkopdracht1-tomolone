from tkinter.filedialog import askopenfilename
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
            if (filename.lower())[-5:] == "fasta":
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
            elif filename == '':
                raise FileNotFoundError
            else:
                raise UserWarning
        except FileNotFoundError:
            print("Er is geen bestand gevonden probeer het opnieuw.")
            return False, False
        except UserWarning:
            print("Het geladen bestand is geen .FASTA. Probeer het opnieuw.")
            return False, False
    return headers, seqlist


def is_dna(seq):
    '''
    Kijkt of het bestand DNA is.
    input: sequentie
    output: boolean True of False
    '''
    dna_chars = 'ATCG'
    dna_set = set(seq)
    for c in dna_set:
        if c in dna_chars:
            pass
        else:
            return False
    return True

def knipt(seq, header, enzym):
    '''
    Simpele knipt functie.
    input: sequentie, header, enzymsequentie
    output: header en waar het knipt.
    '''
    if seq.find(enzym) > -1:
        print(header,'\n\nDe sequentie',enzym,'is gevonden op index',seq.find(enzym))
        print("*"*40)
    

def main():
    '''
    Main functie, roept alles aan.
    '''
    try:
        headers, seqlist = openfile()
        if headers == False:
            return
        enzymlijst = []
        with open("enzymen.txt") as enzymen:
            for line in enzymen.readlines():
                enzymlijst.append((line.strip('\n').replace('^', '').upper()).split(' '))
        trefwoord = (input("Welk woord moet er in de header staan?: "))
        if trefwoord == '':
            isditgoed = (input("Er is geen trefwoord opgegeven. Dit betekent dat je alles gaat scannen.\nDoorgaan? (Ja/Nee) ")).lower()
            if isditgoed[:1] != 'j':
                return
        enzym = (input("Geef de exacte naam van het enzym waar je op wilt zoeken: ").upper())
        if enzym == '':
            raise NameError
        print("|"*50)
        tempenz = enzym
        for x in range(len(enzymlijst)):
            if enzym == enzymlijst[x][0]:
                enzym = enzymlijst[x][1]
        if enzym == tempenz:
            raise ValueError
        for x in range(len(seqlist)):
            if trefwoord.lower() in headers[x].lower():
                if is_dna(seqlist[x]) == True:
                    knipt(seqlist[x], headers[x], enzym)
    except NameError:
        print('\nEr is een enzym nodig om te gaan zoeken.\nSript stopt.')
        return
    except ValueError:
        print("\nDit enzym is niet gevonden in de geladen enzymlijst.\nGeef een juist enzym op of voeg hem zelf toe aan 'enzymen.txt'\nScript stopt")
        return
main()





    
