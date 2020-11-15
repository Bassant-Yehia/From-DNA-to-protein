from Bio.Seq import Seq
from Bio.Seq import transcribe
from Bio.Data import CodonTable
table=CodonTable.unambiguous_dna_by_name["Standard"]
print(table)
DNA_Data=Seq("GGTCAGAAAAAGCCCTCTCCATGTCTACTCACGATACATCCCTGAAAACCACTGAGGAAG")
transcripted_DNA=transcribe(DNA_Data)
print(transcripted_DNA)
translated_Data=transcripted_DNA.translate()
print(translated_Data)
