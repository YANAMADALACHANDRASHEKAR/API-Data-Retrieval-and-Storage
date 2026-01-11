from flask import Flask, request, Response
import sqlite3
from collections import OrderedDict
import json

app = Flask(__name__)
DB_FILE = "Books_database.db"
MAX_LIMIT = 50   # maximum records allowed

@app.route("/api/books", methods=["GET"])
def get_books():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", MAX_LIMIT))

    # Enforce maximum limit
    if limit > MAX_LIMIT:
        limit = MAX_LIMIT

    offset = (page - 1) * limit

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT
            "ISBN",
            "Book-Title",
            "Book-Author",
            "Year-Of-Publication",
            "Publisher"
        FROM Books
        LIMIT {limit} OFFSET {offset}
    """)

    rows = cursor.fetchall()
    conn.close()

    books = []
    for row in rows:
        book = OrderedDict()
        book["ID"] = row[0]
        book["Title"] = row[1]
        book["Author"] = row[2]
        book["Year"] = row[3]
        book["Publisher"] = row[4]
        books.append(book)

    result = {
        "page": page,
        "limit": limit,
        "max_limit": MAX_LIMIT,
        "count": len(books),
        "data": books
    }

    json_data = json.dumps(result, ensure_ascii=False, sort_keys=False, indent=2)
    return Response(json_data, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
