from fastapi import FastAPI
#from pydantic import BaseModel

bot = FastAPI()

# @bot.get ("/listing/{listing_id}")
# def get_listing(listing_id: int):
#     return {"item_number": listing_id}
# @bot.get("/results")
# def search_lists(movie: str):
#     return {"searching movie is": movie}
# class Listing(BaseModel):
#     name: str
#     city: str
#     price: float

# @bot.put("/listing/{listing_id}")
# def update_list(listing_id: int, listing: Listing):
#     return {"massage": f"Listing {listing_id} updated !", "new_data": listing}
# @bot.delete("/listing/{listing_id}")
# def delet_listing(listing_id: int):
#     return {"massage": f"Listing {listing_id} deleted !"}



