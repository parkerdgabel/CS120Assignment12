import genome
import phylo


def test_process_infile():
    infile = open("tiny00.fasta")
    assert [("name1", "AAAAAAAAAA"),
            ("name2", "AAAAAAAAAB")] == phylo.process_infile(infile)


class GenomeTest:
    infile = phylo.process_infile(open("tiny00.fasta"))

    def test_genome_constructor(self):
        pass
