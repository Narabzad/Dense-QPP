# Dense-QPP

This repository replicate Dense-QPP approach Query Performance Prediction results four different query sets including MS MARCO passage dataset , TREC Deep Learning track 2019 and 2020 and TREC DL-Hard. 

Dense-QPP is an unsupervised Query Performance Prediction (QPP) method that is specifically designed for dense retrievers. Dense-QPP operates based on measuring query robustness in light of possible perturbations. To generate query perturbations, we propose to systematically inject noise into the contextualized representation of the query, and compare the retrieved list for the original query with that of the perturbed query. 

## Dense-QPP on MS MARCO queries:
1. Clone This repository and install the required packages are listed in requirement.txt on python 3.7+.
3. Download the [indexed MS MARCO passage using FAISS library from here](https://drive.google.com/file/d/1AQIY_o7vtBLoSS-h3kiNccLPCYFexUtk/view?usp=sharing) and store it in ```msmarco-data``` directory.
4. To get the original run of the dense retriever on msmarco, run ```python Original_retrieval.py```.  The run file will be stored in  ```run``` directory. Alternatively, you can download the [original run files (retrieved results for the four query sets) from here](https://drive.google.com/drive/folders/1QAWyD4V0Fxey-7tsMdWHc5leoS1jhZpW?usp=sharing).
5. To retrieve the results with noisy queries, you can run ```python Noisy_retrieval.py```. This will generate 10 run files with noisy queries which were injected white noise with different levels of standard deviation. The run files will be stored in  ```run``` directory. You can also modify the ```var``` variable to inject your desired white noise. 
6. Now you have the original runfiles as well as runfiles for noisy queries, you can compute the similarity between the two ranked list using ```rankbiasoverlap.py``` python script. You may set the ```original_run``` and ```noisy_run_file```] variable in ```rankbiasoverlap.py```  accordingly to the address of origninal run file as well as runfile created by noisy queries. Further, the similarity between the orignial file and runfile by noisy queries will be stores in ```results``` directore as the predicted performance for each query. 
7. In last step, you can measure the correaltion between actual performance of queries. using ```corr.py``` .In this case You can find the actual performance for each query in ```performance``` directory. 

## Dense-QPP on Trec DL 2019, 2020 and DL-Hard and other query sets: 

To replicate the QPP results on TREC DL-related query sets, you can follow the above mentioned instructions by associated retrieved results for any query set of interest. 
- You can find the mentioned queries and their judged relevance documents (qrels) in ```msmarco-data``` directory.
- By passing any query file to ```q_file_name``` in ```Original_retrieval.py``` and ```Noisy_retrieval.py``` you may retrieve the results for other query sets;
- Once you have the retrieved run  files for original queries as well as results for noise injected queries in any query set, you can measure the ranked bias overlap similarity between them using ```rankbiasoverlap.py``` by setting the ```original_run``` and ```noisy_run_file``` variable in ```rankbiasoverlap.py```.
- Finally, you can measure correlation between predicted performance vs actual performance (reported in ```performance``` directory) by ```corr.py```
