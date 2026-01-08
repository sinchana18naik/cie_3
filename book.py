def book_details(id,title,author,year):
    
        return (
            f"book_id: {id}\n"
            f"title: {title}\n"
            f"author: {author}\n"
            f"year_of_publication: {year}"
        )
if __name__ == "__main__" :
        book_id= "p101"
        title= "maths"
        author= "ashalatha"
        year= 1998
        print(book_details(id,title,author,year))