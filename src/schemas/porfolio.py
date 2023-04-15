def porfolioEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name": str(["name"]),
        "description": str(["description"]),
        "title": str(["title"]),
        "email": str(["email"]),
        "phone": str(["phone"]),
        "location": str(["location"]),
    }   