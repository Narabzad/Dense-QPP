import sys, faiss, json
from torch.utils.data import DataLoader
from sentence_transformers import SentenceTransformer, LoggingHandler, util, models, evaluation, losses, InputExample
import logging
from datetime import datetime
import gzip, os
import tarfile, tqdm
from torch.utils.data import Dataset
import random
from shutil import copyfile
import argparse, torch, pickle

import numpy as np

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])


model_name = 'msmarco-MiniLM-L6-cos-v5'
model = SentenceTransformer(model_name)
model.max_seq_length = 300


data_folder='msmarco-data'
index= faiss.read_index(os.path.join(data_folder,'marco_corpus_faiss') )

top_k = 1000
q_file_name='msmarco-queries.dev.small.tsv'
queries_filepath = os.path.join(data_folder, q_file_name)
qids=[]
queries=[]
with open(queries_filepath, 'r', encoding='utf8') as fIn:
    for line in fIn:
        qid, query = line.strip().split("\t")
        qids.append(qid)
        queries.append(query)
xq = model.encode(queries)
print(xq.shape[1])
print(xq.shape,'q done')

out=open('run/'+q_file_name+'original_run.tsv','w')
    
D, I = index.search(xq, top_k)  # search
rank=1
for q_id in range(len(I)):
    for rank in range(1,top_k +1):
        out.write(qids[q_id]+'\t'+str( I[q_id][rank-1])+'\t'+str(rank)+'\n')
out.close()

