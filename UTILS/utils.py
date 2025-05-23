import numpy as np
import json
import logging
from collections import defaultdict
import json 
import os 

def fix(no, number_type="R"):
    '''
    If the number is less than 10^5 and greater than equal 10^-1 
    then we round it to 2 decimal places 
    else we convert it to scientific notation.
    '''
    if no == 0: return 0
    if number_type == "Z": return int(no)
    exponent = int(np.log10(abs(no)))
    if 0 <= exponent < 5: return round(no, 2)
    return f"{no:.2e}"

def load_env_vars():
    with open("LLM_CONFIG/config.json", "r") as file:
        env = json.load(file)
    for k, v in env.items():
        if k[-3:] == "KEY" or k[-5:] == "TOKEN":
            os.environ[k] = v 

operators = ['+', '*', '=', '/', '^', '(', ')', '-']

def parse(equation):
    elements_ = [var for var in equation.split(' ') if var not in operators and len(var.strip()) > 0]
    elements = []
    for x in elements_:
        try: var = float(x)
        except: elements.append(x)
    return elements

class GraphEquation:
    def __init__(self, equations):
        self.equation_element = []
        for equation in equations:
            self.equation_element.append(parse(equation))
        N = len(self.equation_element)
        self.adj = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if i == j: continue 
                allEdges = [(j, ch) for ch in set(self.equation_element[i]).intersection(set(self.equation_element[j]))]
                self.adj[i].extend(allEdges)
    def getEquation(self):
        qid = np.random.randint(len(self.adj))
        threshold, eqn = 0.25, [qid]
        self.vis, unk = defaultdict(bool), defaultdict(bool)
        self.qu = [qid]
        self.vis[qid] = True 
        while len(self.qu):
            src = self.qu.pop(0)
            if 0.5 + np.random.normal() >= threshold:
                edgeId = np.random.randint(len(self.adj[src]))
                edge = self.adj[src][edgeId]
                if edge[-1] in unk: break
                if edge[0] not in self.vis:
                    unk[edge[-1]] = True 
                    eqn.append(edge[0])
                    self.qu.append(edge[0])
                    self.vis[edge[0]]
        while True:
            ch = np.random.choice(self.equation_element[eqn[-1]])
            if ch not in unk: break 
        unk[ch] = True
        assert len(unk) == len(eqn), f'Bad Equation: {unk} {eqn}'
        known = defaultdict(bool)
        for eId in eqn:
            for ch in self.equation_element[eId]:
                if ch not in unk:
                    known[ch] = True 
        unk, known = [k for k in unk.keys()], [k for k in known.keys()]
        logging.debug(f'{unk}, {known}')
        return unk, known, eqn
    
class Env:
    def __init__(self, filename):
        with open(f"ENTITY/{filename}", "r") as file:
            self.data = json.load(file)
            self.envs = [k for k in self.data]
            self.prefix = "Give me a physics question using the following variables and words.\n\n"    
    def get_topic_words(self):
        units = []
        if len(self.data) == 0: return self.prefix, units
        env = self.envs[np.random.randint(len(self.data))]
        topic_words = f"You may use the following environment - {env}, and it's properties and topic words - "
        if len(self.data[env]["topic_words"]):
            topic_words += np.random.choice(self.data[env]["topic_words"]) + ", "
        two_d = True if np.random.normal() >= -0.5 else False # (1: Enable, 0: Disbale) 2D
        for attribute, v in self.data[env].items():
            # An attribute can be skipped or not to increase the variability.
            if attribute == "topic_words" or np.random.normal() > 0: continue 
            v_range, unit, type, number_type = v 
            type = 0 if type == "S" else 1 # (0: scaler, 1: vector)
            var = fix(np.random.uniform(v_range[0], v_range[1]), \
                      number_type=number_type)
            if two_d and type == 1: 
                theta = np.random.randint(0, 180)
                topic_words += f"{env} {attribute} = {var} {unit} at an angle {theta} degrees with the horizontal, "
            else:
                topic_words += f"{env} {attribute} = {var} {unit}, "
            if unit not in units: units.append(unit)
        return self.prefix + " " + topic_words[:-2]+".", units
    
if __name__ == '__main__':
    obj_env = Env("env_sm.json")
    topic_words, units = obj_env.get_topic_words()
    print(topic_words, units)