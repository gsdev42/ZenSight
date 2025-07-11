# 🧘 ZensightAI  
### *Clarity Through Conversation*  

![ZensightAI Banner](https://static.vecteezy.com/system/resources/previews/023/522/160/original/mindfulness-logo-design-suitable-for-therapy-and-counseling-services-vector.jpg)  

> **"Your mind is a garden. Let’s tend it together."**  
> An AI companion for mindful reflection and emotional balance.  

---

## ✨ **Why ZensightAI?**  
- **Judgment-free zone** – Share freely, anytime  
- **Science-backed tools** – CBT, DBT, and mindfulness techniques  
- **Personalized insights** – Learns your emotional patterns  

---

## 🛠️ **Built With**  

### **AI Core**  
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-00A67E?logo=langchain&logoColor=white)  
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white) ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?logo=huggingface&logoColor=black)  

### **Frontend & Deployment**  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)  

### **Development Tools**  
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) ![VSCode](https://img.shields.io/badge/VSCode-007ACC?logo=visual-studio-code&logoColor=white)  

---

## 🎯 **Key Features**  

| **Feature**               | **Tech Stack**          | **Impact** |  
|---------------------------|-------------------------|------------|  
| **Contextual Responses**  | Groq LLM + Pinecone     | Low-latency, high-relevance answers |  
| **Medical Q&A**           | RAG Pipeline            | Citations from uploaded PDFs |  
| **Conversation Memory**   | Pinecone Vector Store   | Personalized follow-ups |  
| **Real-Time Processing**  | Groq LPU Inference      | 200+ tokens/sec response speed |  

### **Architecture Highlights**  
### **Architecture Diagram**
```mermaid
graph TD
    A[User Query] --> B{Query Understanding}
    B --> C[Pinecone VectorDB]
    C -->|Retrieve Relevant Chunks| D[Groq LLM]
    D --> E[Generate Augmented Response]
    E --> F[User]

    subgraph RAG Pipeline
        B
        C
        D
    end

    style A fill:#FFD166,stroke:#333
    style F fill:#FFD166,stroke:#333
    style C fill:#06D6A0,stroke:#333
    style D fill:#118AB2,stroke:#333

```

## 🌱 **Core Philosophies**  
1. **Privacy First** – All chats are encrypted  
2. **Non-Replacement** – Always suggests human help when needed  
3. **Progress Tracking** – Mood timeline visualization  

---

## 🚀 **Quick Start**  
```bash
git clone https://github.com/yourrepo/zensightai.git  
cd zensightai  
pip install -r requirements.txt  
streamlit run app/app.py  