# Importing the pandas library for data manipulation
import pandas as pd

# Setting the link to the dataset
link = 'https://drive.google.com/uc?export=download&id=1wMkDxzmazaOe3S1X9qF73CPehsnz6a8w'

# Reading the dataset using pandas and storing it in a variable called "customer_data"
customer_data = pd.read_csv(link)

# Creating a list of product categories, age groups, genders
categories = ['Electronics Products', 'Beauty Products', 'Books', 'Clothing', 'Toys']
age_groups = ['Under 18', '18 - 28', '29 - 38', '39 - 48', '49 - 58', '59 above']
genders = ['Male', 'Female']


def age_group_recomendations(age_group):
    # Select the rows from the customer_data DataFrame where the AgeRange column matches the input age_group
    # and count the number of purchases made in each product category for that age group
    category_counts = customer_data[customer_data['AgeRange'] == age_group]['ProductCategory'].value_counts()
    
    # If there are no purchases made in any product category for the given age group
    if len(category_counts) == 0:
        # Return a message indicating that there is not enough data available for that age group
        response = f"We don't have enough data for the {age_groups[age_group - 1]} age group."
    # If there are purchases made in at least one product category for the given age group
    else:
        # Determine which product category has the highest number of purchases for that age group 
        # using the index of the Series returned by value_counts()
        top_category = category_counts.index[0]
        # Return a recommendation to focus marketing efforts on that product category for that age group
        response = f"We recommend focusing marketing on {categories[top_category-1]} for the {age_groups[age_group - 1]} age group."
    # Return a tuple containing the recommendation message and a None value
    return response


def gender_recomendations(gender):
    # Select the rows from the customer_data DataFrame where the Gender column matches the input gender
    # and count the number of purchases made in each product category for that gender
    category_counts = customer_data[customer_data['Gender'] == gender]['ProductCategory'].value_counts()
    
    # If there are no purchases made in any product category for the given gender
    if len(category_counts) == 0:
        # Return a message indicating that there is not enough data available for that gender
        response = f"We don't have enough data for these {genders[gender - 1]} group."
    # If there are purchases made in at least one product category for the given gender
    else:
        # Determine which product category has the highest number of purchases for that gender
        # using the index of the Series returned by value_counts()
        top_category = category_counts.index[0]
        # Return a recommendation to focus marketing efforts on that product category for that gender
        response = f"We recommend focusing marketing on {categories[top_category-1]} for {genders[gender - 1]}s"
    # Return a tuple containing the recommendation message and a None value
    return response


def age_plus_gender_recommendations(gender=None, age_group=None):
    # If both gender and age_group are specified
    if gender is not None and age_group is not None:
        # Filter data by gender and age_group and count occurrences of each product category
        category_counts = customer_data[(customer_data['Gender'] == gender) & (customer_data['AgeRange'] == age_group)]['ProductCategory'].value_counts()
        # If there is no data for the specified gender and age group
        if len(category_counts) == 0:
            response = f"We don't have enough data for the {genders[gender - 1]}s in {age_groups[age_group - 1]} age group."
        else:
            # Get the most popular category for the specified gender and age group
            top_category = category_counts.index[0]
            response = f"We recommend focusing marketing on {categories[top_category-1]} for {genders[gender - 1]}s in the {age_groups[age_group - 1]} age group."
    # If only age_group is specified
    elif gender is None and age_group is not None:
        # Call age_group_recomendations function to get recommendation based on age group
        response = age_group_recomendations(age_group)
    # If only gender is specified
    elif gender is not None and age_group is None:
        # Call gender_recomendations function to get recommendation based on gender
        response = gender_recomendations(gender)
    # If neither gender nor age_group is specified
    else:
        # Get the most popular category among all customers
        top_category = customer_data['ProductCategory'].value_counts().index[0]
        response = f"We recommend focusing marketing on {categories[top_category-1]} for our customers."
    return response


def product_category_recomendations(category):
    # Filter data for given product category and get count of genders and age ranges
    category_counts_gender = customer_data[customer_data['ProductCategory'] == category]['Gender'].value_counts()
    category_counts_age_group = customer_data[customer_data['ProductCategory'] == category]['AgeRange'].value_counts()
    # If there is not enough data for given category, return error message
    if len(category_counts_gender) == 0 or len(category_counts_age_group) == 0:
        response = f"We don't have enough data for the {categories[category - 1]} category."
    else:
        # Get the most popular gender and age range for given category
        top_category = category_counts_gender.index[0]
        top_category2 = category_counts_age_group.index[0]
        # Return recommendation message based on most popular gender and age range
        response = f"We have noticed for {categories[category - 1]} the most popular denomination is, {genders[top_category - 1]}s in the {age_groups[top_category2 - 1]} age group."
    return response