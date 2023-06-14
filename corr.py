import os , numpy
from scipy.stats import pearsonr
from scipy.stats.stats import kendalltau,spearmanr

performance_file=open('performance/mrr_cut_10_Dense-QPP_original_run.tsv','r').readlines()
='Noisyq_0.01.msmarco-queries.dev.small.tsv'

mrr_total=[]
performance_dic={}
for line in performance_file:
    qid,performance=line.rstrip().split()
    performance_dic[qid]=float(performance)
    mrr_total.append(float(performance))
print('MRR ORIGINAL run',numpy.mean(mrr_total))
predicted_file='rbo_'+noisy_run_file+'_500'
qpp_file=open('results/'+predicted_file,'r').readlines()

qpp_dic={}
for line in qpp_file:
    qid,qpp_metrics=line.rstrip().split()
    qpp_metrics=float(qpp_metrics)
    qpp_dic[qid]=float(qpp_metrics)
actual=[]
predicted=[]
for key in performance_dic:
    predicted.append(qpp_dic[key])
    actual.append(performance_dic[key])

print('Correlations for :',predicted_file)
print('Pearson:', pearsonr(actual,predicted)[0], 'P-value:',pearsonr(actual,predicted)[1])
print('kendalltau:', kendalltau(actual,predicted)[0], 'P-value:',kendalltau(actual,predicted)[1])
print('spearmanr:', spearmanr(actual,predicted)[0], 'P-value:',spearmanr(actual,predicted)[1])

