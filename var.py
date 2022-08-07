'''<<< Model Vars >>>'''
IS_TEST_MODE = True
nan_replacment = "Missing"
data_file_name = "Marketing_Leads_India(1).csv"
imputer_model_path = "knnimputer_model.pkl"
features_with_nan_map_to_other = [
    "How did you hear about X Education",
    "What matters most to you in choosing a course",
    "Lead Profile",
    "City",
    "TotalVisits",
    "Page Views Per Visit"]

mappping_values = {
    'Lead Profile': 'Other Leads',
    'City': 'Other Cities',
    'TotalVisits': 3,
    'Page Views Per Visit': 2}
# TotalVisits,Page Views Per Visit == The mean value of the columns.

new_featuers_lst = [
    'Other',
    'Multiple Sources',
    "Social Media",
    "Direct Advertisement",
    "Newspaper/Magazine"]

mapping_featuers_to_new_featuers = {
        "Online Search": "Search",
        "Word Of Mouth" : "Through Recommendations",
        "Student of SomeSchool" : "Through Recommendations",
        "Other": "Other",
        "Multiple Sources": "Multiple Sources",
        "Advertisements" : "Advertisement",
        "Social Media" : "Social Media",
        "SMS" : "Direct Advertisement",
        "Email" : "Direct Advertisement"}
featuers_to_drop = [
    "Receive More Updates About Our Courses",
    "Lead Number",
    "City",
    "Last Activity",
    "Tags",
    "Update me on Supply Chain Content",
    "Get updates on DM Content",
    "I agree to pay the amount through cheque"]
one_hot_lst = [
    "Lead Origin",
    "Lead Source",
    "Country",
    "Specialization",
    "What is your current occupation",
    "What matters most to you in choosing a course",
    "Lead Profile",
    "Last Notable Activity"]
asymmetrique_activity_median = {
    2.0  :  14.0,
    3.0  :  16.0,
    1.0  :  12.0
}
asymmetrique_profile_median = {
    2.0  :  15.0,
    3.0  :  18.0,
    1.0  :  12.0
}