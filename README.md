# Lead_Prediction
![leads1](https://user-images.githubusercontent.com/57361655/187251593-3ab4c36d-5c7c-4c52-9325-7d28f75eed80.jpg)

Created by: Omer Rugi - [Email](mailto:omerihay@gmail.com) - [Linkedin](https://www.linkedin.com/in/omerugi/)

## The problem:
The major part of telemarketing leads!
Leads are potential customers that the telemarketer tries and convince to buy.
But calling each lead takes a lot of time and many of those called end up with no sale.
To try and solve it, I've implemented a lead predictor! it takes the information of the lead and returns a probability of how likely this lead will be converted to a sell.

I've  worked on the data of a telemarketing agency in India and based on the information they provied try and predict. 

## Data:
* Smples - 9240.
* Featuers - 36.
* Featuers with missing data - 12.
* Featuers with non-numeric data - 14.

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

- [x] TotalVisits - Missing to Mean (Or use model)
- [x] Page Views Per Visit - Missing to Mean (Or use model)
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
