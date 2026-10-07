import pandas as pd

data = pd.read_csv("../Survey-Survey.csv", encoding="latin1")

# =============================
# DEMOGRAPHIC DATA CLEANING
# ==============================

# gender 0== male, 1== female

data["gender"] = data["Your gender"].map({
    "Male": 0,
    "Female": 1
})
data["gender"].attrs["description"] = "What is your Gender (0 = Male, 1 = Female)"


# Living with family: 0== No, 1== Yes
data["family"] = data["Living with family?"].map({
    "No": 0,
    "Yes": 1
})
data["family"].attrs["description"] = "Living with family (0 = No, 1 = Yes)"

# ===============================
# ACADEMIC FACTORS
# =============================

data["acad_condition"] = data["Are you happy with your academic Condition?"].map({
    "No": 0,
    "Yes": 1
})
data["acad_condition"].attrs["description"] = (
    "Are you happy with your academic Condition? (0 = No, 1 = Yes)"
)

# ======================
# SOCIAL FACTORS
# ======================

data["addict_drug"] = data["Are you addicted to any drugs?"].map({
    "No": 0,
    "Yes": 1
})
data["addict_drug"].attrs["description"] = "Are you addicted to any drugs? (0 = No, 1 = Yes)"


data["addict_sm"] = data["Are you addicted to social media?"].map({
    "No": 0,
    "Yes": 1
})
data["addict_sm"].attrs["description"] = "Are you addicted to social media? (0 = No, 1 = Yes)"


data["relationship"] = data["Are you in a relationship?"].map({
    "No": 0,
    "Yes": 1
})
data["relationship"].attrs["description"] = "Are you in a relationship? (0 = No, 1 = Yes)"


data["breakup"] = data["did you have a recent breakup?"].map({
    "No": 0,
    "Yes": 1
})
data["breakup"].attrs["description"] = "Did you have a recent breakup? (0 = No, 1 = Yes)"


data["conflict_friend"] = data["How often do you conflict with your friend?"].map({
    "Never occurs": 0,
    "Someimes": 1,
    "Most of the time": 2,
})
data["conflict_friend"].attrs["description"] = (
    "How often do you conflict with your friend? (0 = Never occurs, 1 = Someimes, 2 = Most of the time)"
)

data["finproblem_family?"] = data["Do you have financial problem in your family?"].map({
    "No": 0,
    "Yes": 1
})
data["finproblem_family?"].attrs["description"] = "Do you have financial problem in your family? (0 = No, 1 = Yes)"


data["violence_fam"] = data["Violence in family?"].map({
    "Never": 0,
    "Rarely": 1,
    "Often": 2,
    "Most of the time": 3,
})
data["violence_fam"].attrs["description"] = "Violence in family? (0 = Never, 1 = Rarely, 2 = Often, 3 = Most of the time)"


data["bullied"] = data["Have you ever been bullied"].map({
    "No": 0,
    "Yes": 1
})
data["bullied"].attrs["description"] = "Have you ever been bullied? (0 = No, 1 = Yes)"



data["sex_abuse"] = data["Have you ever been sexually harassed or abused"].map({
    "No": 0,
    "Maybe": 1,
    "Yes": 2
})
data["sex_abuse"].attrs["description"] = "Have you ever been sexually harassed or abused? (0 = No, 1 = Maybe, 2 = Yes)"


