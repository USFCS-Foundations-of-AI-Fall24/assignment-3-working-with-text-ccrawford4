import pickle
import ollama

def build_prompt(num_words) :
    return f'Respond ONLY with a list of {num_words} words separated by commas and NOTHING ELSE'

def get_random_words(num_words, pos=False) :
    file_name = 'random_words.pkl'
    if pos :
        file_name = 'random_words2.pkl'

    with open (file_name, 'rb') as f:
        pickle_data = pickle.load(f)
        return pickle_data[num_words]

# Code to create random words in pickle files
# def get_random_words(num_words) :
#     response = ollama.chat(model='llama3.1', messages=[
#         {
#             'role': 'user',
#             'content': build_prompt(num_words)
#         }
#     ])
#     return [word.strip() for word in response['message']['content'].split(",")]

# sizes = [25, 50, 100, 500, 1000]
# data = {}
# for size in sizes:
#     data[size] = get_random_words(size)
#
# with open('random_words2.pkl', 'wb') as f:
#     pickle.dump(data, f)

