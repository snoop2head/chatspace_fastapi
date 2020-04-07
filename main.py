from fastapi import FastAPI
from datetime import date
from chatspace import ChatSpace

# today's date
today_int = date.today()
print("test_app - Today's date:", today_int)

# Initializing Fast API
app = FastAPI()

# Load ChatSpace
spacer = ChatSpace()


@app.get("/")
def read_root():
    return {"connection": True}


@app.get("/proofread/{text}")
def sentence_proofreader(text: str, q: str = None):
    proofreaded = {"success": False}
    spaced_text = spacer.space(text)
    proofreaded["success"] = True
    proofreaded["spaced_text"] = spaced_text
    print(proofreaded)
    return proofreaded
