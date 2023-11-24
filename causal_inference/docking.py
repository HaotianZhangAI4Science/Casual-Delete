from docking_utils import *
from glob import glob
import os
import numpy as np
import pandas as pd
import os.path as osp
from tqdm import tqdm
import pickle
import shutil
def read_pkl(pkl_file):
    with open(pkl_file,'rb') as f:
        data = pickle.load(f)
    return data

def write_pkl(data_list, pkl_file):
    with open(pkl_file, 'wb') as f:
        pickle.dump(data_list, f)

work_dir = './SDF'
pdb_file = '4fny_protein.pdb'
ori_lig_file = '4fny_ori.sdf'
protein_pdbqt = prepare_target(work_dir, pdb_file)
centroid = sdf2centroid(ori_lig_file)


result_list = []
for j in tqdm(range(3472)):
    try:
        lig_pdbqt = prepare_ligand(work_dir, f'{j}.sdf', verbose=0)
        docked_sdf = docking_with_sdf(work_dir,osp.basename(protein_pdbqt), lig_pdbqt, centroid, verbose=1)
        result = get_result(docked_sdf=docked_sdf, ref_mol= None)
        result_list.append(result)
    except Exception as e:
        print(e)
write_pkl(result_list, './gen_docking_results.pkl')