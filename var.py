'''<<< Lead Prediction Vars >>>'''

'''<< General Vars >>'''
nan_replacment = "Missing" # Placeholder for nan values
IS_TEST_MODE = False # If true - the nb would show all the plots and tests when developing.

'''<< Datasets Path Vars >>'''
data_file_prefix = "data_sets/"
data_file_name = "Marketing_Leads_India(1).csv"
data_step_1 = "step1pp.csv"
data_step_2 = "step2pp.csv"
data_step_3 = "step3pp.csv"

'''<< Models Path Vars >>'''
models_path_prefix = "models/"
imputer_model_path = "knnimputer_model.pkl"
pca_model_path = "pca_model.pkl"
ohe_path_prefix = "ohe_models/"
ohe_path_postfix = "_ohe.pkl"
onehot_models_dict = {
    "Lead Origin":"leadrigin_ohe.pkl",
    "Lead Source":"leadsource_ohe.pkl" ,
    "Country":"country_ohe.pkl",
    "Specialization": "specialization_ohe.pkl",
    "What is your current occupation":"whatisyourcurrentoccupation_ohe.pkl",
    "What matters most to you in choosing a course":"whatmattersmosttoyouinchoosingacourse_ohe.pkl",
    "Lead Profile":"leadprofile_ohe.pkl",
    "Last Notable Activity": "lastnotableactivity_ohe.pkl"   
}
lr_model_path = "lr_model.pkl"

'''<< Data Fetures >>'''
data_features = ['Lead Number', 'Lead Origin', 'Lead Source', 'Do Not Email',
       'Do Not Call', 'Converted', 'TotalVisits',
       'Total Time Spent on Website', 'Page Views Per Visit', 'Last Activity',
       'Country', 'Specialization', 'How did you hear about X Education',
       'What is your current occupation',
       'What matters most to you in choosing a course', 'Search', 'Magazine',
       'Newspaper Article', 'X Education Forums', 'Newspaper',
       'Digital Advertisement', 'Through Recommendations',
       'Receive More Updates About Our Courses', 'Tags', 'Lead Quality',
       'Update me on Supply Chain Content', 'Get updates on DM Content',
       'Lead Profile', 'City', 'Asymmetrique Activity Index',
       'Asymmetrique Profile Index', 'Asymmetrique Activity Score',
       'Asymmetrique Profile Score',
       'I agree to pay the amount through cheque',
       'A free copy of Mastering The Interview', 'Last Notable Activity']
data_features_can_nan = {'Converted','Lead Source', 'TotalVisits', 'Page Views Per Visit', 'Last Activity', 'How did you hear about X Education', 'What matters most to you in choosing a course', 'Lead Profile', 'City', 'Asymmetrique Activity Index', 'Asymmetrique Profile Index', 'Asymmetrique Activity Score', 'Asymmetrique Profile Score'}

'''<< Lead Source Vars >>'''
lead_source_option = {
    "Google",
    "Direct Traffic",
    "Olark Chat",
    "Organic Search",
    "Reference",
    "Welingak Website",
    "Referral Sites",
    "Other",
    "Facebook"
}
def_lead_source_value = "Other"
lead_source_threshold = 51


'''<< "How did you hear.." Vars >>'''
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
# TotalVisits,Page Views Per Visit == The rounded mean value of the columns.

'''<< Featuers Mod Vars (new,merge,drop..) >>'''
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

'''<< One Hot Encoding Vars >>'''
one_hot_lst = [
    "Lead Origin",
    "Lead Source",
    "Country",
    "Specialization",
    "What is your current occupation",
    "What matters most to you in choosing a course",
    "Lead Profile",
    "Last Notable Activity"]

'''<< Asymmetrique Features Vars >>'''
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