from httpx import AsyncClient

from tests.conftest import AUTHOR_1, AUTHOR_2

AUTHOR_NONEXISTENT = "99999999-9999-9999-9999-999999999999"


async def test_get_books_returns_list(client: AsyncClient):
    response = await client.get("/api/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


async def test_create_book_returns_correct_fields(client: AsyncClient):
    payload = {
        "title": "The Great Gatsby",
        "authors": [AUTHOR_1],
        "genre": "Novel",
    }
    response = await client.post("/api/books/", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["title"] == "The Great Gatsby"
    assert data["genre"] == "Novel"
    assert AUTHOR_1 in data["authors"]


async def test_created_book_appears_in_list(client: AsyncClient):
    payload = {
        "title": "1984",
        "authors": [AUTHOR_2],
        "genre": "Dystopian",
    }
    create_resp = await client.post("/api/books/", json=payload)
    assert create_resp.status_code == 200
    created_id = create_resp.json()["id"]

    list_resp = await client.get("/api/books/")
    assert list_resp.status_code == 200
    ids = [b["id"] for b in list_resp.json()]
    assert created_id in ids


async def test_create_book_with_multiple_authors(client: AsyncClient):
    payload = {
        "title": "Co-authored Book",
        "authors": [AUTHOR_1, AUTHOR_2],
        "genre": "Fiction",
    }
    response = await client.post("/api/books/", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert len(data["authors"]) == 2
    assert AUTHOR_1 in data["authors"]
    assert AUTHOR_2 in data["authors"]


async def test_create_book_skips_nonexistent_authors(client: AsyncClient):
    """Из 3 авторов в запросе только 2 есть в БД — книга создаётся с двумя."""
    payload = {
        "title": "Book with missing author",
        "authors": [AUTHOR_1, AUTHOR_2, AUTHOR_NONEXISTENT],
        "genre": "Test",
    }
    response = await client.post("/api/books/", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert len(data["authors"]) == 2
    assert AUTHOR_NONEXISTENT not in data["authors"]


async def test_create_book_deduplicates_authors(client: AsyncClient):
    """Дублирующиеся авторы в запросе — книга создаётся с одним уникальным автором."""
    payload = {
        "title": "Book with duplicate authors",
        "authors": [AUTHOR_1, AUTHOR_1],
        "genre": "Test",
    }
    response = await client.post("/api/books/", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert len(data["authors"]) == 1
    assert AUTHOR_1 in data["authors"]
