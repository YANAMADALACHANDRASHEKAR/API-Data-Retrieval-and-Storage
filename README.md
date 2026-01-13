# API-Data-Retrieval-and-Storage
## **Overview**

The **Books API** is a RESTful service built with **Flask** and **SQLite** that retrieves book data and returns it in **JSON format**.
It supports pagination and request limits for efficient data access.

---

## **Features**

* REST API using Flask
* SQLite database integration
* Pagination (`page`, `limit`)
* Maximum limit enforcement
* JSON responses

---

## **Technology Stack**

* Python 3
* Flask
* SQLite

---

## **Project Structure**

```
books.py
Books_database.db
README.md
```

---

## **Setup & Run**

1. Install Flask:

```
pip install flask
```

2. Run the application:

```
python books.py
```

API runs at:

```
http://127.0.0.1:5000/api/books
```

---

## **API Endpoint**

### Get Books

```
GET /api/books
```

**Query Parameters**

| Name  | Default | Description               |
| ----- | ------- | ------------------------- |
| page  | 1       | Page number               |
| limit | 50      | Records per page (max 50) |

---

## **Sample Response**

```json
{
  "page": 1,
  "limit": 10,
  "count": 10,
  "data": [
    {
      "ID": "9780131103627",
      "Title": "The C Programming Language",
      "Author": "Brian W. Kernighan",
      "Year": 1978,
      "Publisher": "Prentice Hall"
    }
  ]
}
```

---

## **Database Schema**

| Column              | Description |
| ------------------- | ----------- |
| ISBN                | Book ID     |
| Book-Title          | Title       |
| Book-Author         | Author      |
| Year-Of-Publication | Year        |
| Publisher           | Publisher   |

---

