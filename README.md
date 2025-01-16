# NANDAlyze_PLE
Project for nursing researchers using NLP and Nanda classifications for PLE at the Hogeschool Rotterdam

## About this project 
With NANDAlyze nursing researchers will be able to translate narritives (cases, dialogues etc) into the standardized language of the NANDA-I classifications. Nurses tend to use vague or subjective language in patient documentation. To be able to compare, analyse and research nursing documentation standardized terminologies are necessary. The accuracy and agreement on nursing diagnoses varies among nurses and researchers. Nursing classifications are standardized languages which contain also a scientific knowlegde base about nursing. Examples are NANDA-I (nursing diagnosis), NOC (Nursing outcomes) and OMAHA system (problems, outcomes and interventions). NANDAlyze aims to be the first step in this project. The end goal would be for NANDAlyze to define more accurate nursing diagnoses (interoperable)



## Target Audience 
The target audience for this project are nursing researchers. They conduct research about nursing and how to improve care planning. Many nursing researchers I spoke to are specifically doing research about the NANDA-I classifications. I conducted interviews with three researchers at the HR healthcare data-lab and described their pains and gains. 

### Pains

1. **It takes too much time to read all of the data**  
   - Example:  
     A nursing researcher is analyzing electronic health records (EHR) to identify patterns in patient symptoms related to anxiety. The dataset includes over 50,000 patient entries, making it difficult to manually identify trends. Consequently, progress is slow, and insights are delayed.

2. **The research doesn’t have a clear purpose**  
   - Example:  
     A team conducts a study on nursing interventions but fails to define whether they aim to assess the effectiveness of interventions, improve nursing education, or develop new guidelines. This lack of focus results in inconclusive findings and difficulty publishing the study.

3. **Dataset is biased**  
   - Example:  
     Researchers analyzing NANDA diagnoses for elderly care notice that the dataset primarily includes data from urban hospitals, underrepresenting rural settings. As a result, the conclusions drawn are less applicable to rural healthcare environments.

4. **Dataset is incomplete**  
   - Example:  
     A study aiming to evaluate the prevalence of specific NANDA classifications in oncology care lacks records for patients in outpatient chemotherapy settings, leading to gaps in the analysis and skewed findings.

5. **Context gets lost**  
   - Example:  
     While analyzing notes on nursing diagnoses, researchers use an AI model to summarize data. However, the AI strips away essential context, such as the timeline of symptom progression, making the summaries insufficient for drawing accurate conclusions.

6. **Patient disagrees with analysis**  
   - Example:  
     A study on depression-related diagnoses employs sentiment analysis to evaluate patient narratives. A patient disputes the diagnosis, arguing that their feelings were misrepresented due to the limitations of the analysis tool.

---

### Gains

1. **Dataset is large enough**  
   - Example:  
     Researchers studying chronic pain interventions access a comprehensive dataset of 200,000 patient records from multiple healthcare settings, enabling them to identify robust trends and correlations.

2. **Two researchers or more conduct the research**  
   - Example:  
     Two nursing researchers collaborate on an analysis of maternal health NANDA classifications. One focuses on data cleaning and preparation, while the other focuses on validating results, ensuring better accuracy and reduced errors.

3. **Conclusions are based upon NANDA classifications**  
   - Example:  
     A study evaluating nursing interventions for cardiac patients uses NANDA classifications to categorize symptoms and nursing actions, ensuring the findings are easily applicable to clinical practice.

4. **Data is accurately cleaned**  
   - Example:  
     During research on diabetes-related care plans, a dedicated data scientist ensures that all duplicate records, irrelevant fields, and inconsistent entries are removed or corrected, resulting in precise analysis.

5. **Dataset is complete**  
   - Example:  
     A study on pressure ulcers includes patient data from all hospital units (ICU, inpatient, outpatient), ensuring no critical population is excluded, leading to comprehensive insights.

6. **There is a “perfect” answer to look back at when you test the case with a NLP tool**  
   - Example:  
     Researchers use a gold-standard annotated dataset for pneumonia-related nursing diagnoses to validate their NLP model. This ensures that the model’s predictions are benchmarked against highly accurate and reliable data.


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
9) Is used in a containerized and safe environment

### Should haves
1) Can use both images and text files (multimodality)
2) User can choose between different language models 
3) User can choose between different transformers 
4) User can choose between different tokenizers 
5) User can choose between different embedders 
6) Can use NANDA classifications 
7) Has an interface that is tested with the target audience 
8) NANDAlyze is able to clinically reason
9) Multiple standardized prompts 

### Could haves 
1) User can choose GPU heat 
2) Can choose between roles the LLM could have 

### Shouldn’t haves 
1) The interface should not be overly complex or require extensive training for the target audience to use effectively.
2) The system should not make clinical decisions autonomously without the ability for human oversight or intervention.
3) The AI should not use language models or data sources that are not validated for clinical applications.
4) The solution should not ignore NANDA classifications when generating diagnostic suggestions.
5) The interface should not limit accessibility for the target audience (e.g., requiring high-end hardware or software).
6) The system should not allow unrestricted or unauthorized access to sensitive data.
7) The AI should not operate without logging its reasoning or steps for auditability and transparency.
8) The application should not rely on a single language model or framework, ensuring flexibility and adaptability.
9) The tool should not force users into rigid workflows that do not align with clinical reasoning practices.
10) The system should not generate output in languages that are unsupported by the target audience or application.


## Flowchart NANDAlyze
### Flowchart 1 
This is the flowchart I made for the presentation I did for the international team of nursing researchers. It's supposed to illustrate what happens in the process from going from input to output. <br></br>
<img src="images/Screenshot 2025-01-09 at 12.40.20.png" width="600" alt="accessibility text">

## Flowchart 2
I got some feedback from researchers about this flowchart. The input (that's multimodal) should be multiple seperate layers. In this case I used both images and text files as an example but it could also be used with audio files. Also, there are two output layers: the "answer" and the answer with the NANDA classifications. I added this in my final version. 
<img src="images/Screenshot 2025-01-16 at 16.47.36.png" width="600" alt="accessibility text">
