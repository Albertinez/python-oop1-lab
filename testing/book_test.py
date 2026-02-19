from lib.book import Book

def test_turn_page():
    b = Book("Python Basics", 100)
    b.turn_page()  # Should print message
    assert b.page_count == 100
