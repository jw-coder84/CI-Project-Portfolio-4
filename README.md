# **_Book Central - Portfolio Project 4_**

The purpose of this website is to provide a library with an online management system. Using this website, users can browse the selection of available books, view the details of each book and check them out for borrowing. Admin users can create, update and delete records. They can also view a list of books on loan with the corresponding user they are on loan with, and the date the book is due to be returned. 

![Responsive image](static/readme/responsive-view.png)

## [View deployed website](https://library-m-system.herokuapp.com/)


# User Experience
## User Stories
I used a Github kanban board with issues to represent individual tasks of my project that will make up my website.
The following objectives were created from admin and user perspectives.

- As a **Site User** I can **register an account** so that **I can view the selection of books and choose one to borrow**
- As a **Site User** I can **view a paginated list of books** so that **I can select a book to view it's details**
- As a **Site User** I can **click a book link** so that **I can view details about the book such as the plot description**
- As a **Site User** I can **check out a book** so that **I can borrow it to read**
- As a **Site User** I can **view a list of the books I have checked out** so that **I can track the number of books and the return dates**
- As a **Site Admin** I can **create, read, update and delete books** so that **I can manage the libraries inventory**
- As a **Site Admin** I can **view all books that are checked out** so that **I can track number of books and return dates per user**
- As a **Site Admin** I can **notify users of a fine** so that **I can apply a penalty for overdue books**

### Guthub project board
![Project board](static/readme/project-board.png)

### Wireframes
<br>
<details><summary><b>Site home page</b></summary>

![Site home image](static/readme/wireframe-home.png)
</details><br>

<details><summary><b>Site book list page</b></summary>

![Site book list image](static/readme/wireframe-list.png)
</details><br>

<details><summary><b>Site book detail page</b></summary>

![Site book detail image](static/readme/wireframe-detail.png)
</details><br>

<details><summary><b>Site sign up page</b></summary>

![Site signup image](static/readme/wireframe-signup.png)
</details><br>

<details><summary><b>Site login page</b></summary>

![Site login image](static/readme/wireframe-login.png)
</details><br>

The final designs ended up differing from the wireframe designs. This was simply due to preference of an alternative with the effect on different screen sizes.

### Entity Relationship Diagram
I created the following diagram in MS Excel. It shows the database tables, fields, field types and the relationships.
![entity relationship diagram](static/readme/erd.png)

# Features
- __Navigation Bar__
    - The nav bar remains at the top of the page across the site.
    ![Site nav bar](static/readme/site-header.png)
    - The functionality changes for mobile view.
    ![mobile nav bar](static/readme/mobile-header.png)
    - Additional options are shown when logged in as an admin.
    ![navbar admin](static/readme/navbar-admin.png)

- __Home Page__
    - The home page features the site name in a Google font. I used library style images for the page backgrounds.
![Home page](static/readme/landing-page.png)


- __Register page__
    - Users can create an account using the signup form.
    ![sign up](static/readme/sign-up.png)

- __Login page__
    - Once an account is created, users can sign in. Admin can also login with this form.
    ![login](static/readme/login.png)

- __logout page__
    - Once the logout link has been clicked in the nav bar, users are presented with the following form.
    ![logout](static/readme/logout.png)

- __Book List page__
    - The book list page displays a paginated list of the books in the libraries catalog.
![book list](static/readme/book-list-page.png)

- __Book Detail page__
    - The book detail page shows all the fields from the book table including the synopsis, to give users insight into what they can expect from the book. The synopsis section is scrollable within a fixed y-axis length.
    ![book details](static/readme/book-detail-page.png)
    - When users are logged in, the page features the checkout button.<br>
    <img src="static/readme/book-detail-user.png" width="272" height="376"><br>
    - Once the checkout button is clicked a confirmation message is shown to acknowledge the user's action. <br>
    ![checkout message](static/readme/checkout-book.png)
    - When logged in as an admin, additional buttons will be shown for updating and deleting the viewed book. <br>
    <img src="static/readme/book-detail-admin.png" width="272" height="456"><br>

- __Admin front end CRUD functionality__
    - The link to the Add Book form is on the nav bar when logged in as an admin.
    ![Add book form](static/readme/add-book-form.png)
    - Update Book form.
    ![Update book form](static/readme/update-book-form.png)
    - Delete Book form.<br>
    ![Delete book form](static/readme/delete-book-form.png)

- __Books on Loan__
    - Admin users can view a list of the books that are on loan.
    ![Books on loan](static/readme/books-onloan-page.png)
    
## Future Implementations
- The genres in the nav bar dropdown list all link to the book list page which shows all books. I would like to have implemented a filtered view, only showing books of one genre, matching the genre that the user clicked on in the dropdown list. 
- To import the genres in the navbar list from the Genre database table using the jinja template code. Currently, the genres are hard coded in the list.

Both of the above functions were attempted but I didn't have time resolve the issues that prevented them from working. 

- Once the return date has been exceeded a fine notification is issued to the user to inform them the book is overdue. I have a method to determine if the book is overdue in the BookIssued db model but didn't have time to implement this feature. A reminder email could also be sent to the user when the return date is approaching.

- If a book is checked out, then the checkout button is replaced with an 'on loan' message. 

# Testing

## HTML
- Book list page HTML
    - I encountered an error on the book list page.
![book list error](static/readme/book-list-error.png)

    - I removed the stray div tags.
![book list html](static/readme/book-list-html.png)

- Home page HTML
![home html](static/readme/html-checker.png)

- Book detail page HTML.
    - There was a warning which recommended using a heading tag (h2 - h6) within the section tag for the synopsis field.
![book detail html](static/readme/book-detail-html.png)

- Login page HTML
![login html](static/readme/login-html.png)

- Signup page HTML
![signup html](static/readme/signup-html.png)

## CSS
- I received the following result from the CSS validator.
![css checker](static/readme/css-checker.png)

## Python
Other Python files had very little code and/or were unaltered once generated by the app installation. I've included the files that had more code and were modified greatly.
- admin.py
![admin.py](static/readme/admin-py.png)
- models.py
![models.py](static/readme/models-py.png)
- settings.py
![settings.py](static/readme/settings-py.png)
- urls.py
![urls.py](static/readme/urls-py.png)
- views.py
![views.py](static/readme/views-py.png)

## Lighthouse
- Google Chrome Lighthouse report for desktop
![lighthouse desktop](static/readme/lighthouse-desktop.png)
- Report for mobile
![lighthouse mobile](static/readme/lighthouse-mobile.png)

## Automated Testing
A coverage report was genereated for my Python automated test files.
![coverage](static/readme/coverage.png)

## Errors and fixes during development
- When adding a book from the backend admin account I received the error: TypeError attribute must be string.
In the DB model I had set width and height attributes for the cover ImageField. The values for these attributes were integers which caused the error. The attribute values needed to be variables which contained the integer measurements. These attributes were optional so I removed them. I set the height in width attributes in the html \<img\> tag.

- The book cover image were not appearing on the site. I needed to include the following line of code in the app urls.py file, after the urlpatterns list.<br>
\+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)<br>

    I also needed to add the following import statements:<br>
from django.conf import settings<br>
from django.conf.urls.static import static<br>

    The settings.py file included:<br>
MEDIA_URL = '/media/'<br>
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br>

    With all of the above in place, the images displayed on the site and when a new book was created the cover images were automatically stored in the 'media' directory.

- When trying to add a new book through the front end admin page an error was recieved stating the slug field was missing. This was already working when using the admin backend pages. 
To fix this, I needed to add my own 'save' method to the Book class in models.py. This automatically generated the slug field value. I was then able to add a new book using the front end page.

- I set up a page to show a list of the books on loan. I set this up just like the book list page but none of the records would display.
I had to add the following variable to the BookIssued view class in views.py:<br>
context_object_name = 'books_issued'<br>
I then referenced the value of this variable in the html template code:<br>
{% for loan in books_issued %}<br>
The list of records were then displayed on the page.
