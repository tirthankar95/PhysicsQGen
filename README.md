# Physics Word Problem Generation
## Folder Structure
1. **DATASET** - Contains saved physics questions generated using our method, saved by topics.
2. **ENTITY** - Each topic has an entity, which contains topic words and properties.
3. **FINE_TUNE_GPT2** - Code for finetuning GPT-2.
4. **LLM** - Contains a RAG chains to generate questions.
5. **LLM_CONFIG** - Contains config for the code to select LLMs.
   Meaning of some config variables
    - BUILD_DATASET -> Assign it to true if you are confident to save the physics questions in DATASET.
    - OPENAI_API_KEY -> API KEY for openai models
    - INNER_MODEL -> The name of the open ai model.
6. **NOVELTY_SCORE** - Code to calculate novelty scores.
7. **TOPICS** - Equations of each topic are present in this file.
8. **UTILS** -  Any utility functions.

## How to run the code
`physics.py` is the main entry point of the code. 
**To see all options on how to run the code see the image below.**
![alt text](src/options.png)

## [TBD] 
`1. Fix ln(2) and exp(...) for nuclear physics. ??`
`2. Instead of using topic words from json. Use RAG.`
`    a. Decide which Physics book should I put in RAG.`
`    b. Should I put question bank questions into RAG.`
`    c. Create a POC to see what chunks are being fetched.`
`    d. Prompt the original question + with all the variables.`
