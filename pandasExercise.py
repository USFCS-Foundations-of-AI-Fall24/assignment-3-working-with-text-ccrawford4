import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def chapter_one(data_frame) :
    return data_frame['class']

def chapter_two(data_frame) :
    def count(df, key, value):
        return df[key].value_counts()[value]

    def calculate_prop(df, key, value):
        return count(df, key, value) / len(df)

    recurrence_prop = calculate_prop(data_frame, 'class', 'recurrence-events')
    no_recurrence_prop = calculate_prop(data_frame, 'class', 'no-recurrence-events')
    if recurrence_prop > no_recurrence_prop:
        return "recurrence-events", recurrence_prop
    return "no-recurrence-events", no_recurrence_prop

def chapter_three(data_frame) :
    filtered_rows = data_frame[data_frame['class'] == 'recurrence-events']
    most_common_age = filtered_rows['age'].mode()[0]
    most_common_menopause = filtered_rows['menopause'].mode()[0]
    return most_common_age, most_common_menopause

def chapter_four(data_frame) :
    recurrence_df = data_frame[data_frame['class'] == 'recurrence-events']
    age_counts = recurrence_df['age'].value_counts().sort_index()

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=age_counts.index, y=age_counts.values, palette="Blues_d")
    plt.title("Number of Recurrences for Each Age Group", fontsize=16)
    plt.xlabel("Age Group", fontsize=12)
    plt.ylabel("Number of Recurrences", fontsize=12)

    # Show the plot
    plt.show()
    return

def print_results(chapter_name, function, df) :
    print(chapter_name + ": ")
    print(function(df))

if __name__ == '__main__':
    column_names = ['class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']
    df = pd.read_csv('breast-cancer.data', names=column_names)
    results = {
        "Chapter 1":  chapter_one,
        "Chapter 2": chapter_two,
        "Chapter 3": chapter_three,
        "Chapter 4": chapter_four
    }
    for name, value in results.items():
        print_results(name, value, df)
