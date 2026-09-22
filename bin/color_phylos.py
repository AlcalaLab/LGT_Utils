#!/usr/bin/env python3

import glob, sys
from ete4 import NCBITaxa, Tree

from pathlib import Path


def ncbi_taxonomy(
        taxon_list: list,
        update_ncbi: bool = False) -> dict:

    txnmy_db = {}
    ncbi = NCBITaxa()

    if not Path(f'{Path.home()}/.local/share/ete/taxdump.tar.gz').is_file():
        print('oh-no, missing NCBI taxonomy database!')
        print('preparing NCBI taxonomy database')
        ncbi.update_taxonomy_database()

    for taxon in taxon_list:
        if 'Unid' in taxon:
            continue

        if 'Candidatus' in taxon:
            genus = taxon.split("_")[1]

        else:
            genus = taxon.partition("_")[0].replace("Pseudonitzschia","Pseudo-nitzschia").replace("Pseudo_nitzschia","Pseudo-nitzschia")

        # print(genus)
        clear_taxon = True

        try:
            taxid = list(ncbi.get_name_translator([taxon.replace("_"," ")]).values())[0][0]

        except IndexError:
            try:
                taxid = list(ncbi.get_name_translator([genus]).values())[0][0]

            except IndexError:
                clear_taxon = False
                txnmy_db[taxon] = 'Other'

        if clear_taxon:
            tax_lineage = ncbi.get_lineage(taxid)
            full_lineage_names = ncbi.get_taxid_translator(tax_lineage)
            full_taxonomy = [full_lineage_names[taxid] for taxid in tax_lineage]
            txnmy_db[taxon] = reduce_taxonomy(full_taxonomy, genus)

    return txnmy_db


def reduce_taxonomy(
        full_taxonomy: list,
        taxon_name: str) -> list:

    if 'Bacteria' in full_taxonomy:
        reduced_taxonomy = 'Bacteria'
    elif 'Archaea' in full_taxonomy:
        reduced_taxonomy = 'Archaea'

    elif 'Opisthokonta' in full_taxonomy:
        reduced_taxonomy = 'Opisthokonta'

    elif 'Viridiplantae' in full_taxonomy:
        reduced_taxonomy = 'Chloroplastida'

    elif 'Rhodophyta' in full_taxonomy:
        reduced_taxonomy = 'Rhodophyta'

    elif 'Rhodelphea' in full_taxonomy:
        reduced_taxonomy = 'Rhodophyta'

    elif 'Cryptophyceae' in full_taxonomy:
        reduced_taxonomy = 'Cryptista'

    elif 'Haptophyta' in full_taxonomy:
        reduced_taxonomy = 'Haptophyta'

    elif 'Centroplasthelida' in full_taxonomy:
        reduced_taxonomy = 'Centroplasthelida'

    elif 'Metamonada' in full_taxonomy:
        reduced_taxonomy = 'Metamonada'

    elif 'Discoba' in full_taxonomy:
        reduced_taxonomy = 'Discoba'

    elif 'Amoebozoa' in full_taxonomy:
        reduced_taxonomy = 'Amoebozoa'

    elif 'Glaucocystophyceae' in full_taxonomy:
        reduced_taxonomy = 'Glaucophyta'

    elif 'Sar' in full_taxonomy:
        if 'Alveolata' in full_taxonomy:
            reduced_taxonomy = 'Alveolata'
        elif 'Rhizaria' in full_taxonomy:
            reduced_taxonomy = 'Rhizaria'
        else:
            reduced_taxonomy = 'Stramenopila'

    elif 'Eukaryota' in full_taxonomy:
        reduced_taxonomy = 'Eukaryota'

    else:
        reducted_taxonomy = 'Other'

    return reduced_taxonomy


def get_color_dict(user_select = None):
    clade_color_dict = {
        'Rhodophyta': '#1E6922', 'Chloroplastida': '#02a609dc', 'Glaucophyta': '#37BD70',
        'Opisthokonta':  '#4A0354', 'Amoebozoa': '#8ee5eff2', 'Discoba': '#c20005fe',
        'Metamonada': '#c20064fe', 'Stramenopila': '#002ea2ff', 'Alveolata': '#0050a2ff',
        'Rhizaria': '#0074ebff', 'Haptophyta': '#d58601f9', 'Centroplasthelida': '#feab23ff',
        'Cryptista': '#7701c9ff', 'Bacteria': '#000000', 'Archaea': '#8A8A8A',
        'Eukaryota': '#A37A00', 'Other':'#E012BE'}
    if not user_select:
        return clade_color_dict


def get_clade_color(taxon_name, color_dict):
    return color_dict[list(ncbi_taxonomy([taxon_name]).values())[0]]


def color_nexus_format(tree_file):
    color_tree_out = f'{tree_file.rpartition("/")[-1].rpartition(".")[0]}.NowInColor.nex'

    color_dict = get_color_dict()

    t = Tree(tree_file)

    for node in t.leaves():
            taxon_color = get_clade_color(node.name, color_dict)
            node.name = f'{node.name}[&user_colour="{taxon_color}"]'

    tree_string = f'{t.write().replace("'","").rstrip(";")}:0;'

    out_tree = f'#NEXUS\nBegin Trees;\n Tree tree1={tree_string}\nEnd;'

    with open(color_tree_out,'w+') as w:
        w.write(out_tree)


if __name__ == '__main__':
    try:
        tree_input = sys.argv[1]
    except:
        # print('\nUsage:\n\n    python3 color_phylos.py [PHYLOGENETIC-TREE-FILE/DIR] [COLOR-MAP]\n\n')
        print('\nUsage:\n\n    python3 color_phylos.py [PHYLOGENETIC-TREE-FILE/DIR]\n\n')
        sys.exit(1)

    if Path(tree_input).is_file():
        color_nexus_format(tree_input)

    elif Path(tree_input).is_dir():
        tree_suffixes = ['newick','nwk','treefile']
        tree_files = []
        for suff in tree_suffixes:
            tree_files += glob.glob(f'{tree_input}/*{suff}')

        if not tree_files:
            print('No Newick formatted phylogenies found...')
            sys.exit(1)

        for tree_file in list(set(tree_files)):
            print(tree_file)
            color_nexus_format(tree_file)
