from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id (
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={
        "device_map": "auto"
    },
    pipeline_kwargs=dict(
        max_new_tokens = 512,
        do_samples = False,
        repetition_penalty = 1.03       
   )
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("Explain My Name Meaning")
print(response.content)