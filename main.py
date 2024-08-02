import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
import pandas as pd

# load .env
load_dotenv()

# dataframe
input_datapath = "Reviews.csv"  # to save space, we provide a pre-filtered dataset
df = pd.read_csv(input_datapath, index_col=0)
df = df[["Time", "ProductId", "UserId", "Score", "Summary", "Text"]]
df = df.dropna()
df["combined"] = (
    "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
)
print(df.head(2))

# print("\nOpenAI\n")
# client = OpenAI()
#
# # completion = client.chat.completions.create(
# #   model="gpt-4o-mini",
# #   messages=[
# #     {"role": "system", "content": "Answer in a consistent sytle."},
# #     {"role": "user", "content": "Teach me about patience."},
# #     {"role": "assistant", "content": "You wait like a really long time and then sometimes good things happen."},
# #     {"role": "user", "content": "Teach me about the ocean."}
# #   ]
# # )
#
# def get_embedding(text, model="text-embedding-3-small"):
#    text = text.replace("\n", " ")
#    return client.embeddings.create(input = [text], model=model).data[0].embedding
#
# df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
# df.to_csv('output/embedded_1k_reviews.csv', index=False)
#
# for messages in completion.choices:
#     print(messages.message.content)
#
# # Anthropic
#
# # print("\nAnthropic\n")
# # client = anthropic.Anthropic()
# # message = client.messages.create(
# #     model="claude-3-5-sonnet-20240620",
# #     max_tokens=1024,
# #     messages=[
# #         {"role": "user", "content": "Hello, Claude"}
# #     ]
# # )
# # print(message.content)
