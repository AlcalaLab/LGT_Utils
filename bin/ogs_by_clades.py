#!/usr/bin/env python3

"""
Hasty code to identify gene families that have high representation in two or more
focal clades, to the exclusion of other clades.

This requires a spreadsheet formatted similarly to the one in the repo, as well as
a focal clade and other clades to consider as "acceptable".

This does NOT perform any plotting and is a quick/dirty way to enrich for gene families
present in the selected clades of organisms.

This code also needs to be "pointed" to a folder of peptides, prepared by the
PhyG pipeline too.
"""


import glob, sys

from collections import defaultdict

import pandas as pd

def ogs_from_fasta(fasta_file, delim: str = '_XX_'):
    return [i.rpartition(delim)[-1].rstrip() for i in open(fasta_file).readlines() if i.startswith('>')]


def prep_og_taxon_dict(prot_dir, taxon_list, delim: str = '_XX_'):
    taxon_df = pd.read_csv(taxon_list)

    og_dict = defaultdict(list)

    for f in glob.glob(f'{prot_dir}/*fas*'):
        t = f.rpartition("/")[-1].partition(".")[0]
        if t in taxon_df.Taxon.to_list():
            taxon_ogs = ogs_from_fasta(f, delim)
            for og in taxon_ogs:
                og_dict[og].append(t)

    return og_dict, taxon_df


def get_taxa_by_clade(taxon_df, clade):
    try:
        clade_taxa = taxon_df[(taxon_df == clade).any(axis=1)]['Taxon'].to_list()
        return clade_taxa
    except:
        return None


def check_og_occ_by_clade(og_dict, clade_taxa, min_occ = 0.8):
    ogs_passing = []
    min_taxa = int(len(clade_taxa) * min_occ)
    for k, v in og_dict.items():
        clade_taxa_present = len(set(clade_taxa) & set(v))
        if clade_taxa_present >= min_taxa:
            ogs_passing.append(k)
    return ogs_passing


def assess_by_clades(prot_dir, taxon_list, focal_clades: list, other_clades: list, delim: str = '_XX_', min_occ: float = 0.8, max_non_target = 0.1):
    og_dict, taxon_df = prep_og_taxon_dict(prot_dir, taxon_list, delim)

    focal_clade_ogs = []

    focal_taxa = []

    all_acceptable_taxa = []

    final_ogs = []

    for clade in focal_clades:
        clade_taxa = get_taxa_by_clade(taxon_df, clade)
        focal_taxa += clade_taxa
        all_acceptable_taxa += clade_taxa

        if not clade_taxa:
            print(f'Issue with clade: {clade}')
            break
            # sys.exit()

        focal_clade_ogs += check_og_occ_by_clade(og_dict, clade_taxa, min_occ)

    for clade in other_clades:
        all_acceptable_taxa += get_taxa_by_clade(taxon_df, clade)

    all_acceptable_taxa = list(set(all_acceptable_taxa))

    non_target_prop = []

    for og in list(set(focal_clade_ogs)):
        if focal_clade_ogs.count(og) == len(focal_clades):
            exclusion_thresh = int(len(og_dict[og]) * max_non_target)
            if len([i for i in og_dict[og] if i not in all_acceptable_taxa]) < exclusion_thresh:
                final_ogs.append(og)
            else:
                tmp = len([i for i in og_dict[og] if i not in all_acceptable_taxa]) / len(og_dict[og])
                non_target_prop.append(tmp)
