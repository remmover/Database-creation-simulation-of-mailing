from mongoengine import connect, MultipleObjectsReturned

from models import Author, Quote
import json

connect(
    db="mein",
    host="mongodb+srv://remmover:******@cluster0.uhuxtdj.mongodb.net/?retryWrites=true&w=majority"
)


def load_data_from_json(json_file):
    with open(json_file, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def save_authors_to_database(authors):
    Author.objects().delete()
    try:
        for author in authors:
            Author(
                fullname=author["fullname"],
                born_date=author["born_date"],
                born_location=author["born_location"],
                description=author["description"],
            ).save()
        print("Authors data loaded successfully.")
    except Exception as e:
        print(f"Error loading quotes data: {str(e)}")


def save_quotes_to_database(quotes):
    Quote.objects().delete()
    try:
        for quote in quotes:
            try:
                author = Author.objects.get(fullname=quote["author"])
            except MultipleObjectsReturned:
                continue

            Quote(tags=quote["tags"], author=author, quote=quote["quote"]).save()

        print("Quotes data loaded successfully.")
    except Exception as e:
        print(f"Error loading quotes data: {str(e)}")


if __name__ == "__main__":
    authors_json_file = "data/authors.json"
    quotes_json_file = "data/quotes.json"

    authors_data = load_data_from_json(authors_json_file)
    quotes_data = load_data_from_json(quotes_json_file)

    save_authors_to_database(authors_data)
    save_quotes_to_database(quotes_data)
