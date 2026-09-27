#!/usr/bin/env python3

import sys
import pandas as pd
def etol_385_groups():
    db = {
        'opisthokonta': ['Monosiga_brevicollis', 'Salpingoeca_rosetta', 'Drosophila_melanogaster',
            'Homo_sapiens', 'Nematostella_vectensis', 'Trichoplax_adhaerens', 'Capsaspora_owczarzaki',
            'Batrachochytrium_dendrobatidis', 'Saccharomyces_cerevisiae', 'Fonticula_alba'],
        'amoebozoa': ['Acytostelium_subglobosum', 'Dictyostelium_discoideum', 'Vermamoeba_vermiformis',
            'Acanthamoeba_castellanii', 'Stereomyxa_ramosa'],
        'haptophyta': ['Chrysochromulina_tobin', 'Prymnesium_parvum', 'Emiliania_huxleyi',
            'Pavlova_lutheri', 'Pavlova_sp'],
        'centroheliozoa': ['Acanthocystis_sp', 'Raineriophrys_erinaceoides', 'Raphidiophrys_heterophryoidea'],
        'alveolata': ['Plasmodium_falciparum', 'Toxoplasma_gondii', 'Vitrella_brassicaformis',
            'Breviolum_minutum', 'Perkinsus_marinus', 'Oxytricha_trifallax', 'Tetrahymena_thermophila'],
        'stramenopila': ['Aureococcus_anophagefferens', 'Ectocarpus_siliculosus', 'Phaeomonas_parva',
            'Fragilariopsis_cylindrus', 'Pseudonitzschia_australis', 'Phaeodactylum_tricornutum',
            'Thalassiosira_pseudonana', 'Nannochloropsis_gaditana', 'Aplanochytrium_kerguelense',
            'Hondaea_fermentalgiana', 'Blastocystis_hominis', 'Cafeteria_roebergensis',
            'Halocafeteria_seosinensis'],
        'rhizaria': ['Bigelowiella_natans', 'Plasmodiophora_brassicae', 'Reticulomyxa_filosa'],
        'cryptista': ['Chroomonas_mesostigmatica', 'Geminigera_cryophila', 'Guillardia_theta',
            'Goniomonas_avonlea', 'Roombia_truncata', 'Palpitomonas_bilix'],
        'rhodophyta': ['Gracilariopsis_chorda', 'Chondrus_crispus', 'Porphyridium_purpureum',
        'Galdieria_sulphuraria', 'Cyanidioschyzon_merolae'],
        'rhodelphis': ['Rhodelphis_limneticus', 'Rhodelphis_marinus'],
        'glaucophyta': ['Cyanophora_paradoxa','Cyanoptyche_gloeocystis'],
        'chlorophyta': ['Arabidopsis_thaliana', 'Populus_trichocarpa', 'Physcomitrella_patens',
            'Mesostigma_viride', 'Botryococcus_braunii', 'Coccomyxa_subellipsoidea',
            'Symbiochloris_reticulata', 'Chlorella_variabilis', 'Helicosporidium_sp',
            'Chlamydomonas_reinhardtii', 'Gonium_pectorale', 'Volvox_carteri', 'Dunaliella_salina',
            'Chromochloris_zofingiensis', 'Bathycoccus_prasinos', 'Ostreococcus_tauri',
            'Micromonas_pusilla', 'Cymbomonas_tetramitiformis'],
        'hemimastigophora': ['Hemimastix_kukwesjijk', 'Spironema_cf_multiciliatum'],
        'provora': ['Nibbleromonas_arcticus', 'Nibbleromonas_curacaus', 'Nibbleromonas_quarantinus',
            'Nibbleromonas_kosolapovi', 'Ubysseya_fretuma'],
        'discoba': ['Bodo_saltans', 'Trypanosoma_brucei', 'Eutreptiella_gymnastica',
            'Euglena_longa', 'Naegleria_gruberi', 'Percolomonas_cosmopolitus',
            'Pharyngomonas_kirbyi', 'Andalucia_godoyi', 'Ophirina_amphinema'],
        'metamonada_no_anaeramoeba': ['Chilomastix_cuspidata', 'Dysnectes_brevis',
            'Giardia_lamblia', 'Carpediemonas_membranifera', 'Trichomonas_vaginalis',
            'Monocercomonoides_sp'],
        'metamonada_with_anaeramoeba': ['Chilomastix_cuspidata', 'Dysnectes_brevis',
            'Giardia_lamblia', 'Carpediemonas_membranifera', 'Trichomonas_vaginalis',
            'Monocercomonoides_sp', 'Anaeramoeba_flamelloides', 'Anaeramoeba_ignava'],
        'telonema': ['Telonema_sp', 'Telonema_subtile'],
        'picozoa': ['Picozoa_COSAG01', 'Picozoa_COSAG02', 'Picozoa_COSAG06'],
        'malawimonada': ['Gefionella_okellyi', 'Imasa_heleensis'],
        'ancyromonada': ['Ancyromonas_sp', 'Ancyromonas_sigmoides'],
        'crums': ['Diphylleia_rotans', 'Rigifila_ramosa', 'Mantamonas_sp', 'Mantamonas_plastica']
    }
    #Archaeplastida related hypotheses
    #Archaeplastida related hypotheses
    db['archaeplastida'] = db['chlorophyta'] + db['rhodophyta'] + db['glaucophyta'] + db['rhodelphis']
    db['archaeplastida_cryptista'] = db['archaeplastida'] + db['cryptista']
    db['archaeplastida_picozoa'] = db['archaeplastida'] + db['picozoa']
    db['glaucophyta_rhodophyta'] = db['rhodophyta'] + db['glaucophyta']
    db['glaucophyta_rhodophyta_rhodelphis'] = db['glaucophyta_rhodophyta'] + db['rhodelphis']
    db['chlorophyta_rhodophyta'] = db['chlorophyta']+db['rhodophyta']
    db['chlorophyta_rhodophyta_rhodelphis'] = db['chlorophyta_rhodophyta'] + db['rhodelphis']
    db['chlorophyta_glaucophyta'] = db['chlorophyta'] + db['glaucophyta']
    db['chlorophyta_glaucophyta_cryptista'] = db['chlorophyta'] + db['glaucophyta'] + db['cryptista']
    db['rhodophyta_rhodelphis'] = db['rhodophyta'] + db['rhodelphis']
    db['rhodophyta_picozoa'] = db['rhodophyta'] + db['picozoa']
    db['rhodophyta_rhodelphis_picozoa'] = db['rhodophyta'] + db['rhodelphis'] + db['picozoa']
    # Haptista_related
    db['haptista'] = db['haptophyta'] + db['centroheliozoa']
    db['haptophyta_telonema'] = db['haptophyta'] + db['telonema']
    db['haptophyta_picozoa'] = db['haptophyta'] + db['picozoa']
    db['haptophyta_telonema_picozoa'] = db['haptophyta_telonema'] + db['picozoa']
    db['centroheliozoa_telonema'] = db['centroheliozoa'] + db['telonema']
    db['centroheliozoa_picozoa'] = db['centroheliozoa'] + db['picozoa']
    db['centroheliozoa_telonema_picozoa'] = db['centroheliozoa_telonema'] + db['picozoa']
    db['haptista_picozoa_telonema'] = db['haptophyta'] + db['centroheliozoa'] + db['telonema'] + db['picozoa']
    # SAR related hypotheses
    db['sar'] = db['alveolata'] + db['stramenopila'] + db['rhizaria']
    db['tsar'] = db['sar'] + db['telonema']
    db['telonema_picozoa_sar'] = db['tsar'] + db['picozoa']
    # SAR + Haptista
    db['sar_haptista'] = db['sar'] + db['haptista']
    db['tsar_haptista'] = db['tsar'] + db['haptista']
    db['telonema_picozoa_sar_haptista'] = db['tsar_haptista'] + db['picozoa']
    # Picozoa+Telonema
    db['picozoa_telonema'] = db['telonema'] + db['picozoa']
    # Excavata related hypotheses
    db['excavata_anaeramoeba_malawimonada'] = db['discoba'] + db['malawimonada'] + db['metamonada_with_anaeramoeba']
    db['excavata_malawimonada'] = db['discoba'] + db['malawimonada'] + db['metamonada_no_anaeramoeba']
    db['excavata_anaeramoeba'] = db['discoba'] + db['metamonada_with_anaeramoeba']
    db['excavata'] = db['discoba'] + db['metamonada_no_anaeramoeba']
    db['metamonada_malawimonada'] = db['metamonada_no_anaeramoeba'] + db['malawimonada']
    db['metamonada_ancyromonada'] = db['metamonada_no_anaeramoeba'] + db['ancyromonada']
    db['metamonada_anaeramoeba_malawimonada'] = db['metamonada_with_anaeramoeba'] + db['malawimonada']
    db['metamonada_anaeramoeba_ancyromonada'] = db['metamonada_with_anaeramoeba'] + db['ancyromonada']
    db['metamonada_malawimonada_ancyromonada'] = db['metamonada_no_anaeramoeba'] + db['malawimonada'] + db['ancyromonada']
    db['metamonada_anaeramoeba_malawimonada_ancyromonada'] = db['metamonada_with_anaeramoeba'] + db['malawimonada'] + db['ancyromonada']
    db['malawimonada_ancyromonada'] = db['malawimonada'] + db['ancyromonada']
    # SAR + Excavata
    db['sar_excavata_anaeramoeba'] = db['sar'] + db['excavata_anaeramoeba']
    db['sar_excavata'] = db['sar'] + db['excavata']
    db['tsar_excavata_anaeramoeba'] = db['tsar'] + db['excavata_anaeramoeba']
    db['tsar_excavata'] = db['tsar'] + db['excavata']
    db['telonema_picozoa_sar_excavata_anaeramoeba'] = db['telonema_picozoa_sar'] + db['excavata_anaeramoeba']
    db['telonema_picozoa_sar_excavata'] = db['telonema_picozoa_sar'] + db['excavata']
    # Amoebozoa related hypotheses
    db['amoebozoa_anaeramoeba'] = db['amoebozoa'] + ['Anaeramoeba_flamelloides', 'Anaeramoeba_ignava']
    db['diaphoretickes'] = db['archaeplastida'] + db['cryptista'] + db['sar'] + db['provora'] + db['haptista'] + db['picozoa_telonema']
    db['obazoa'] = db['opisthokonta'] + ['Thecamonas_trahens', 'Pygsuia_biforma']
    return db

def etol_317_groups():
    db = {
        'opisthokonta': ['Batrachochytrium_dendrobatidis', 'Saccharomyces_cerevisiae',
            'Fonticula_alba', 'Salpingoeca_rosetta', 'Monosiga_brevicollis', 'Homo_sapiens',
            'Drosophila_melanogaster', 'Nematostella_vectensis', 'Trichoplax_adhaerens',
            'Capsaspora_owczarzaki'],
        'amoebozoa': ['Acytostelium_subglobosum', 'Dictyostelium_discoideum', 'Vermamoeba_vermiformis',
            'Acanthamoeba_castellanii', 'Stereomyxa_ramosa'],
        'haptophyta': ['Emiliania_huxleyi', 'Prymnesium_parvum', 'Chrysochromulina_tobin',
            'Pavlova_lutheri', 'Pavlovales_sp'],
        'centroheliozoa': ['Acanthocystis_sp', 'Raineriophrys_erinaceoides', 'Raphidiophrys_heterophryoidea'],
        'alveolata': ['Vitrella_brassicaformis', 'Chromera_velia', 'Plasmodium_falciparum',
            'Perkinsus_marinus', 'Breviolum_minutum', 'Tetrahymena_thermophila', 'Oxytricha_trifallax'],
        'stramenopila': ['Bicosoecid_sp', 'Cafeteria_roebergensis', 'Hondaea_fermentalgiana',
            'Aplanochytrium_kerguelense', 'Thalassiosira_pseudonana', 'Phaeodactylum_tricornutum',
            'Fragilariopsis_cylindrus', 'Pseudo_nitzschia_multiseries', 'Ectocarpus_siliculosus',
            'Nannochloropsis_gaditana', 'Aureococcus_anophagefferens', 'Phaeomonas_parva',
            'Blastocystis_hominis'],
        'rhizaria': ['Bigelowiella_natans', 'Plasmodiophora_brassicae', 'Reticulomyxa_filosa'],
        'cryptista': ['Goniomonas_avonlea', 'Geminigera_cryophila', 'Guillardia_theta',
            'Chroomonas_mesostigmatica', 'Roombia_truncata', 'Palpitomonas_bilix'],
        'rhodophyta': ['Gracilariopsis_chorda', 'Chondrus_crispus', 'Porphyridium_purpureum',
        'Galdieria_sulphuraria', 'Cyanidioschyzon_merolae'],
        'rhodelphis': ['Rhodelphis_limneticus', 'Rhodelphis_marinus'],
        'glaucophyta': ['Cyanophora_paradoxa','Cyanoptyche_gloeocystis'],
        'chlorophyta': ['Dunaliella_salina', 'Volvox_carteri', 'Gonium_pectorale',
            'Chlamydomonas_reinhardtii', 'Chromochloris_zofingiensis', 'Botryococcus_braunii',
            'Symbiochloris_reticulata', 'Coccomyxa_subellipsoidea', 'Chlorella_sorokiniana',
            'Helicosporidium_sp', 'Cymbomonas_tetramitiformis', 'Bathycoccus_prasinos',
            'Ostreococcus_tauri', 'Micromonas_pusilla', 'Physcomitrium_patens',
            'Arabidopsis_thaliana', 'Populus_trichocarpa', 'Mesostigma_viride'],
        'hemimastigophora': ['Hemimastix_kukwesjijk', 'Spironema_cf_multiciliatum'],
        'provora': ['Nibbleromonas_arcticus', 'Nibbleromonas_curacaus', 'Nibbleromonas_quarantinus',
            'Nibbleromonas_kosolapovi', 'Ubysseya_fretuma'],
        'discoba': ['Bodo_saltans', 'Trypanosoma_brucei', 'Eutreptiella_gymnastica',
            'Euglena_gracilis', 'Pharyngomonas_kirbyi', 'Percolomonas_cosmopolitus',
            'Naegleria_gruberi', 'Andalucia_godoyi', 'Ophirina_amphinema'],
        'metamonada_no_anaeramoeba': ['Dysnectes_brevis', 'Giardia_lamblia',
            'Chilomastix_cuspidata', 'Carpediemonas_membranifera', 'Trichomonas_vaginalis',
            'Monocercomonoides_sp'],
        'metamonada_with_anaeramoeba': ['Anaeramoeba_ignava', 'Anaeramoeba_flamelloides',
            'Dysnectes_brevis', 'Giardia_lamblia', 'Chilomastix_cuspidata',
            'Carpediemonas_membranifera', 'Trichomonas_vaginalis', 'Monocercomonoides_sp'],
        'telonema': ['Telonema_sp', 'Telonema_subtile'],
        'picozoa': ['Picozoa_COSAG01', 'Picozoa_COSAG02', 'Picozoa_COSAG06'],
        'malawimonada': ['Gefionella_okellyi', 'Imasa_heleensis'],
        'ancyromonada': ['Ancyromonas_sp', 'Ancyromonas_sigmoides'],
        'crums': ['Diphylleia_rotans', 'Rigifila_ramosa', 'Mantamonas_sp', 'Mantamonas_plastica']
    }
    #Archaeplastida related hypotheses
    db['archaeplastida'] = db['chlorophyta'] + db['rhodophyta'] + db['glaucophyta'] + db['rhodelphis']
    db['archaeplastida_cryptista'] = db['archaeplastida'] + db['cryptista']
    db['archaeplastida_picozoa'] = db['archaeplastida'] + db['picozoa']
    db['glaucophyta_rhodophyta'] = db['rhodophyta'] + db['glaucophyta']
    db['glaucophyta_rhodophyta_rhodelphis'] = db['glaucophyta_rhodophyta'] + db['rhodelphis']
    db['chlorophyta_rhodophyta'] = db['chlorophyta']+db['rhodophyta']
    db['chlorophyta_rhodophyta_rhodelphis'] = db['chlorophyta_rhodophyta'] + db['rhodelphis']
    db['chlorophyta_glaucophyta'] = db['chlorophyta'] + db['glaucophyta']
    db['chlorophyta_glaucophyta_cryptista'] = db['chlorophyta'] + db['glaucophyta'] + db['cryptista']
    db['rhodophyta_rhodelphis'] = db['rhodophyta'] + db['rhodelphis']
    db['rhodophyta_picozoa'] = db['rhodophyta'] + db['picozoa']
    db['rhodophyta_rhodelphis_picozoa'] = db['rhodophyta'] + db['rhodelphis'] + db['picozoa']
    # Haptista_related
    db['haptista'] = db['haptophyta'] + db['centroheliozoa']
    db['haptophyta_telonema'] = db['haptophyta'] + db['telonema']
    db['haptophyta_picozoa'] = db['haptophyta'] + db['picozoa']
    db['haptophyta_telonema_picozoa'] = db['haptophyta_telonema'] + db['picozoa']
    db['centroheliozoa_telonema'] = db['centroheliozoa'] + db['telonema']
    db['centroheliozoa_picozoa'] = db['centroheliozoa'] + db['picozoa']
    db['centroheliozoa_telonema_picozoa'] = db['centroheliozoa_telonema'] + db['picozoa']
    db['haptista_picozoa_telonema'] = db['haptophyta'] + db['centroheliozoa'] + db['telonema'] + db['picozoa']
    # SAR related hypotheses
    db['sar'] = db['alveolata'] + db['stramenopila'] + db['rhizaria']
    db['tsar'] = db['sar'] + db['telonema']
    db['telonema_picozoa_sar'] = db['tsar'] + db['picozoa']
    # SAR + Haptista
    db['sar_haptista'] = db['sar'] + db['haptista']
    db['tsar_haptista'] = db['tsar'] + db['haptista']
    db['telonema_picozoa_sar_haptista'] = db['tsar_haptista'] + db['picozoa']
    # Picozoa+Telonema
    db['picozoa_telonema'] = db['telonema'] + db['picozoa']
    # Excavata related hypotheses
    db['excavata_anaeramoeba_malawimonada'] = db['discoba'] + db['malawimonada'] + db['metamonada_with_anaeramoeba']
    db['excavata_malawimonada'] = db['discoba'] + db['malawimonada'] + db['metamonada_no_anaeramoeba']
    db['excavata_anaeramoeba'] = db['discoba'] + db['metamonada_with_anaeramoeba']
    db['excavata'] = db['discoba'] + db['metamonada_no_anaeramoeba']
    db['metamonada_malawimonada'] = db['metamonada_no_anaeramoeba'] + db['malawimonada']
    db['metamonada_ancyromonada'] = db['metamonada_no_anaeramoeba'] + db['ancyromonada']
    db['metamonada_anaeramoeba_malawimonada'] = db['metamonada_with_anaeramoeba'] + db['malawimonada']
    db['metamonada_anaeramoeba_ancyromonada'] = db['metamonada_with_anaeramoeba'] + db['ancyromonada']
    db['metamonada_malawimonada_ancyromonada'] = db['metamonada_no_anaeramoeba'] + db['malawimonada'] + db['ancyromonada']
    db['metamonada_anaeramoeba_malawimonada_ancyromonada'] = db['metamonada_with_anaeramoeba'] + db['malawimonada'] + db['ancyromonada']
    db['malawimonada_ancyromonada'] = db['malawimonada'] + db['ancyromonada']
    # SAR + Excavata
    db['sar_excavata_anaeramoeba'] = db['sar'] + db['excavata_anaeramoeba']
    db['sar_excavata'] = db['sar'] + db['excavata']
    db['tsar_excavata_anaeramoeba'] = db['tsar'] + db['excavata_anaeramoeba']
    db['tsar_excavata'] = db['tsar'] + db['excavata']
    db['telonema_picozoa_sar_excavata_anaeramoeba'] = db['telonema_picozoa_sar'] + db['excavata_anaeramoeba']
    db['telonema_picozoa_sar_excavata'] = db['telonema_picozoa_sar'] + db['excavata']
    # Amoebozoa related hypotheses
    db['amoebozoa_anaeramoeba'] = db['amoebozoa'] + ['Anaeramoeba_flamelloides', 'Anaeramoeba_ignava']
    db['diaphoretickes'] = db['archaeplastida'] + db['cryptista'] + db['sar'] + db['provora'] + db['haptista'] + db['picozoa_telonema']
    db['obazoa'] = db['opisthokonta'] + ['Thecamonas_trahens', 'Pygsuia_biforma']
    return db


def prep_splits(split_section):
    splits = {}
    for i in split_section:
        score, taxa = i.split('\t ')
        split_taxa = [int(i) for i in list(taxa.split())]
        split_taxa.sort()
        splits[str(split_taxa)] = int(score)
    return splits


def prep_taxa(nex_splits_file):
    init_parse = [i.rstrip().replace("'","").replace("[","").replace("]","").split() for i in open(nex_splits_file).readlines() if i.startswith('[')]
    taxa = {i[-1]:int(i[0]) for i in init_parse}
    return taxa


def parse_nexus_splits(nex_splits_file: str):
    taxa = prep_taxa(nex_splits_file)
    split_section = [i.strip('\n\t') for i in open(nex_splits_file).read().split("MATRIX")[-1].split(';')[0].rstrip().split(",")[:-1]]
    split_vals = prep_splits(split_section)
    return taxa, split_vals


def get_topo_taxa(taxa, topo_taxa):
    return str(sorted(taxa[i] for i in topo_taxa))


def assess_topologies(nex_splits_file: str, outfile: str, etol_317: bool = True):
    if etol_317:
        topo_db = etol_317_groups()
    else:
        topo_db = etol_385_groups()

    taxa, split_vals = parse_nexus_splits(nex_splits_file)
    topo_split_vals = {}

    for k, v in topo_db.items():
        topo_taxa = get_topo_taxa(taxa, v)
        try:
            topo_split_vals[k] = split_vals[topo_taxa]
        except:
            topo_split_vals[k] = 0

    final_db = {nex_splits_file.rpartition("/")[-1].rpartition(".splits.nex")[0]: topo_split_vals}
    final_df = pd.DataFrame(final_db).T

    final_df.to_csv(f'{outfile}.BootStrapEval.csv')

if __name__ == '__main__':
    try:
        nex_splits_file = sys.argv[1]
        outfile = sys.argv[2]
    except:
        print('\nUsage:\n\n    python3 eval_nexus_splits.py [NEXUS-SPLITS-FILE] [OUTPUT-TABLE-NAME]\n')
        sys.exit(1)

    etol_317 = True

    assess_topologies(nex_splits_file, outfile, etol_317)
