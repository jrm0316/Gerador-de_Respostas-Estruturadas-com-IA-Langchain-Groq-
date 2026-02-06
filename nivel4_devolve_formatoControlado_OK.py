#Gerador-de_Respostas-Estruturadas-com-IA-Langchain-Groq-

# -*- coding: utf-8 -*-

import sys
sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["tema"],
    template="""
Responsa APENAS no formato abaixo (JSON):

{{
    
    "titulo": "...",
    "descricao": "...",
    "nivel": "iniciante | intermediario | avancado"
}}

Tema: {tema}
"""
)

prompt_final = prompt.format(tema="Python")

resposta = llm.invoke(prompt_final)

print(resposta.content)