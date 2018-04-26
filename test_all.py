import genome
import phylo


def test_process_infile():
    infile = open("tiny00.fasta")
    assert [("name1", "AAAAAAAAAA"),
            ("name2", "AAAAAAAAAB")] == phylo.process_infile(infile)


class testGenome:
    infile = phylo.process_infile(open("tiny00.fasta"))

    def test_genome_constructor(self):
        gene = genome.GenomeData(self.infile[0][0], self.infile[0][1], 2)
        assert gene.id() == "name1"
        assert gene.sequence() == "AAAAAAAAAA"
        assert gene.ngrams() == set(["AA"])

    def test_genome_equality(self):
        gene1 = genome.GenomeData(self.infile[0][0], self.infile[0][1], 2)
        gene2 = genome.GenomeData(self.infile[0][0], self.infile[0][1], 2)
        assert gene1 == gene2
