
import genome

def cartesian_product(A, B):
    """Returns the cartesian product of A and B.
    Parameters: A is an iterable.
                B is an iterable
    Returns: A set of tuples such that (x in A, y in B).
    Pre-conditions: A is iterable.
                    B is iterable
    Post-conditions: a set is returned."""
    lst = []
    for x in A:
        for y in B:
            lst.append((x, y))
    return set(lst)

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
    orgs = process_infile(infile)
    orgs = set([genome.GenomeData(x[0], x[1], N) for x in orgs])
