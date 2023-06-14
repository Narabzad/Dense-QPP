import collections
import math
import rbo

original_run=open('run/msmarco-queries.dev.small.tsvoriginal_run.tsv','r').readlines()
noisy_run_file='Noisyq_0.01.msmarco-queries.dev.small.tsv'
noisy_run=open('run/'+noisy_run_file,'r').readlines()
noisy_dic=collections.defaultdict(list)
for line in noisy_run:
    qid,docid,rank=line.rstrip().split('\t')
    noisy_dic[qid].append(docid)
        
org_dic=collections.defaultdict(list)
for line in original_run:
    qid,docid,rank=line.rstrip().split('\t')
    org_dic[qid].append(docid)

print('run files loaded')
for K in range(1,11):
    K=K*100
    print('RBO on depth', K)
    rank_org_ar=[]
    rank_noise_ar=[]
    out=open('results/rbo_'+noisy_run_file+'_'+str(K),'w')
    for qid in org_dic:
        rank_org_ar=[]
        rank_noise_ar=[]
        for doc in org_dic[qid][:K]:
            rank_org=org_dic[qid].index(doc)
            try:
                rank_noise=noisy_dic[qid].index(doc)
                rank_noise_ar.append(int(rank_noise))
            except:
                pass
            rank_org_ar.append(int(rank_org))
            
        sm=rbo.RankingSimilarity(org_dic[qid][:K], noisy_dic[qid][:K]).rbo()
        out.write(qid+'\t'+str(sm)+'\n')
    out.close()


    
