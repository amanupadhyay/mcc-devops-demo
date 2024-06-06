from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"msg": "About Us"}

@app.get("contact-us")
def contact_us():
    return {"email": "aman@example.com", "phone": "5647823455"}