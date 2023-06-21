#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, jsonify, request
import random

app = Flask(__name__)

def read_facts_from_file():
    with open('facts.txt', 'r') as file:
        facts = file.readlines()
    return facts

facts_list = read_facts_from_file()

@app.route('/facts', methods=['GET'])
def get_random_fact():
    index = request.args.get('index')

    if index:
        try:
            fact = facts_list[int(index)]
        except IndexError:
            return jsonify({'error': 'Invalid index'}), 400
    else:
        fact = random.choice(facts_list)

    return jsonify({'fact': fact.strip()})

if __name__ == '__main__':
    app.run()


# In[ ]:




