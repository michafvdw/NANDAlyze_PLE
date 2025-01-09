# NANDAlyze_PLE
Project for nursing researchers using NLP and Nanda classifications for PLE at the Hogeschool Rotterdam

NANDAlyze

About this project 
With NANDAlyze nurses will be able to be better at assigning the right diagnosis to patients. The workload for nurses is often very high. With an administrative burden there is less time to work one on one with the patient and carefully analyse all the symptoms they are experiencing. These symptoms might get overlooked and could lead to a faulty diagnosis. NANDAlyze aims to be the first step to solve this problem. If you look at both the ERF (electronic patient file) and the conversations between patient and nurse, is there information that is missed? The end goal would be for NANDAlyze to be able to clinically reason. 

Target Audience 
The target audience for this project are nursing researchers. They conduct research about nurses and the healthcare field. Often this focuses on how to better the healthcare system. Many nursing researchers I spoke to are specifically doing research about the NANDA classifications. I conducted interviews with three researchers at the IVG lab and described their pains and gains. 

Pains 
It takes too much time to read all of the data
The research doesn’t have a clear purpose 
Dataset is biased 
Dataset is incomplete 
Context gets lost 
Patient disagrees with analysis 

Gains
Dataset is large enough
Two researchers or more conduct the research 
Conclusions are based upon NANDA classifications 
Data is accurately cleaned 
Dataset is complete
There is a “perfect” answer to look back at when you test the case with a NLP tool 

Deliverables for PLE and what’s next?
This project is made for a project at the hogeschool Rotterdam called PLE (Personal Learning Environment). Next, the project will be further developed with the internship at the datalab IVG at the hogeschool Rotterdam I’m doing. In total, the project will be developed in the span of a year. I have written down for you what the Must haves, should haves, could haves and shouldn’t haves are. The must haves are what will be developed for PLE, the rest is meant for my internship. 

Must haves
(One) prototype where there is an interface that meets the needs of the target audience 
Implemented RAG or FAISS algorithm 
Can look at either images or at text files to analyse 
Uses hugging face or Azure 
Uses Streamlit or a different framework for the interface 
Has been tested with at least one case where the desired output is known 
User is able to write a prompt to ask the NLP tool 
Can choose at least one language model

Should haves
Can use both images and text files (multimodality)
User can choose between different language models 
User can choose between different transformers 
User can choose between different tokenizers 
User can choose between different embedders 
Can upload and use NANDA classifications 
Has an interface that is tested with the target audience 
NANDAlyze is able to clinically reason
Is used in a containerized and safe environment 

Could haves 
User can choose GPU heat 
Can choose between roles the LLM could have 

Shouldn’t haves 

Flowchart NANDAlyze

