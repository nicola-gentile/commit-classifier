# commit-classifier
This project contains a tool that identifies the developer that commited more bug fix and the developer that committed more new feature. Running benchmarks is asd branch we obtained the following results over the dataset.

```
Correct predictions: 916/1151 (80.0%)
Wrong predictions: 235/1151 (20.0%)
1. bug fix
2. refactoring
3. new feature
Predict   1         2         3         
Actual
1         405       89        6         

2         37        328       39        

3         13        51        183       





Overall Statistics : 

95% CI                                                            (0.77254,0.81912)
ACC Macro                                                         0.86389
ARI                                                               0.48311
AUNP                                                              0.843
AUNU                                                              0.84146
Bangdiwala B                                                      0.64518
Bennett S                                                         0.69374
CBA                                                               0.75058
CSI                                                               0.58546
Chi-Squared                                                       1112.7785
Chi-Squared DF                                                    4
Conditional Entropy                                               0.86121
Cramer V                                                          0.69527
Cross Entropy                                                     1.5386
F1 Macro                                                          0.79033
F1 Micro                                                          0.79583
FNR Macro                                                         0.21241
FNR Micro                                                         0.20417
FPR Macro                                                         0.10467
FPR Micro                                                         0.10209
Gwet AC1                                                          0.69935
Hamming Loss                                                      0.20417
Joint Entropy                                                     2.39039
KL Divergence                                                     0.00942
Kappa                                                             0.6825
Kappa 95% CI                                                      (0.64628,0.71871)
Kappa No Prevalence                                               0.59166
Kappa Standard Error                                              0.01848
Kappa Unbiased                                                    0.68189
Krippendorff Alpha                                                0.68203
Lambda A                                                          0.63902
Lambda B                                                          0.65593
Mutual Information                                                0.65867
NIR                                                               0.4344
NPV Macro                                                         0.8943
NPV Micro                                                         0.89791
Overall ACC                                                       0.79583
Overall CEN                                                       0.40362
Overall J                                                         (1.96602,0.65534)
Overall MCC                                                       0.68511
Overall MCEN                                                      0.54809
Overall RACC                                                      0.35695
Overall RACCU                                                     0.35817
P-Value                                                           None
PPV Macro                                                         0.79787
PPV Micro                                                         0.79583
Pearson C                                                         0.70111
Phi-Squared                                                       0.96679
RCI                                                               0.43074
RR                                                                383.66667
Reference Entropy                                                 1.52918
Response Entropy                                                  1.51989
SOA1(Landis & Koch)                                               Substantial
SOA2(Fleiss)                                                      Intermediate to Good
SOA3(Altman)                                                      Good
SOA4(Cicchetti)                                                   Good
SOA5(Cramer)                                                      Strong
SOA6(Matthews)                                                    Moderate
SOA7(Lambda A)                                                    Strong
SOA8(Lambda B)                                                    Strong
SOA9(Krippendorff Alpha)                                          Tentative
SOA10(Pearson C)                                                  Strong
Scott PI                                                          0.68189
Standard Error                                                    0.01188
TNR Macro                                                         0.89533
TNR Micro                                                         0.89791
TPR Macro                                                         0.78759
TPR Micro                                                         0.79583
Zero-one Loss                                                     235

Class Statistics :

Classes                                                           1             2             3             
ACC(Accuracy)                                                     0.87402       0.81234       0.9053        
AGF(Adjusted F-score)                                             0.84947       0.82856       0.83856       
AGM(Adjusted geometric mean)                                      0.88586       0.81237       0.88796       
AM(Difference between automatic and manual classification)        -45           64            -19           
AUC(Area under the ROC curve)                                     0.8666        0.81223       0.84556       
AUCI(AUC value interpretation)                                    Very Good     Very Good     Very Good     
AUPR(Area under the PR curve)                                     0.85005       0.75637       0.77176       
BB(Braun-Blanquet similarity)                                     0.81          0.70085       0.74089       
BCD(Bray-Curtis dissimilarity)                                    0.01955       0.0278        0.00825       
BM(Informedness or bookmaker informedness)                        0.7332        0.62446       0.69111       
CEN(Confusion entropy)                                            0.31555       0.48476       0.43175       
DOR(Diagnostic odds ratio)                                        51.24316      18.71203      54.58229      
DP(Discriminant power)                                            0.94257       0.70136       0.95769       
DPI(Discriminant power interpretation)                            Poor          Poor          Poor          
ERR(Error rate)                                                   0.12598       0.18766       0.0947        
F0.5(F0.5 score)                                                  0.87284       0.72056       0.78947       
F1(F1 score - harmonic mean of precision and sensitivity)         0.84817       0.75229       0.77053       
F2(F2 score)                                                      0.82485       0.78695       0.75247       
FDR(False discovery rate)                                         0.10989       0.29915       0.19737       
FN(False negative/miss/type 2 error)                              95            76            64            
FNR(Miss rate or false negative rate)                             0.19          0.18812       0.25911       
FOR(False omission rate)                                          0.13649       0.11127       0.06934       
FP(False positive/type 1 error/false alarm)                       50            140           45            
FPR(Fall-out or false positive rate)                              0.0768        0.18742       0.04978       
G(G-measure geometric mean of precision and sensitivity)          0.84911       0.75433       0.77114       
GI(Gini index)                                                    0.7332        0.62446       0.69111       
GM(G-mean geometric mean of specificity and sensitivity)          0.86475       0.81223       0.83905       
HD(Hamming distance)                                              145           216           109           
IBA(Index of balanced accuracy)                                   0.66314       0.65926       0.55664       
ICSI(Individual classification success index)                     0.70011       0.51274       0.54352       
IS(Information score)                                             1.03494       0.99765       1.90311       
J(Jaccard index)                                                  0.73636       0.60294       0.62671       
LS(Lift score)                                                    2.04903       1.99674       3.7402        
MCC(Matthews correlation coefficient)                             0.74334       0.60677       0.71189       
MCCI(Matthews correlation coefficient interpretation)             Strong        Moderate      Strong        
MCEN(Modified confusion entropy)                                  0.44297       0.64189       0.57132       
MK(Markedness)                                                    0.75362       0.58958       0.73329       
N(Condition negative)                                             651           747           904           
NLR(Negative likelihood ratio)                                    0.20581       0.23151       0.27268       
NLRI(Negative likelihood ratio interpretation)                    Poor          Poor          Poor          
NPV(Negative predictive value)                                    0.86351       0.88873       0.93066       
OC(Overlap coefficient)                                           0.89011       0.81188       0.80263       
OOC(Otsuka-Ochiai coefficient)                                    0.84911       0.75433       0.77114       
OP(Optimized precision)                                           0.80871       0.8119        0.78152       
P(Condition positive or support)                                  500           404           247           
PLR(Positive likelihood ratio)                                    10.5462       4.33197       14.88367      
PLRI(Positive likelihood ratio interpretation)                    Good          Poor          Good          
POP(Population)                                                   1151          1151          1151          
PPV(Precision or positive predictive value)                       0.89011       0.70085       0.80263       
PRE(Prevalence)                                                   0.4344        0.351         0.2146        
Q(Yule Q - coefficient of colligation)                            0.96172       0.89854       0.96402       
QI(Yule Q interpretation)                                         Strong        Strong        Strong        
RACC(Random accuracy)                                             0.17172       0.14272       0.04251       
RACCU(Random accuracy unbiased)                                   0.17211       0.14349       0.04258       
TN(True negative/correct rejection)                               601           607           859           
TNR(Specificity or true negative rate)                            0.9232        0.81258       0.95022       
TON(Test outcome negative)                                        696           683           923           
TOP(Test outcome positive)                                        455           468           228           
TP(True positive/hit)                                             405           328           183           
TPR(Sensitivity, recall, hit rate, or true positive rate)         0.81          0.81188       0.74089       
Y(Youden index)                                                   0.7332        0.62446       0.69111       
dInd(Distance index)                                              0.20494       0.26554       0.26385       
sInd(Similarity index)                                            0.85509       0.81223       0.81343       
```
To setup the project run the following commands in the linux shell.
```bash
git clone https://github.com/nicola-gentile/commit-classifier.git
cd commit-classifier
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Command to run the tool
```
python3 main.py <local-repo-path>
```
