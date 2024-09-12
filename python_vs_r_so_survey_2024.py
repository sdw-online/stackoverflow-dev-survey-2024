import pandas as pd
import matplotlib.pyplot as plt 


"""
Workflow

1. Load data into dataframe
2. Count the number of users for Python and R
3. Create bar chart to compare tools 
4. Customize the bar chart 
5. Display the bar chart + results 

"""


# 1.
df = pd.read_csv("survey_results_public.csv")


# 2. 
python_users = df['LanguageHaveWorkedWith'].str.contains('Python', na=False).sum()
r_users = df['LanguageHaveWorkedWith'].str.contains('R', na=False).sum()


# 3. 
languages = ['Python', 'R']
users = [python_users, r_users]
colours = ['#1de044', '#1d44e0']


plt.figure(figsize=(10, 6))
plt.bar(languages, users, color=colours)



# 4. 
plt.title('Which is more popular - Python vs R? (StackOverflow Dev Survey 2024)')
plt.xlabel('Programming Language', fontsize=12)
plt.ylabel('No of users', fontsize=12)


for idx, v in enumerate(users):
    plt.text(idx, v, str(v), ha='center', va='bottom')


# 5. 
plt.tight_layout()
plt.show()


print(f"No of Python users: {python_users}")
print(f"No of R users: {r_users}")
