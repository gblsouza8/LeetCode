select sample_id, dna_sequence, species, 
if(dna_sequence in(select dna_sequence from samples where regexp_like(dna_sequence, '^ATG')), 1, 0) as has_start,
if(dna_sequence in(select dna_sequence from samples where regexp_like(dna_sequence, '(TAA|TAG|TGA)$')), 1, 0)  as has_stop,
if(dna_sequence in(select dna_sequence from samples where regexp_like(dna_sequence, 'ATAT')), 1, 0)  as has_atat,
if(dna_sequence in(select dna_sequence from samples where regexp_like(dna_sequence, 'GGG')), 1, 0)  as has_ggg
from samples;