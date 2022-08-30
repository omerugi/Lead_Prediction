# Lead_Prediction
![leads1](https://user-images.githubusercontent.com/57361655/187251593-3ab4c36d-5c7c-4c52-9325-7d28f75eed80.jpg)

Created by: Omer Rugi - [Email](mailto:omerihay@gmail.com) - [Linkedin](https://www.linkedin.com/in/omerugi/)

[![My Skills](https://skillicons.dev/icons?i=python,fastapi,postgres)](https://skillicons.dev)

## What I wanted to get from this project:
The idea behind this project is to overcome dirty and diffecult dataset, the one I'm using contains several non-numeric categories, a lot of missing values, and useless featues.

## The problem:
The major part of telemarketing leads!
Leads are potential customers that the telemarketer tries and convince to buy.
But calling each lead takes a lot of time and many of those called end up with no sale.
To try and solve it, I've implemented a lead predictor! it takes the information of the lead and returns a probability of how likely this lead will be converted to a sell.

I've  worked on the data of a telemarketing agency in India and based on the information they provied try and predict. 

## General idea:
The general idea is to create a datea processing pipline (made of 3 steps) + a model, that will process the data and new data. while also pretrain and save models for fastter responses.
Afther cerating the pipline there is a web server that recives samples of new leads, and return the probabilty of them converting + keep that prediction on a DB.
The web server is based on FastAPI, and the DB using postgres.

## The project structuer:
`LeadPrediction.ipynb` - the notebook with all the plots + pipline + models.
`var.py` - contains all the varibles that cannot change and are used in the pipline.
`main_rout.py` - web server API.
`models` - folder that keeps all the pre trained models used in the pipline (OneHot, KNNImp, LR).
`data_sets` - folder that keep the original dataset + a dataset after each step in the pipline (there are 3 steps).
`database` - connection to the data base + the models of the tables.
`repos` - the data layer with all the functinalitys to process new samples.

## Data:
* Smples - 9240.
* Featuers - 36.
* Featuers with missing data - 12.
* Featuers with non-numeric data - 14.

## Issues and solutions:

* Missing values - there where a lot of missing values in several featuers, and I used few ideas to overcome this problem.
    * Use default value - Some featuers had "default value" (like - "Other"), so in does cases I've replaced the missing value with the "default value".
    * Mean values - in featuers with numerice values like counters, I've used the mean of the featuer.
    * KNN Imputer - some featuers represented the score of the lead, important featuers, so using KNN Imputer I've filled in the missing values.

* Featuers noise - some featuers where noise that will be useless to the model, so I had to clean them in several ways.
    * All "no" featuers - they seem useless so they were removed.
    * Small amount of samples - some featues had categories in them with very few samples, so I've used a threshold to make thoes into "default value".
    * Duplicated featuers - featuers with the same "idea" behind them were merged.
    * Splitting featuers - one featuer had few categories that were similar to other featuers, so I needed to split and merge.
    * Typo - fixed typo in featuers so the categories are similar.

* Non numeric featuers - many featuers had categories in them, or some rank, so they had to be Encoded properly.
    * Categories - used OneHot Encoding.
    * Rank - replace the "words" to ranking in numbers.



## The process:

### First step - Replace NaN values and Encode features:
- [x] NaN to missing
- [x] Boolean to 0,1
- [x] Asymmetrique Index Encoding - Replace the low,mid,high with 1,2,3.
- [x] Lead Quality Encoding - Replace Worst, Low in Relevance, Not Sure, Might be, and High in Relevance with 1-5.

### Second step - Modify Features:
- [x] Lead Source : 
    - google to Google
    - less then 50 to Other
- [x] Countries - Split the feature to India and Other
- [x] How did you hear about X Education - Missing to Other
- [x] What matters most to you in choosing a course - Missing to Other
- [x] Lead Profile - Missing to Other Leads
- [x] City - Missing to Other Cities.

- [x] TotalVisits - Missing to Mean.
- [x] Page Views Per Visit - Missing to Mean.
- [x] Create Featuers:
    - Other
    - Multiple Sources
    - Social Media
    - Direct Advertisement
    - Advertisement (replace Digital Advertisement)
- [x] Merge & Drop:
    - Magazine + Newspaper Article + Newspaper => Newspaper/Magazine.
- [x] Map "How did you hear about X Education" to Features:
    - Online Search => Search
    - Word Of Mouth, Student of SomeSchool => Through Recommendations
    - Other => (new feature) Other
    - Multiple Sources => (new feature) Multiple Sources
    - Advertisements => (new feature) Advertisement
    - Social Media => (new feature) Social Media
    - SMS, Email => (new feature) Direct Advertisement
- [x] Drop "Receive More Updates About Our Courses", "Update me on Supply Chain Content", "Get updates on DM Content","I agree to pay the amount through cheque" -> All "No", useless.
- [x] Drop "Lead Number" -> Will not give us insights.
- [x] Drop "City" -> Lot's of "other" and missing data.
- [x] Drop "Last Activity" -> Duplicated.
- [x] Drop "Tags" -> Given after a call, will not be filled for new lead.

### Third step - Modify Features with models:
- [x] One Hot Encoding - save models + init in code
- [x] Asymmetrique Features - Fill in using imputer & median.

### Fourth step - Running predictions:
- [x] Logistic Regression
