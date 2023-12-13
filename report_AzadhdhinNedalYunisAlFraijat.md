---
title: 'Student dropout analysis based on previously  acquired educational achievements: A case of the University of Portalegre'
subtitle: Business Analysis, Business Informatics Ms, Fall 2023. 
author: 
    - Izeldeen Nedal Yunis Al Fraijat
    - Danat Semeneev
    - Ieva Žube
    - Pankaj Chettri
    - Kristaps Eglītis^[Rīga Technical University]
abstract: .
date: last-modified
mainfont: CMU Serif
sansfont: CMU Serif 
monofont: CMU Serif
fontenc: T2A
lang: en
keywords: AA1, AA2
link-citations: true
tbl-cap-location: bottom
csquotes: true
execute:
  echo: false
  eval: true
  warning: false
  error: true
  include: true
format:
  pdf:
    pdf-engine: xelatex
    pdf-engine-opt: '-shell-escape'
    keep-tex: true
    keep-md: true
    cite-method: biblatex
    header-includes:
    - \usepackage{csquotes}
    - \usepackage[authordate, abbreviate = true, date = year, autocite=inline, backref = true]{biblatex-chicago}
  html:
    html-math-method: katex
bibliography: bibliography.bib
---


 <!-- {{< include ./text/abstract_text.txt >}}  -->

<!-- #  {{< includes ./_abstract.md >}}  -->

## Abstract

In the world of education, the path to success is often visualized as a linear progression, where students follow a predefined journey from kindergarten to graduation. However, the reality is far more complex. There could be various reasons that come along the study program that led students to deviate from this path. These students might encounter different challenges, circumstances, or a lack of proper resources that have led them to drop out of university.


In this dataset provided to us, we will delve deeper into understanding the reasons why students have dropped out of the university, based on the data at our disposal. We will leverage our social knowledge to comprehend the factors that influenced their decision to drop out and work to prevent such occurrences if the issues are within the university's purview. Our goal is to offer solutions, support, and the necessary resources to facilitate students' educational journeys. We will also use the analysis we've conducted on the dropout students to learn from their experiences and chart a unique educational pathway with fewer dropouts.



# Introduction

Starting from preliminary school we are told that having an education is very important for your future or that without higher education your job possibilities are going to be very limited.
While primary education is mandatory, having higher education is not. There are, however, many reasons for which people may want to pursue higher education. 
 According to studies, many factors are materialistic, the most important factor for pursuing higher education is job acquisition [@knutsen_motivation_2011]. Some other factors may include increased income in the existing job, improved work conditions or increased ability for retirement. Of course, other, more intrisic factors include seeking for additional knowledge or self-fulfillment [@cortes_factors_2023]. There are also factors like meeting new friends, improving social interaction skills or just wanting to make a difference in the world.
Of course factors that cannot be ignored are social pressure [@temple_factors_2009], meaning that having friends that want to pursue higher education can influence ones own decision or influence of family members.
However, there are people that discontinue their studies prematurely and we are interested to learn what the reasons for such a decision could be.
Based on the study and datasets that we used for our research there are multiple factors that influence dropping out.

Nevertheless, pursuing higher education and actually getting the degree has some tangible benefits.
According to an OECD – Education at a Glance 2019 research paper [@oecd_education_2019].

> “On average across OECD countries, adults with a short-cycle tertiary degree earn 20% more than adults with upper secondary education. The earnings advantage increases to 44% for those with a bachelor’s degree and to 91% for those with a master’s or doctoral degree.”

With this in mind, it is important for government and educational institutions to ensure high level of graduates in society to ensure economic growth and overall increase in well-being.
To measure the success of this goal, it is important to set KPI’s, track them and make educated conclusions on what needs to be done or is being done right to reach the goal of higher educated society.

## Target Metrics and KPI

In this particular case, KPI’s will be chosen based on datasets of Portugese High Schools but most likely data can be generalised, atleast for Europe, as the region and sociodemographics are not so different.
Even though there are many factors that influence the success of graduation, only factors that can be proven  by government and educational institutions will be chosen. In order to thwart embezzlement, indicators should be restricted in magnitude and difficult to falsify or manipulate.  After rigorous analysis, we propose the following KPIs.

   a.  **Student grade improvement compared to support**.
    Based on the dataset, students who had support had 3x lower dropout rates than students that didn’t have. While it is not practical to allocate higher amount of money for studying that itself does not generate value, it scoops that it at least a sizeable parts of the dropout students could be held from leaving with a relatively small aid that would make the benefits of studies outweigh those of working/etc. Leaving is commonly associated with very poor grades (otherwise, even a morally disinterested student would opt to formally remain in the university until they are asked to leave due to poor performance). Since a person with infinitesimal grades is a clear candidate for dropping out, one should identify those students with abrupt downward grade dynamics and quench this. 
    In the proposed KPI, the $(grade)_{i}$ is the mean relative grade change for student $j$ over all their courses at university i at moment t, and the assistance is the mean aid per student (can be 0). If there are no students on their way down , the KPI is guaranteed to be positive. 

$$KPI_{1, i,t} =  \frac{|\Delta(\bar{grade})_i|}{ (\bar{assistance}_i)}$$
This does not depend on the number of courses, because the courses are themselves  different  difficulties, the important thing that the university (the students too) should look after in this regard, that the situation with grades does drastically deteriorate over time.  

 

a. **Institutional Improvements**. Although volatile and subjective, as one of the metrics (not KPIs, since it is more difficult to tie this to specific redresses) there could be a longitudinal survey about one's satisfaction with the studies and programme in general in the fashion of a job an exit or quasi-exit interview (when a person does not leave actually, but they are still invited to answer the questions as if they would be leaving). This would allow to track the scale of dropouts due to frustration with the programme (not engaging enough). 

a. **Relative changes in student's grades**. 
   Datasets tell us that the higher the average grade, the lower the dropout rate. Usually students that have low grades are uninterested in the subjects which could be due to having chosen not the right program for them or that the way lectures and information is presented is uninteresting or outdated. Either way this can be improved. Increasing the possibility that the student has chosen the right program for him can be done by introducing more “open days” in higher education institutions and having more upfront information about what can be expected from programs. The overall lecture performance can be improved by taking more time to have up-to-date information presented and teachers having decent motivation of teaching students. This can be achieved by increasing teacher salaries and institutions having more control over teachers and information they present to students. 

All these metrics are still vulnerable to misrepresentation, but it is inevitable given the freedom the universities enjoy in managing their study programmes. Still, any manipulation of this metrics can only be temporary and thus is also not in the best interest of the university.  

## Exploratory Data Analysis

### Descriptive Statistics 





As we have checked, the dataset does not have zero values, so there is nothing to purge inside it. Later on, we get the basic descriptive statistics, shown below in  
[Tables -@tbl-descstat-3; -@tbl-descstat-1; -@tbl-descstat-2; -@tbl-descstat-4; -@tbl-descstat-5; -@tbl-descstat-6; -@tbl-descstat-7 ]



::: {#tbl-descstat-1 .cell tbl-cap='Descriptive statistics' execution_count=36}

::: {.cell-output .cell-output-display execution_count=36}
         Mari. stat.    Appl. mode.    Appl. orde.    Cour.    Dayt. atte.
-----  -------------  -------------  -------------  -------  -------------
count        4424           4424           4424     4424           4424
mean            1.18          18.67           1.73  8856.64           0.89
std             0.61          17.48           1.31  2063.57           0.31
min             1              1              0       33              0
25%             1              1              1     9085              1
50%             1             17              1     9238              1
75%             1             39              2     9556              1
max             6             57              9     9991              1
:::
:::


::: {#tbl-descstat-2 .cell tbl-cap='Descriptive statistics (cont\'d)' execution_count=35}

::: {.cell-output .cell-output-display execution_count=35}
         Prev. qual.    Prev. qual. (gra.    Naci.    Moth. qual.    Fath. qual.
-----  -------------  -------------------  -------  -------------  -------------
count        4424                 4424     4424           4424           4424
mean            4.58               132.61     1.87          19.56          22.28
std            10.22                13.19     6.91          15.6           15.34
min             1                   95        1              1              1
25%             1                  125        1              2              3
50%             1                  133.1      1             19             19
75%             1                  140        1             37             37
max            43                  190      109             44             44
:::
:::


::: {#tbl-descstat-3 .cell tbl-cap='Descriptive statistics (cont\'d)' tbl-font-size='8' execution_count=9}

::: {.cell-output .cell-output-display execution_count=9}

```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mother's occupation</th>
      <th>Father's occupation</th>
      <th>Admission grade</th>
      <th>Displaced</th>
      <th>Educational special needs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4424.00</td>
      <td>4424.00</td>
      <td>4424.00</td>
      <td>4424.00</td>
      <td>4424.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>10.96</td>
      <td>11.03</td>
      <td>126.98</td>
      <td>0.55</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>std</th>
      <td>26.42</td>
      <td>25.26</td>
      <td>14.48</td>
      <td>0.50</td>
      <td>0.11</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>95.00</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.00</td>
      <td>4.00</td>
      <td>117.90</td>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.00</td>
      <td>7.00</td>
      <td>126.10</td>
      <td>1.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9.00</td>
      <td>9.00</td>
      <td>134.80</td>
      <td>1.00</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>max</th>
      <td>194.00</td>
      <td>195.00</td>
      <td>190.00</td>
      <td>1.00</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>
```

:::
:::


::: {.cell execution_count=59}

::: {.cell-output .cell-output-display execution_count=59}
```
'Curricular units 2nd sem (enrolled), Curricular units 2nd sem (evaluations), Curricular units 2nd sem (approved), Curricular units 2nd sem (grade)'
```
:::
:::


::: {#tbl-descstat-4 .cell tbl-cap='Descriptive statistics (cont\'d). Columns, left-to-right: Debtor, Tuition fees up to date, Gender, Scholarship holder, Age at enrollment' tbl-font-size='8' execution_count=55}

::: {.cell-output .cell-output-display execution_count=55}
-----  -------  -------  -------  -------  -------
count  4424     4424     4424     4424     4424
mean      0.11     0.88     0.35     0.25    23.27
std       0.32     0.32     0.48     0.43     7.59
min       0        0        0        0       17
25%       0        1        0        0       19
50%       0        1        0        0       20
75%       0        1        1        0       25
max       1        1        1        1       70
-----  -------  -------  -------  -------  -------
:::
:::


::: {#tbl-descstat-5 .cell tbl-cap='Descriptive statistics (cont\'d). Columns International, Curricular units 1st sem (credited), Curricular units 1st sem (enrolled), Curricular units 1st sem (evaluations).' tbl-font-size='8' execution_count=62}

::: {.cell-output .cell-output-display execution_count=62}
-----  -------  -------  -------  -------
count  4424     4424     4424     4424
mean      0.02     0.71     6.27     8.3
std       0.16     2.36     2.48     4.18
min       0        0        0        0
25%       0        0        5        6
50%       0        0        6        8
75%       0        0        7       10
max       1       20       26       45
-----  -------  -------  -------  -------
:::
:::


::: {#tbl-descstat-6 .cell tbl-cap='Descriptive statistics (cont\'d). Columns Curricular units 1st sem (approved), Curricular units 1st sem (grade), Curricular units 1st sem (without evaluations), Curricular units 2nd sem (credited)\'' tbl-font-size='4' execution_count=61}

::: {.cell-output .cell-output-display execution_count=61}
-----  -------  -------  -------  -------
count  4424     4424     4424     4424
mean      4.71    10.64     0.14     0.54
std       3.09     4.84     0.69     1.92
min       0        0        0        0
25%       3       11        0        0
50%       5       12.29     0        0
75%       6       13.4      0        0
max      26       18.88    12       19
-----  -------  -------  -------  -------
:::
:::


::: {#tbl-descstat-7 .cell tbl-cap='Descriptive statistics (cont\'d). Curricular units 2nd sem (enrolled), Curricular units 2nd sem (evaluations), Curricular units 2nd sem (approved), Curricular units 2nd sem (grade)\'' execution_count=60}

::: {.cell-output .cell-output-display execution_count=60}
-----  -------  -------  -------  -------
count  4424     4424     4424     4424
mean      6.23     8.06     4.44    10.23
std       2.2      3.95     3.01     5.21
min       0        0        0        0
25%       5        6        2       10.75
50%       6        8        5       12.2
75%       7       10        6       13.33
max      23       33       20       18.57
-----  -------  -------  -------  -------
:::
:::




The students are from multiple countries, but the overwhelming majority of the students are from Portugal. It would be interesting to see how the students' admission grade depends on their previous qualification in their home countries, but the samples are scarce. Many students from abroad are from the Overseas Territories where it's more challenging to get comparable education. However, they and inland Portugal students were naturally given some exemptions, as the dataset states [^source_dataset_docs] 

 . For example, the students admitted per Ordance no. 854 [^dataset] were not required to demonstrate the proof of their validity since their received a diploma in secondary education administered in Portuguese (Angola, East Timor, Mozambique, Guinea Equatorial). Students admitted per Ordnance no. 533 [^conversion] were from another university in Portugal with overlapping courses covered recently enough so they were not required to repeat them. Finally, those admitted per Ordnance no. 612 [^recalculation] came from other countries but had comparable material in their studies and so their points were recalculated with some amortization.
 
 [^recalculation]: Link to the source document: <https://dre.tretas.org/dre/51542/portaria-612-93-de-29-de-junho>


[^source_dataset_docs]: Link to the dataset description: <https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success>
[^conversion]: Link to the source document: <https://dre.tretas.org/dre/104726/portaria-533-A-99-de-22-de-julho> 
[^dataset]: Link to the source document: <https://dre.tretas.org/dre/106607/portaria-854-B-99-de-4-de-outubro>  







::: {.cell execution_count=44}

::: {.cell-output .cell-output-display}
![Relative graduation points for students with different education backgrounds](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/fig-education-output-1.png){#fig-education}
:::
:::


Due to class imbalance , the variability for the Portuguese students is much higher, and while the 3 categories (see @fig-education) with highest grades are natural, i. e. doctors, masters as higher education, the 3rd is unintuitive (the 10 classes) and we tend to explain it as self-selection and high correlation with other indicators (those entering the university in the 10th grade are more motivated then dwelling in schools in 11th and 12th grades).  

Also, there is a drastic imbalance over yet another crucial factor: age. Students of age are far less ubiquitous, can have far more incentives to abandon studies and  smaller potential for apprehension of material. Indeed, this is clearly shown on the next graph [-@fig-age-distr]  

::: {.cell execution_count=45}

::: {.cell-output .cell-output-display}
![Distribution of age for dropout and graduate student](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/fig-age-distr-output-1.png){#fig-age-distr}
:::
:::


Q. v. the sizes of the bins for dropout students differ far less than the total size for the name of the student. 



If the hypothesis about some external factors is correct , the target variable should be much dependent on previous grades,  
The datapoint cloud on [Table -@fig-points-distr], however, shows that this rule has a lot of exceptions. 

::: {.cell execution_count=47}

::: {.cell-output .cell-output-display}
![Joint and marginal distributions of current admission and previous qualification grades](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/fig-points-distr-output-1.png){#fig-points-distr}
:::
:::


We can draw the following observations: 

*  The **distribution of admission grades** is roughly normal with most students scoring between ***120 and 160 marks***.

*  The **distribution of previous qualifications** (grades) is also the same with most of them having grades in between ***120 and 160***.

*  There is seen a **positive correlation** between admission grade and previous qualification grade indicating students with higher previous qualifications tend to have higher admission grades.

This was the visualization for the few quantitative columns, which shows the natural interconnection between the curricularly accrued units in the 1st and the 2nd year, which are in turn mostly unrelated to the admission grade. This is understandable since the grades are commonly based on the successfulness of the local program and student's toil, while the students' backgrounds are commonly different and this puts them into inequitable positions when passing the admission exams. 

In these previous graphs, we considered quantitative columns that are more or less exogenous to the dataset (e. g. age and the previous qualification grade are not influenced by the the current grade of the students).

However, the majority of columns of this dataset are qualitative and they are at least partially endogenous as stem from the decisions during the study. For this, we need to propose a mechanism of influence, then formulate and test a hypothesis via an analysis of discriminate groups. 


We also consider the impact of scholarships and other compensations in academic support, which should alleviate the complications associated with adaptations in new environment. 



<!-- Furthermore, not only the pecuniary, but also institutional aspects can be improved -- and so influence the academic success. Below we demonstrate how the institutional improvements can influence the dropout.  -->



![Student mobility and financial burden as indicators and drivers of their motivation and impediments](./figs/reasons-1.jpg){#fig-word-1}

We see that having debt is always a serious impediment against studies because it gives wrong incentives towards directly making money in the short run instead of focusing solely on one's studies that could aid to make altogether greater money in the long run. 

![Student inter-university mobility and health conditions proxies as indicators and drivers of their motivation towards learning and impediments (Part 2)](./figs/reasons2.jpg){#fig-word-2}

![Marital status as distractor from studying](./figs/rasons-3.jpg){#fig-word-3}



<!-- **Observations :**

*  Schools having *implemented institutional improvements yeilds a significant lowering of the dropout rate* when compared to those without. -->



In different studies, it is quite common to compare the academic success of a student with the academic successes of ttheir parents as this has both direct and indirect effects , s. a. i. e. both are connected to welfare, but also it can be that there is another channel of knowledge transmission to the younger generation. 



**Observations :**
* The bar chart shows that mother's occupation is quite influential. This influence is greater the pa's due to traditional effect, and we distinctly see that students whose mothers are 'white collars' dropout significantly more rarely than those whose mothers are more engaged in physical labor. 
<!-- 
*  The bar chart shows that *Students with mothers in lower-level occupations* tend to have higher dropout rates than compared to those with mothers in high paying jobs. -->

*  This also may suggest the mother's occupation can influence student retention, emphasizing the need for financial support and family engagement.













### Data correlation table (quantitative columns only)

::: {.cell execution_count=36}

::: {.cell-output .cell-output-display}
![Data correlation table (quantitative columns are represented only since there to compute true correlations between quantitative columns it is necessary to OHE-encode them, which would burst no. of columns to many thousands, but the values of the correlations will be statistically insignificant due to low cardinality of 90% of classes)](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/fig-correlation-output-1.png){#fig-correlation}
:::
:::












































In the remaining part, we examine the correlations of purely endogenous temporal variables. This does not give a scoop about the source of causation and is not a good predictor, but exhibits an analysis of autocorrelation inside the quasi-temporal data.



::: {.cell execution_count=28}

::: {.cell-output .cell-output-display}
![](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/cell-54-output-1.png){}
:::
:::


We can see that the points for the 1st semester and 2nd semester are correlated which shows that are one's marks are primary drivers of success and exhibit sizeable correlations 

::: {.cell execution_count=31}

::: {.cell-output .cell-output-display}
![](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/cell-55-output-1.png){}
:::
:::


::: {.cell execution_count=33}

::: {.cell-output .cell-output-display}
![](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/cell-56-output-1.png){}
:::
:::


::: {.cell execution_count=34}

::: {.cell-output .cell-output-display}
![](report_AzadhdhinNedalYunisAlFraijat_files/figure-pdf/cell-57-output-1.png){}
:::
:::


## Data Mining

In this matrix for correlations, we already see high correlations between many values. Hence, if we (certainly) consider qualitative variables in our data mining analysis, we must reduce the number of variables because the true dimensionality of the initial space is too high and virtually all ways of embedding are too costly and prohibitive given a relatively small amount of datapoints in this dataset. 
First our common step would be to dispose of multicollinear columns.  
High dimensionality prevents intuitive DBSCAN threshold setting and some inferior algorithms as TSNE.

After we perform the PCA, we select estimators from various standard families that are idependently fine-tuned and then, by F1 measure, the model that is most precise in predicting the outcome is rendered. 
The results of the best models are given in leaderboard   below in @tbl-leaderboard.
<!-- @tbl-leaderboard. -->

::: {#tbl-leaderboard .cell tbl-cap='Results of fitting estimators of different families' execution_count=42}

::: {.cell-output .cell-output-display}
```
<IPython.core.display.HTML object>
```
:::

::: {.cell-output .cell-output-display}

```{=html}
<style type="text/css">
#T_96c03 th {
  text-align: left;
}
#T_96c03_row0_col0, #T_96c03_row0_col1, #T_96c03_row0_col2, #T_96c03_row0_col3, #T_96c03_row0_col4, #T_96c03_row0_col7, #T_96c03_row1_col0, #T_96c03_row1_col5, #T_96c03_row1_col6, #T_96c03_row2_col0, #T_96c03_row2_col1, #T_96c03_row2_col2, #T_96c03_row2_col3, #T_96c03_row2_col4, #T_96c03_row2_col5, #T_96c03_row2_col6, #T_96c03_row2_col7, #T_96c03_row3_col0, #T_96c03_row3_col1, #T_96c03_row3_col2, #T_96c03_row3_col3, #T_96c03_row3_col4, #T_96c03_row3_col5, #T_96c03_row3_col6, #T_96c03_row3_col7, #T_96c03_row4_col0, #T_96c03_row4_col1, #T_96c03_row4_col2, #T_96c03_row4_col3, #T_96c03_row4_col4, #T_96c03_row4_col5, #T_96c03_row4_col6, #T_96c03_row4_col7, #T_96c03_row5_col0, #T_96c03_row5_col1, #T_96c03_row5_col2, #T_96c03_row5_col3, #T_96c03_row5_col4, #T_96c03_row5_col5, #T_96c03_row5_col6, #T_96c03_row5_col7, #T_96c03_row6_col0, #T_96c03_row6_col1, #T_96c03_row6_col2, #T_96c03_row6_col3, #T_96c03_row6_col4, #T_96c03_row6_col5, #T_96c03_row6_col6, #T_96c03_row6_col7, #T_96c03_row7_col0, #T_96c03_row7_col1, #T_96c03_row7_col2, #T_96c03_row7_col3, #T_96c03_row7_col4, #T_96c03_row7_col5, #T_96c03_row7_col6, #T_96c03_row7_col7, #T_96c03_row8_col0, #T_96c03_row8_col1, #T_96c03_row8_col2, #T_96c03_row8_col3, #T_96c03_row8_col4, #T_96c03_row8_col5, #T_96c03_row8_col6, #T_96c03_row8_col7, #T_96c03_row9_col0, #T_96c03_row9_col1, #T_96c03_row9_col2, #T_96c03_row9_col3, #T_96c03_row9_col4, #T_96c03_row9_col5, #T_96c03_row9_col6, #T_96c03_row9_col7, #T_96c03_row10_col0, #T_96c03_row10_col1, #T_96c03_row10_col2, #T_96c03_row10_col3, #T_96c03_row10_col4, #T_96c03_row10_col5, #T_96c03_row10_col6, #T_96c03_row10_col7, #T_96c03_row11_col0, #T_96c03_row11_col1, #T_96c03_row11_col2, #T_96c03_row11_col3, #T_96c03_row11_col4, #T_96c03_row11_col5, #T_96c03_row11_col6, #T_96c03_row11_col7, #T_96c03_row12_col0, #T_96c03_row12_col1, #T_96c03_row12_col2, #T_96c03_row12_col3, #T_96c03_row12_col4, #T_96c03_row12_col5, #T_96c03_row12_col6, #T_96c03_row12_col7, #T_96c03_row13_col0, #T_96c03_row13_col1, #T_96c03_row13_col2, #T_96c03_row13_col3, #T_96c03_row13_col4, #T_96c03_row13_col5, #T_96c03_row13_col6, #T_96c03_row13_col7, #T_96c03_row14_col0, #T_96c03_row14_col1, #T_96c03_row14_col2, #T_96c03_row14_col3, #T_96c03_row14_col4, #T_96c03_row14_col5, #T_96c03_row14_col6, #T_96c03_row14_col7 {
  text-align: left;
}
#T_96c03_row0_col5, #T_96c03_row0_col6, #T_96c03_row1_col1, #T_96c03_row1_col2, #T_96c03_row1_col3, #T_96c03_row1_col4, #T_96c03_row1_col7 {
  text-align: left;
  background-color: yellow;
}
#T_96c03_row0_col8, #T_96c03_row1_col8, #T_96c03_row2_col8, #T_96c03_row3_col8, #T_96c03_row4_col8, #T_96c03_row5_col8, #T_96c03_row6_col8, #T_96c03_row7_col8, #T_96c03_row8_col8, #T_96c03_row10_col8, #T_96c03_row11_col8, #T_96c03_row12_col8, #T_96c03_row13_col8, #T_96c03_row14_col8 {
  text-align: left;
  background-color: lightgrey;
}
#T_96c03_row9_col8 {
  text-align: left;
  background-color: yellow;
  background-color: lightgrey;
}
</style>
<table id="T_96c03">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_96c03_level0_col0" class="col_heading level0 col0" >Model</th>
      <th id="T_96c03_level0_col1" class="col_heading level0 col1" >Accuracy</th>
      <th id="T_96c03_level0_col2" class="col_heading level0 col2" >AUC</th>
      <th id="T_96c03_level0_col3" class="col_heading level0 col3" >Recall</th>
      <th id="T_96c03_level0_col4" class="col_heading level0 col4" >Prec.</th>
      <th id="T_96c03_level0_col5" class="col_heading level0 col5" >F1</th>
      <th id="T_96c03_level0_col6" class="col_heading level0 col6" >Kappa</th>
      <th id="T_96c03_level0_col7" class="col_heading level0 col7" >MCC</th>
      <th id="T_96c03_level0_col8" class="col_heading level0 col8" >TT (Sec)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_96c03_level0_row0" class="row_heading level0 row0" >catboost</th>
      <td id="T_96c03_row0_col0" class="data row0 col0" >CatBoost Classifier</td>
      <td id="T_96c03_row0_col1" class="data row0 col1" >0.7290</td>
      <td id="T_96c03_row0_col2" class="data row0 col2" >0.8626</td>
      <td id="T_96c03_row0_col3" class="data row0 col3" >0.7290</td>
      <td id="T_96c03_row0_col4" class="data row0 col4" >0.7099</td>
      <td id="T_96c03_row0_col5" class="data row0 col5" >0.7150</td>
      <td id="T_96c03_row0_col6" class="data row0 col6" >0.5443</td>
      <td id="T_96c03_row0_col7" class="data row0 col7" >0.5491</td>
      <td id="T_96c03_row0_col8" class="data row0 col8" >1.5310</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row1" class="row_heading level0 row1" >gbc</th>
      <td id="T_96c03_row1_col0" class="data row1 col0" >Gradient Boosting Classifier</td>
      <td id="T_96c03_row1_col1" class="data row1 col1" >0.7293</td>
      <td id="T_96c03_row1_col2" class="data row1 col2" >0.8674</td>
      <td id="T_96c03_row1_col3" class="data row1 col3" >0.7293</td>
      <td id="T_96c03_row1_col4" class="data row1 col4" >0.7124</td>
      <td id="T_96c03_row1_col5" class="data row1 col5" >0.7147</td>
      <td id="T_96c03_row1_col6" class="data row1 col6" >0.5426</td>
      <td id="T_96c03_row1_col7" class="data row1 col7" >0.5494</td>
      <td id="T_96c03_row1_col8" class="data row1 col8" >0.4880</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row2" class="row_heading level0 row2" >et</th>
      <td id="T_96c03_row2_col0" class="data row2 col0" >Extra Trees Classifier</td>
      <td id="T_96c03_row2_col1" class="data row2 col1" >0.7271</td>
      <td id="T_96c03_row2_col2" class="data row2 col2" >0.8606</td>
      <td id="T_96c03_row2_col3" class="data row2 col3" >0.7271</td>
      <td id="T_96c03_row2_col4" class="data row2 col4" >0.7068</td>
      <td id="T_96c03_row2_col5" class="data row2 col5" >0.7105</td>
      <td id="T_96c03_row2_col6" class="data row2 col6" >0.5377</td>
      <td id="T_96c03_row2_col7" class="data row2 col7" >0.5446</td>
      <td id="T_96c03_row2_col8" class="data row2 col8" >0.0780</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row3" class="row_heading level0 row3" >lightgbm</th>
      <td id="T_96c03_row3_col0" class="data row3 col0" >Light Gradient Boosting Machine</td>
      <td id="T_96c03_row3_col1" class="data row3 col1" >0.7248</td>
      <td id="T_96c03_row3_col2" class="data row3 col2" >0.8591</td>
      <td id="T_96c03_row3_col3" class="data row3 col3" >0.7248</td>
      <td id="T_96c03_row3_col4" class="data row3 col4" >0.7044</td>
      <td id="T_96c03_row3_col5" class="data row3 col5" >0.7092</td>
      <td id="T_96c03_row3_col6" class="data row3 col6" >0.5357</td>
      <td id="T_96c03_row3_col7" class="data row3 col7" >0.5413</td>
      <td id="T_96c03_row3_col8" class="data row3 col8" >0.7420</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row4" class="row_heading level0 row4" >rf</th>
      <td id="T_96c03_row4_col0" class="data row4 col0" >Random Forest Classifier</td>
      <td id="T_96c03_row4_col1" class="data row4 col1" >0.7255</td>
      <td id="T_96c03_row4_col2" class="data row4 col2" >0.8644</td>
      <td id="T_96c03_row4_col3" class="data row4 col3" >0.7255</td>
      <td id="T_96c03_row4_col4" class="data row4 col4" >0.7041</td>
      <td id="T_96c03_row4_col5" class="data row4 col5" >0.7088</td>
      <td id="T_96c03_row4_col6" class="data row4 col6" >0.5357</td>
      <td id="T_96c03_row4_col7" class="data row4 col7" >0.5420</td>
      <td id="T_96c03_row4_col8" class="data row4 col8" >0.1360</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row5" class="row_heading level0 row5" >lda</th>
      <td id="T_96c03_row5_col0" class="data row5 col0" >Linear Discriminant Analysis</td>
      <td id="T_96c03_row5_col1" class="data row5 col1" >0.7190</td>
      <td id="T_96c03_row5_col2" class="data row5 col2" >0.8560</td>
      <td id="T_96c03_row5_col3" class="data row5 col3" >0.7190</td>
      <td id="T_96c03_row5_col4" class="data row5 col4" >0.7047</td>
      <td id="T_96c03_row5_col5" class="data row5 col5" >0.6984</td>
      <td id="T_96c03_row5_col6" class="data row5 col6" >0.5163</td>
      <td id="T_96c03_row5_col7" class="data row5 col7" >0.5310</td>
      <td id="T_96c03_row5_col8" class="data row5 col8" >0.0290</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row6" class="row_heading level0 row6" >ada</th>
      <td id="T_96c03_row6_col0" class="data row6 col0" >Ada Boost Classifier</td>
      <td id="T_96c03_row6_col1" class="data row6 col1" >0.7071</td>
      <td id="T_96c03_row6_col2" class="data row6 col2" >0.8237</td>
      <td id="T_96c03_row6_col3" class="data row6 col3" >0.7071</td>
      <td id="T_96c03_row6_col4" class="data row6 col4" >0.6952</td>
      <td id="T_96c03_row6_col5" class="data row6 col5" >0.6956</td>
      <td id="T_96c03_row6_col6" class="data row6 col6" >0.5077</td>
      <td id="T_96c03_row6_col7" class="data row6 col7" >0.5134</td>
      <td id="T_96c03_row6_col8" class="data row6 col8" >0.0600</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row7" class="row_heading level0 row7" >qda</th>
      <td id="T_96c03_row7_col0" class="data row7 col0" >Quadratic Discriminant Analysis</td>
      <td id="T_96c03_row7_col1" class="data row7 col1" >0.7113</td>
      <td id="T_96c03_row7_col2" class="data row7 col2" >0.8471</td>
      <td id="T_96c03_row7_col3" class="data row7 col3" >0.7113</td>
      <td id="T_96c03_row7_col4" class="data row7 col4" >0.6939</td>
      <td id="T_96c03_row7_col5" class="data row7 col5" >0.6892</td>
      <td id="T_96c03_row7_col6" class="data row7 col6" >0.5023</td>
      <td id="T_96c03_row7_col7" class="data row7 col7" >0.5166</td>
      <td id="T_96c03_row7_col8" class="data row7 col8" >0.0380</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row8" class="row_heading level0 row8" >knn</th>
      <td id="T_96c03_row8_col0" class="data row8 col0" >K Neighbors Classifier</td>
      <td id="T_96c03_row8_col1" class="data row8 col1" >0.6945</td>
      <td id="T_96c03_row8_col2" class="data row8 col2" >0.8128</td>
      <td id="T_96c03_row8_col3" class="data row8 col3" >0.6945</td>
      <td id="T_96c03_row8_col4" class="data row8 col4" >0.6716</td>
      <td id="T_96c03_row8_col5" class="data row8 col5" >0.6792</td>
      <td id="T_96c03_row8_col6" class="data row8 col6" >0.4882</td>
      <td id="T_96c03_row8_col7" class="data row8 col7" >0.4917</td>
      <td id="T_96c03_row8_col8" class="data row8 col8" >0.0380</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row9" class="row_heading level0 row9" >ridge</th>
      <td id="T_96c03_row9_col0" class="data row9 col0" >Ridge Classifier</td>
      <td id="T_96c03_row9_col1" class="data row9 col1" >0.7125</td>
      <td id="T_96c03_row9_col2" class="data row9 col2" >0.0000</td>
      <td id="T_96c03_row9_col3" class="data row9 col3" >0.7125</td>
      <td id="T_96c03_row9_col4" class="data row9 col4" >0.6846</td>
      <td id="T_96c03_row9_col5" class="data row9 col5" >0.6676</td>
      <td id="T_96c03_row9_col6" class="data row9 col6" >0.4912</td>
      <td id="T_96c03_row9_col7" class="data row9 col7" >0.5196</td>
      <td id="T_96c03_row9_col8" class="data row9 col8" >0.0220</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row10" class="row_heading level0 row10" >dt</th>
      <td id="T_96c03_row10_col0" class="data row10 col0" >Decision Tree Classifier</td>
      <td id="T_96c03_row10_col1" class="data row10 col1" >0.6237</td>
      <td id="T_96c03_row10_col2" class="data row10 col2" >0.7070</td>
      <td id="T_96c03_row10_col3" class="data row10 col3" >0.6237</td>
      <td id="T_96c03_row10_col4" class="data row10 col4" >0.6283</td>
      <td id="T_96c03_row10_col5" class="data row10 col5" >0.6251</td>
      <td id="T_96c03_row10_col6" class="data row10 col6" >0.3907</td>
      <td id="T_96c03_row10_col7" class="data row10 col7" >0.3914</td>
      <td id="T_96c03_row10_col8" class="data row10 col8" >0.0290</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row11" class="row_heading level0 row11" >lr</th>
      <td id="T_96c03_row11_col0" class="data row11 col0" >Logistic Regression</td>
      <td id="T_96c03_row11_col1" class="data row11 col1" >0.4754</td>
      <td id="T_96c03_row11_col2" class="data row11 col2" >0.5142</td>
      <td id="T_96c03_row11_col3" class="data row11 col3" >0.4754</td>
      <td id="T_96c03_row11_col4" class="data row11 col4" >0.3960</td>
      <td id="T_96c03_row11_col5" class="data row11 col5" >0.4313</td>
      <td id="T_96c03_row11_col6" class="data row11 col6" >0.0909</td>
      <td id="T_96c03_row11_col7" class="data row11 col7" >0.0956</td>
      <td id="T_96c03_row11_col8" class="data row11 col8" >0.4810</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row12" class="row_heading level0 row12" >nb</th>
      <td id="T_96c03_row12_col0" class="data row12 col0" >Naive Bayes</td>
      <td id="T_96c03_row12_col1" class="data row12 col1" >0.4997</td>
      <td id="T_96c03_row12_col2" class="data row12 col2" >0.5850</td>
      <td id="T_96c03_row12_col3" class="data row12 col3" >0.4997</td>
      <td id="T_96c03_row12_col4" class="data row12 col4" >0.3821</td>
      <td id="T_96c03_row12_col5" class="data row12 col5" >0.3679</td>
      <td id="T_96c03_row12_col6" class="data row12 col6" >0.0198</td>
      <td id="T_96c03_row12_col7" class="data row12 col7" >0.0399</td>
      <td id="T_96c03_row12_col8" class="data row12 col8" >0.0230</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row13" class="row_heading level0 row13" >dummy</th>
      <td id="T_96c03_row13_col0" class="data row13 col0" >Dummy Classifier</td>
      <td id="T_96c03_row13_col1" class="data row13 col1" >0.4994</td>
      <td id="T_96c03_row13_col2" class="data row13 col2" >0.5000</td>
      <td id="T_96c03_row13_col3" class="data row13 col3" >0.4994</td>
      <td id="T_96c03_row13_col4" class="data row13 col4" >0.2494</td>
      <td id="T_96c03_row13_col5" class="data row13 col5" >0.3326</td>
      <td id="T_96c03_row13_col6" class="data row13 col6" >0.0000</td>
      <td id="T_96c03_row13_col7" class="data row13 col7" >0.0000</td>
      <td id="T_96c03_row13_col8" class="data row13 col8" >0.0520</td>
    </tr>
    <tr>
      <th id="T_96c03_level0_row14" class="row_heading level0 row14" >svm</th>
      <td id="T_96c03_row14_col0" class="data row14 col0" >SVM - Linear Kernel</td>
      <td id="T_96c03_row14_col1" class="data row14 col1" >0.3043</td>
      <td id="T_96c03_row14_col2" class="data row14 col2" >0.0000</td>
      <td id="T_96c03_row14_col3" class="data row14 col3" >0.3043</td>
      <td id="T_96c03_row14_col4" class="data row14 col4" >0.2231</td>
      <td id="T_96c03_row14_col5" class="data row14 col5" >0.2482</td>
      <td id="T_96c03_row14_col6" class="data row14 col6" >0.0001</td>
      <td id="T_96c03_row14_col7" class="data row14 col7" >-0.0007</td>
      <td id="T_96c03_row14_col8" class="data row14 col8" >0.0290</td>
    </tr>
  </tbody>
</table>
```

:::

::: {.cell-output .cell-output-display}
```
<IPython.core.display.HTML object>
```
:::
:::


Thus, the best model by F1 measure is CatBoostClassifier, which is renowned for scoring fairly well on tabular data, while ordinary GBC is the most second to prime and the most robust one, featuring best conventional recall, accuracy, and precision metrics. 

However, while all top models in @tbl-leaderboard demonstrate significant improvement over a dummy classifier and other simplistic models such as Logistic Regression, the scores are still 
which indicates that reduction of dimensionality, which is inevitable under given class imbalance, has come at a price of variance loss, or, alternatively, all the covariates do not explain sufficiently well the outcome of studies: in academic success, as in life, a lot depends on the proper characteristics of a person which are difficult to elicit and much is undetermined. After all, it is a matter of principle whether to continue studying despite all ordeals. 

## **Conclusion**

> With this analysis, we have some valuable insights some crucial factors like Academic support, socioeconomic factors, previous qualifications, and others play a significant role in student retention.  


> The observed patterns imply a lot to stress in the lives of students and their associates. First, we strive to insentivize parents to improve their labour efficiency and pursue greater carreer so that ultimately they could dedicate more time to their children's education, and proactively stir their self-propelled interest. 
 Additionally, we could provide financial assistance to those who are struggling to pay with if this is contemporaneous with a significant degradation in their university marks, as this subrogates the stimuli for a person in an age where they are most perceptive to knowledge and is a good predictor of a dropout. 
 Also importantly, we could teach the students, especially going on their second studies, that it is quite unlikely that they are going to get high grades or exit the university without proper time management and confirmation that they assign top priority to their studies. They are also advised to make that clear to all their relatives and stakeholders who might underestimate the effects of such a change. Although this could result in a reduction of enthusiastic entrants, this would increase at least the KPI of retention and arguably also increase the KPI on number of diplomas issued, because with fewer but more motivated students the university would have more time to dedicate to most obstinate pending alumni.

> Addressing these factors carefully can effectively lead to dropout rates reduction and improve overall student outcomes













