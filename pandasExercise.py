import pandas as pd
import numpy as np

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
    # Determine the most common value for age and menopause for patients
    # with recurrences
    best = df['class'].get('recurrence-events')
    print(best)


def print_results(chapter_name, function, df) :
    print(chapter_name + ": ")
    print(function(df))

if __name__ == '__main__':
    column_names = ['class', 'age', 'Menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']
    df = pd.read_csv('breast-cancer.data', names=column_names)
    results = {
        "Chapter 1": chapter_one,
        "Chapter 2": chapter_two,
        "Chapter 3": chapter_three,
    }
    for name, value in results.items():
        print_results(name, value, df)
