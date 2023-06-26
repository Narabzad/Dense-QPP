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

## More results
Due to space constraints, we were unable to include the Spearman's Rho results in the table presented in the paper. However, we would like to report the correlation results for Pearson's Rho, Kendall's Tau, and Spearman's Rho on the four datasets in relation to the experiment conducted for predicting both SBERT (Table 1) and ANCE (Table 2) dense retrievers.

### SBERT
|              | MS MARCO |        |          |   2019  |        |          |   2020  |        |          |   Hard  |        |          |
|--------------|:--------:|:------:|:--------:|:-------:|:------:|:--------:|:-------:|:------:|:--------:|:-------:|:------:|:--------:|
|              | Pearson  | Kendal | Spearman | Pearson | Kendal | Spearman | Pearson | Kendal | Spearman | Pearson | Kendal | Spearman |
| Clarity      |    0.065 |  0.053 |    0.073 |   0.217 |  0.111 |    0.151 |   0.196 |  0.137 |    0.188 |   0.232 |  0.110 |    0.162 |
| QF           |    0.175 |  0.115 |    0.153 |   0.071 |  0.022 |    0.043 |   0.148 |  0.029 |    0.052 |   0.044 |  0.051 |    0.060 |
| NQC          |    0.219 |  0.202 |    0.280 |   0.560 |  0.419 |    0.595 |   0.285 |  0.194 |    0.289 |   0.418 |  0.276 |    0.381 |
| WIG          |    0.048 |  0.032 |    0.044 |   0.139 |  0.071 |    0.116 |   0.153 |  0.032 |    0.051 |   0.093 |  0.072 |    0.105 |
| n(sigma_\%)  |    0.128 |  0.128 |    0.180 |   0.501 |  0.361 |    0.532 |   0.242 |  0.158 |    0.232 |   0.400 |  0.259 |    0.369 |
| SMV          |    0.183 |  0.127 |    0.171 |   0.577 |  0.428 |    0.600 |   0.360 |  0.246 |    0.357 |   0.396 |  0.314 |    0.438 |
| UEF          |    0.218 |  0.166 |    0.224 |   0.607 |  0.428 |    0.601 |   0.336 |  0.228 |    0.329 |   0.441 |  0.298 |    0.412 |
| NeuralQPP    |    0.060 |  0.055 |    0.075 |   0.209 |  0.057 |    0.057 |   0.152 |  0.015 |    0.003 |   0.232 |  0.080 |    0.103 |
| Pclarity_NQC |    0.213 |  0.136 |    0.193 |   0.428 |  0.314 |    0.451 |   0.084 |  0.202 |    0.292 |   0.088 |  0.053 |    0.083 |
| NQAQPP       |    0.267 |  0.216 |    0.292 |   0.269 |  0.129 |    0.160 |   0.221 |  0.159 |    0.234 |   0.113 |  0.240 |    0.359 |
| BERTQPP      |    0.292 |  0.223 |    0.301 |   0.334 |  0.143 |    0.194 |   0.378 |  0.273 |    0.411 |   0.435 |  0.181 |    0.256 |
| qppBERT-PL   |    0.277 |  0.230 |    0.288 |   0.299 |  0.131 |    0.183 |   0.344 |  0.224 |    0.335 |   0.405 |  0.171 |    0.225 |
| DeepQPP      |    0.021 |  0.017 |    0.024 |   0.139 |  0.103 |    0.106 |   0.262 |  0.197 |    0.291 |   0.096 |  0.049 |    0.065 |
| QPP-PRP      |    0.010 |  0.014 |    0.275 |   0.203 |  0.204 |    0.281 |   0.181 |  0.143 |    0.219 |   0.181 |  0.099 |    0.144 |
| DenseQPP     |    0.335 |  0.296 |    0.403 |   0.683 |  0.437 |    0.607 |   0.390 |  0.274 |    0.425 |   0.465 |  0.339 |    0.492 |


 ### ANCE

 |              | MS MARCO |        |          |   2019  |        |          |   2020  |        |          |   Hard  |        |          |
|--------------|:--------:|:------:|:--------:|:-------:|:------:|:--------:|:-------:|:------:|:--------:|:-------:|:------:|:--------:|
|              | Pearson  | Kendal | Spearman | Pearson | Kendal | Spearman | Pearson | Kendal | Spearman | Pearson | Kendal | Spearman |
| Clarity      |    0.161 |  0.196 |    0.233 | 0.353   | 0.237  | 0.344    |   0.281 |  0.215 |    0.320 |   0.221 |  0.230 |    0.331 |
| QF           |    0.071 |  0.034 |    0.045 |   0.129 |  0.098 |    0.148 |   0.283 |  0.257 |    0.361 |   0.155 |  0.118 |    0.165 |
| NQC          |    0.109 |  0.140 |    0.193 |   0.504 |  0.335 |    0.446 |   0.442 |  0.328 |    0.449 |   0.235 |  0.300 |    0.424 |
| WIG          |    0.100 |  0.100 |    0.137 |   0.159 |  0.120 |    0.186 |   0.230 |  0.195 |    0.275 |   0.166 |  0.133 |    0.189 |
| n(sigma_\%)  |    0.030 |  0.042 |    0.058 |   0.361 |  0.233 |    0.347 |   0.199 |  0.181 |    0.262 |   0.242 |  0.197 |    0.275 |
| SMV          |    0.109 |  0.152 |    0.211 |   0.518 |  0.337 |    0.447 |   0.417 |  0.328 |    0.456 |   0.174 |  0.290 |    0.438 |
| UEF          |    0.198 |  0.219 |    0.301 |   0.520 |  0.350 |    0.453 |   0.458 |  0.348 |    0.497 |   0.229 |  0.310 |    0.458 |
| NeuralQPP    |    0.073 |  0.060 |    0.082 |   0.047 |  0.004 |    0.035 |   0.220 |  0.087 |    0.120 |   0.142 |  0.063 |    0.099 |
| Pclarity_NQC |    0.125 |  0.138 |    0.186 |   0.423 |  0.288 |    0.383 |   0.498 |  0.309 |    0.420 |   0.434 |  0.408 |    0.561 |
| NQAQPP       |    0.267 |  0.221 |    0.298 |   0.115 |  0.140 |    0.192 |   0.147 |  0.152 |    0.204 |   0.334 |  0.264 |    0.360 |
| BERTQPP      |    0.271 |  0.218 |    0.298 |   0.144 |  0.165 |    0.232 |   0.362 |  0.268 |    0.381 |   0.213 |  0.143 |    0.049 |
| qppBERT-PL   |    0.251 |  0.208 |    0.273 |   0.229 |  0.189 |    0.247 |   0.313 |  0.205 |    0.280 |   0.303 |  0.254 |    0.342 |
| Deep-QPP     |    0.031 |  0.032 |    0.044 |   0.183 |  0.195 |    0.264 |   0.196 |  0.127 |    0.194 |   0.154 |  0.131 |    0.175 |
| QPP-PRP      |    0.016 |  0.014 |    0.019 |   0.096 |  0.086 |    0.107 |   0.201 |  0.170 |    0.278 |   0.016 |  0.004 |    0.033 |
| DenseQPP     |    0.296 |  0.242 |    0.327 |   0.528 |  0.363 |    0.482 |   0.443 |  0.332 |    0.483 |   0.315 |  0.310 |    0.456 |

