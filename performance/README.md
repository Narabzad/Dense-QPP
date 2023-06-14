
You can evaluate the oridginal run files and obtain the actual performance using diferent tools. 

The ```mrr.py``` scripts can calculate mrr of any run file given the relevance judgements (qrels) as well as the original run file and store the results in ```performance``` directory, e.g.:

```python mrr.py -qrels msmarco-data/msmarco-qrels.dev.small.trec -run run/msmarco-original_run.tsv ``` 


You may also use [```trec_eval``` tool](https://github.com/usnistgov/trec_eval) to measure other evaluatio nmetrics such as ndcg,Mean Average Precision, etc at different cutoffs. 
