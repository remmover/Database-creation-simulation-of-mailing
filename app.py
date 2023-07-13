import redis
from mongoengine import connect
from models import Author, Quote
from redis_lru import RedisLRU

connect(
    db="mein",
    host="mongodb+srv://remmover:******@cluster0.uhuxtdj.mongodb.net/?retryWrites=true&w=majority"
)

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def search_quotes_by_author(author_name):
    author = Author.objects(fullname__istartswith=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return quotes
    else:
        return []


@cache
def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags__icontains=tag)
    return quotes


@cache
def search_quotes_by_tags(tags):
    tags_list = [tag.strip() for tag in tags.split(',')]
    quotes = Quote.objects(tags__in=tags_list)
    return quotes


def print_quotes(quotes):
    for quote in quotes:
        print(quote.quote)


def main():
    while True:
        command = input("Enter a command: ")
        parts = command.split(':')
        action = parts[0].strip()
        value = parts[1].strip() if len(parts) > 1 else None

        match action:
            case 'name':
                quotes = search_quotes_by_author(value)
                print_quotes(quotes)
            case 'tag':
                quotes = search_quotes_by_tag(value)
                print_quotes(quotes)
            case 'tags':
                quotes = search_quotes_by_tags(value)
                print_quotes(quotes)
            case 'exit':
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == '__main__':
    main()
