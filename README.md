# Lead_Prediction

## The process:

## Plot Data:
- [x] Plot basic data on the features.

## Modify Features:
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
