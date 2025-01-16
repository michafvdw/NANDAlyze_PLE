# NANDAlyze_PLE
Project for nursing researchers using NLP and Nanda classifications for PLE at the Hogeschool Rotterdam

## About this project 
With NANDAlyze nursing researchers will be able to translate narritives (cases, dialogues etc) into the standardized language of the NANDA-I classifications. Nurses tend to use vague or subjective language in patient documentation. To be able to compare, analyse and research nursing documentation standardized terminologies are necessary. The accuracy and agreement on nursing diagnoses varies among nurses and researchers. Nursing classifications are standardized languages which contain also a scientific knowlegde base about nursing. Examples are NANDA-I (nursing diagnosis), NOC (Nursing outcomes) and OMAHA system (problems, outcomes and interventions). NANDAlyze aims to be the first step in this project. The end goal would be for NANDAlyze to define more accurate nursing diagnoses (interoperable)



## Target Audience 
The target audience for this project are nursing researchers. They conduct research about nursing and how to improve care planning. Many nursing researchers I spoke to are specifically doing research about the NANDA-I classifications. I conducted interviews with three researchers at the HR healthcare data-lab and described their pains and gains. 

### Pains 
1) It takes too much time to read all of the data
2) The research doesn’t have a clear purpose 
3) Dataset is biased 
4) Dataset is incomplete 
5) Context gets lost 
6) Patient disagrees with analysis 

### Gains
1) Dataset is large enough
2) Two researchers or more conduct the research 
3) Conclusions are based upon NANDA classifications 
4) Data is accurately cleaned 
5) Dataset is complete
6) There is a “perfect” answer to look back at when you test the case with a NLP tool 

## Deliverables for PLE and what’s next?
This project is made for a project at the hogeschool Rotterdam called PLE (Personal Learning Environment). Next, the project will be further developed with the internship at the datalab IVG at the hogeschool Rotterdam I’m doing. In total, the project will be developed in the span of a year. I have written down for you what the Must haves, should haves, could haves and shouldn’t haves are. The must haves are what will be developed for PLE, the rest is meant for my internship. 

### Must haves
1) (One) prototype where there is an interface that meets the needs of the target audience 
2) Implemented RAG or FAISS algorithm 
3) Can look at both images or at text files to analyse 
4) Uses hugging face or Azure 
5) Uses Streamlit or a different framework for the interface 
6) Has been tested with at least one case where the desired output is known (golden standard)
7) At least one standardized prompt
8) Can choose at least two language model

### Should haves
1) Can use both images and text files (multimodality)
2) User can choose between different language models 
3) User can choose between different transformers 
4) User can choose between different tokenizers 
5) User can choose between different embedders 
6) Can use NANDA classifications 
7) Has an interface that is tested with the target audience 
8) NANDAlyze is able to clinically reason
9) Is used in a containerized and safe environment
10) Multiple standardized prompts 

### Could haves 
1) User can choose GPU heat 
2) Can choose between roles the LLM could have 

### Shouldn’t haves 

## Flowchart NANDAlyze
<img src="images/Screenshot 2025-01-09 at 12.40.20.png" width="600" alt="accessibility text">
