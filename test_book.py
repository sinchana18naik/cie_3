from book import book_details

def test_book_details():
    excepted_output =(
        "book_id: p101\n"
        "title: maths\n"
        "author: ashalatha\n"
        "year_of_publication: 1998"
    )
    assert book_details("p101" , "maths", "ashalatha" ,1998) == excepted_output