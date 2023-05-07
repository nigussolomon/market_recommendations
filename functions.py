import pandas as pd
link = 'https://drive.google.com/uc?export=download&id=1wMkDxzmazaOe3S1X9qF73CPehsnz6a8w'
customer_data = pd.read_csv(link)

categories = ['Electronics Products', 'Beauty Products', 'Books', 'Clothing', 'Toys']
age_groups = ['Under 18', '18 - 28', '29 - 38', '39 - 48', '49 - 58', '59 above']
genders = ['Male', 'Female']

def age_group_recomendations(age_group):
    category_counts = customer_data[customer_data['AgeRange'] == age_group]['ProductCategory'].value_counts()
    if len(category_counts) == 0:
        response = f"We don't have enough data for the {age_groups[age_group - 1]} age group."
    else:
        top_category = category_counts.index[0]
        response = f"We recommend focusing marketing on {categories[top_category-1]} for the {age_groups[age_group - 1]} age group."
    return response

def gender_recomendations(gender):
    category_counts = customer_data[customer_data['Gender'] == gender]['ProductCategory'].value_counts()
    if len(category_counts) == 0:
        response = f"We don't have enough data for these {genders[gender - 1]} group."
    else:
        top_category = category_counts.index[0]
        response = f"We recommend focusing marketing on {categories[top_category-1]} for {genders[gender - 1]}s"
    return response

def age_plus_gender_recommendations(gender=None, age_group=None):
    if gender is not None and age_group is not None:
        category_counts = customer_data[(customer_data['Gender'] == gender) & (customer_data['AgeRange'] == age_group)]['ProductCategory'].value_counts()
        if len(category_counts) == 0:
            response = f"We don't have enough data for the {genders[gender - 1]}s in {age_groups[age_group - 1]} age group."
        else:
            top_category = category_counts.index[0]
            response = f"We recommend focusing marketing on {categories[top_category-1]} for {genders[gender - 1]}s in the {age_groups[age_group - 1]} age group."
    elif gender is None and age_group is not None:
        response = age_group_recomendations(age_group)
    elif gender is not None and age_group is None:
        response = gender_recomendations(gender)
    else:
        top_category = customer_data['ProductCategory'].value_counts().index[0]
        response = f"We recommend focusing marketing on {categories[top_category-1]} for our customers."
    return response

def product_category_recomendations(category):
    category_counts = customer_data[customer_data['ProductCategory'] == category]['Gender'].value_counts()
    category_counts2 = customer_data[customer_data['ProductCategory'] == category]['AgeRange'].value_counts()
    if len(category_counts) == 0 or len(category_counts2) == 0:
        response = f"We don't have enough data for the {categories[category - 1]} category."
    else:
        top_category = category_counts.index[0]
        top_category2 = category_counts2.index[0]
        response = f"We have noticed for {categories[category - 1]} the most popular denomination is, {genders[top_category - 1]}s in the {age_groups[top_category2 - 1]} age group."
    return response