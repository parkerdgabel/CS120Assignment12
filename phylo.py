
def process_infile(infile):
    """Processes the infile for the organisms.
    Parameters: infile is an open File.
    Returns: A list of tuples of all organisms in the file.
    Pre-conditions: infile is open
    Post-conditions: A list is returned."""
    orgs = []
    infile = infile.read().split(">")
    infile.pop(0)
    infile = [x.split() for x in infile]
    for org in infile:
        orgs.append((org[0], "".join(org[5:])))
    return orgs

def main():
    infile = input("FASTA file: ")
    N = input("n-gram size: ")
    try:
        infile = open(infile)
        N = int(N)
    except FileNotFoundError:
        print("ERROR: could not open file " + infile)
        exit()
    except ValueError:
        print("ERROR: Bad value for N")
        exit()
    
