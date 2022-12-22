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
    
# Testing