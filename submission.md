# Option B - Golden Dataset for RAG

## 5 Question-Answer Pairs

1) **Question:** In the 3Blue1Brown neural network video, what does one neuron actually calculate, and why do we need an activation function after that?  
**Answer:** A neuron takes input values, multiplies them by weights, adds a bias, and then passes that result through an activation function. The activation part is important because if every layer stayed linear, the whole network would behave like one big linear model and lose expressive power.  
**Source:** 3Blue1Brown - *But what is a Neural Network?* (section on weighted sum + activation, approx. 04:20-06:50)

2) **Question:** In simple terms, how does gradient descent help a neural network learn?  
**Answer:** Gradient descent checks how much each parameter is contributing to the loss and nudges parameters in the direction that reduces that loss. Doing this repeatedly over many training examples gradually improves predictions.  
**Source:** 3Blue1Brown - *But what is a Neural Network?* (training/backprop intuition, approx. 12:10-16:30)

3) **Question:** In the transformer video, what key issue does self-attention solve?  
**Answer:** Self-attention allows each token to look at other relevant tokens directly, even if they are far away in the sequence. This helps the model capture long-range context better than strictly local or fixed-window approaches.  
**Source:** 3Blue1Brown - *Transformers, the tech behind LLMs* (motivation for self-attention, approx. 04:30-08:20)

4) **Question:** Based on CampusX, how is deep learning different from traditional machine learning in terms of features?  
**Answer:** In traditional ML, people often design features manually. In deep learning, feature representations are learned by the network itself across layers, so less manual feature engineering is needed.  
**Source:** CampusX - *What is Deep Learning? (Hindi)* (definition and DL vs ML comparison, approx. 02:10-06:20)

5) **Question:** From CodeWithHarry's discussion, what matters most in real deep learning projects besides model choice?  
**Answer:** Data quality and quantity, consistent preprocessing, and proper evaluation setup are all critical. A strong model still performs poorly if data is noisy or testing is weak.  
**Source:** CodeWithHarry - *All About ML & Deep Learning (Hindi)* (practical workflow/pitfalls, approx. 14:20-21:40)

## Short Methodology Note

- I selected questions that test understanding, not memorization: mechanism, comparison, and practical judgment.
- I used transcript sections where the instructor clearly explains "how" or "why", then turned those points into questions.
- I kept coverage balanced: neural basics, optimization, transformers, DL vs ML, and project-level practical factors.
- I wrote short answers on purpose so each one can be checked quickly against one source segment.
- Wrong retrieval would usually look like a generic answer that uses ML words but misses the core idea (for example, mixing attention with backprop, or ignoring data quality in project outcomes).
