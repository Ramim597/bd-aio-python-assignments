# Q2: Create a class Book with the following attributes:
# - title
# - author
# - list of reviews

# And add methods to:
# - add a new review
# - count reviews
# - display all reviews


class Book:
    def __init__(self, title, author, list_of_reviews, count):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews
        self.count = count

    def add_new_review(self, new_review):
        self.list_of_reviews.append(new_review)
        self.count += 1

    def count_reviews(self):
        print(f"total reviews = {self.count}")

    def display_all_reviews(self):
        review_num = 1
        for all_reviews in self.list_of_reviews:
            print(review_num, all_reviews)
            review_num += 1


auth1 = Book("Outliers", "Paul Graham", ["Good job"], 1)
auth1.add_new_review("this is awesome")
auth1.add_new_review("book is good")
auth1.count_reviews()
auth1.display_all_reviews()
