# import os
# import reflex as rx
# from openai import OpenAI


# # Checking if the API key is set properly
# if not os.getenv("OPENAI_API_KEY"):
#     raise Exception("Please set OPENAI_API_KEY environment variable.")


# class QA(rx.Base):
#     """A question and answer pair."""

#     question: str
#     answer: str


# DEFAULT_CHATS = {
#     "Intros": [],
# }


# class State(rx.State):
#     """The app state."""

#     # A dict from the chat name to the list of questions and answers.
#     chats: dict[str, list[QA]] = DEFAULT_CHATS

#     # The current chat name.
#     current_chat = "Intros"

#     # The current question.
#     question: str

#     # Whether we are processing the question.
#     processing: bool = False

#     # The name of the new chat.
#     new_chat_name: str = ""

#     def create_chat(self):
#         """Create a new chat.

#         Example:
#             self.new_chat_name = "General"
#             self.create_chat()  # Creates a new chat named "General"
#         """
#         # Add the new chat to the list of chats.
#         self.current_chat = self.new_chat_name
#         self.chats[self.new_chat_name] = []
#         # -> None

#     def delete_chat(self):
#         """Delete the current chat.

#         Example:
#             self.current_chat = "General"
#             self.delete_chat()  # Removes the "General" chat.
#         """
#         del self.chats[self.current_chat]
#         if len(self.chats) == 0:
#             self.chats = DEFAULT_CHATS
#         self.current_chat = list(self.chats.keys())[0]
#         # -> None

#     def set_chat(self, chat_name: str):
#         """Set the name of the current chat.

#         Example:
#             self.set_chat("General")  # Sets current chat to "General"

#         Args:
#             chat_name: The name of the chat.
#         """
#         self.current_chat = chat_name
#         # -> None

#     @rx.var
#     def chat_titles(self) -> list[str]:
#         """Get the list of chat titles.

#         Example:
#             self.chats = {"Intros": [], "General": []}
#             self.chat_titles  # -> ["Intros", "General"]

#         Returns:
#             The list of chat names.
#         """
#         return list(self.chats.keys())  # -> list[str]

#     async def process_question(self, form_data: dict[str, str]):
#         """Process a question and yield its response.

#         Example:
#             form_data = {"question": "What is Reflex?"}
#             async for response in self.process_question(form_data):
#                 print(response)  # Yields responses like "Reflex is a chatbot..."

#         Args:
#             form_data: A dict containing the question.
#         """
#         # Get the question from the form
#         question = form_data["question"]

#         # Check if the question is empty
#         if question == "":
#             return  # -> None

#         model = self.openai_process_question

#         async for value in model(question):
#             yield value  # -> str (response from the OpenAI API)

#     async def openai_process_question(self, question: str):
#         """Get the response from the API.

#         Example:
#             question = "What is Reflex?"
#             async for response in self.openai_process_question(question):
#                 print(response)  # Yields streamed response chunks.

#         Args:
#             question: The question to process.
#         """
#         # Add the question to the list of questions.
#         qa = QA(question=question, answer="")
#         self.chats[self.current_chat].append(qa)

#         # Clear the input and start the processing.
#         self.processing = True
#         yield  # -> None (indicates start of processing)

#         # Build the messages.
#         messages = [
#             {
#                 "role": "system",
#                 "content": "You are a friendly chatbot named Reflex. Respond in markdown.",
#             }
#         ]
#         for qa in self.chats[self.current_chat]:
#             messages.append({"role": "user", "content": qa.question})
#             messages.append({"role": "assistant", "content": qa.answer})

#         # Remove the last mock answer.
#         messages = messages[:-1]

#         # Start a new session to answer the question.
#         session = OpenAI().chat.completions.create(
#             model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
#             messages=messages,
#             stream=True,
#         )

#         # Stream the results, yielding after every word.
#         for item in session:
#             if hasattr(item.choices[0].delta, "content"):
#                 answer_text = item.choices[0].delta.content
#                 # Ensure answer_text is not None before concatenation
#                 if answer_text is not None:
#                     self.chats[self.current_chat][-1].answer += answer_text
#                 else:
#                     # Handle the case where answer_text is None, perhaps log it or assign a default value
#                     answer_text = ""
#                     self.chats[self.current_chat][-1].answer += answer_text
#                 self.chats = self.chats
#                 yield  # -> str (streamed response chunk)

#         # Toggle the processing flag.
#         self.processing = False
#         # -> None
