# ASH|TECHS

(Developer: Femi Ashiru)

![ASH|TECHS Website Responsive Image](docs/am-i-responsive.png)

[Live Project](https://ash-techs-a3f0a77bec88.herokuapp.com/)

## Table of Content

- [ASH|TECHS](#ashtechs)
  - [Table of Content](#table-of-content)
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
  - [Scope](#scope)
  - [Design](#design)
    - [Design Choices](#design-choices)
    - [Colour](#colour)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [What links users can and cannot see](#what-links-users-can-and-cannot-see)
    - [Database Structure](#database-structure)
    - [MongoDB Collections](#mongodb-collections)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks and Tools](#frameworks-and-tools)
  - [Features](#features)
    - [Logo Navigation and Search bar](#logo-navigation-and-search-bar)
    - [Home](#home)
    - [Footer](#footer)
    - [Sign In](#sign-in)
    - [Register](#register)
    - [Profile](#profile)
    - [Add Product](#add-product)
    - [Edit Product](#edit-product)
    - [Delete Product](#delete-product)
    - [Add Review](#add-review)
    - [Edit Review](#edit-review)
    - [Delete Review](#delete-review)
    - [Bag](#bag)
    - [Checkout](#checkout)
    - [Checkout Success](#checkout-success)
    - [404 Page](#404-page)
    - [500 Page](#500-page)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JS Validation](#js-validation)
    - [Python Validation](#python-validation)
    - [Accessibility](#accessibility)
    - [Performance](#performance)
    - [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
    - [Responsiveness](#responsiveness)
    - [Testing user stories](#testing-user-stories)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- To see all products within the store.
- To make purchases.
- To see all reviews within the store.
- To leave product reviews.
- To add items to wishlist.

### Site Owner Goals

- To allow users to purchase products.
- To manage the admin of products.

## User Experience

### Target Audience

- People who are interested in purchasing technology products.
- People looking for bargains and deals within tech.

### User Requirements and Expectations

- Easy to use navigation that is responsive.
- Be able to easily browse between sections of the site.
- All links to work as expected.
- Appealing design that works well on both desktop and mobile devices.
- Be able to browse products log in and make a purchase.
- Be able to add reviews to all products if logged in.
- Be able to edit/delete users own reviews.
- Be able to add and remove items from wishlist if logged in.
- All users to b aable to sort and filter down to specific products.
- All users to be able to search for products using a search bar feature.
- All users to be able to see products and reviews.
- Accessibility.

### User Stories

| **Num** | **As an/a** | **I want to be able to** | **So that I can** |
|------------|-------------|--------------------------|-------------------|
|1|Shopper|See all products|Decide which item to purchase|
|2|Shopper|See individual product details|See specific details, such as price, quantity, description and review|
|3|Shopper|Sort products by brand, price, rating and category|See products in ascending and descenging order|
|4|Shopper|See my recent orders|Track my previous orders|
|5|Shopper|See my wishlist|Track what items I want|
|6|Shopper|Add and remove items from wishlist|See wishlist items in my profile|
|7|Shopper|Use search bar to search products|Find a specific product|
|8|Shopper|See all reviews|Make a choice on products based on previous reviews|
|9|Shopper|Add reviews for specific products|Give opinion on products and help others to make decisions|
|10|Shopper|Edit or Delete reviews for specific products|Remove or update an incorrectly submitted review|
|11|Shopper|Easily update products quantity when purchasing it|Buy a certain amount of products|
|12|Shopper|Receive an email confirmation when I puechase a product|Know that my purchase has been successful|
|13|Shopper|Update my profile|Add new shipping/billing details to my profile|
|14|Shopper|Add and Remove Items from my shopping bag|Have greater flexibility over what I purchased|
|15|Site User|Register to the site|See and edit my profile|
|16|Site User|Log in and out|Access my personal account information|
|17|Site User|Receive an email confirmation that I have registered my account|Confirm that I can log in|
|18|Site Owner|To add products|Have more products on the site|
|19|Site Owner|To edit products|Correct, update or change a product|
|20|Site Owner|To delete products|Remove products we no longer sale|

## Scope

The scope of the project in its first release is defined by the following features:

- Simple navigation that allows user to navigate between sections of the site.
- Allow users to log into their own accounts and perform CRUD operations on reviews and make purchases from site utilising Stripe implementation. Admin users should also be able to perform CRUD operations on products.
- Allow all users to see products and reviews for those products.
- Allow all users to search and sort all products.
- Allow visitors to create an account and see their previous orders, wishlist and details on profile.
- An error page (404.html) and internal server error page (500.html) that appears when visiting a page that does not exist or when an internal server error has been detected.
- Clear and simple favicon icon to help users identify the site.

Features to be built in future releases:

- Allow admin to add/edit/delete Brands, Categories and User Accounts without accessing Django dashboard.
- Further development to allow Site Users to delete their own account and cancel orders.
- Ability to send an unsuccessful email if something goes wrong with their purchase.
- Allow deals and clearance items to be seen on home page for mobile and tablet.

## Design

### Design Choices

ASHTECHS was designed to mimic the look and feel of popular technonlogy retailer Currys PC World. The layout is a very simple and clean one with little clutter on the page so that users can accurately locate all the necesarry sections of the site with ease. The majority of the site is styled using Bootstrap components and custom CSS which has helped the site keep a consistent structure and made it fully responsive on Mobile and Tablet devices.

### Colour

For the colour scheme I opted for simple yet bold colours. I opted for different shades of blue to represent Business ([Color Theory: Blue as a Branding Color](https://brandingcompass.com/branding/color-theory-blue-as-a-branding-color/)) as well as Loyalty, trust and security. I want Site Users to know that this brand can be trusted and that theme is also represented in the choice of logo taken from [Favicon](https://favicon.io/)

![Colour Scheme](docs/features/colour-scheme.png)

### Fonts

The main font used in the entirety of the website is "'Roboto', sans-serif". For the 'TECH' part of the logo I opted for 'Share Tech', sans-serif which has somewhat of a digital feel to it. The 'Share Tech' font is also used for the headings across the site. Both fonts were imported using Google Fonts API.

### Structure

The site has a total of 14 pages each having certain restrictions based on who is logged in. The entire site is fully responsive and has been tested within the industry standard width of 320px.

The website consists of 14 main pages:

- Main page which shows all movies stored, giving all users the ability to see details and reviews.
- Sign in page that allows returning users to log in to their account.
- Register page that allows visitors to the site to set up their own new accounts.
- Profile page that allows logged in users to see and edit their movies as well as delete their own account. Admin user can also see all the users with accounts and delete them.
- Add and edit movie pages which are only accessible to logged in users.
- Add and edit review pages which are only accessible to logged in users.
- Manage genere page which allows the admin user to see all genres stored and delete them.
- Add and edit genre pages which are only accessible to admin user.

Using Figma I created a conceptual flow chart of how users will navigate throughout the site.

![MovieCrazyClub ConceptualFlow Image](docs/data_models/conceptual-flow-chart.png)

#### What links users can and cannot see

- All users:
  - Home
  - Products
  - Product Details
  - Shopping Bag
  - Sign In
  - Register
- Logged in (non-admin user)
  - Home
  - Products
  - Product Details
  - Shopping Bag
  - Sign Out
  - Profile
  - Checkout
  - Checkout Success
  - Add/Edit/Delete Review
- Logged in (admin user)
  - Home
  - Products
  - Product Details
  - Shopping Bag
  - Sign Out
  - Profile
  - Checkout
  - Checkout Success
  - Add/Edit/Delete Review
  - Add/Edit/Delete Product

- Logged in users can only edit and delete their own reviews.

### Database Structure

Using Lucid chart I created an ERD to show how data will flow and be stored within ElephantSQL for Django.

![MovieCrazyClub MongoDB Image](docs/data_models/movie-crazy-club-erd.png)

### MongoDB Collections

<p>Genres</p>

"_id":{"$oid":"UNIQUE_ID"},

"genre_name":"Comedy"

<p>Movies</p>


"_id":{"$oid":"UNIQUE_ID"},

"genre_name":"Comedy",

"title":"Rush Hour",

"year":{"$numberInt":"1998"},

"plot":"When a Chinese diplomat's daughter is kidnapped in Los Angeles, he calls in Hong Kong Detective Inspector Lee (Jackie Chan) to assist the FBI with the case. But the FBI doesn't want anything to do with Lee, and they dump him off on the LAPD, who assign wisecracking Detective James Carter (Chris Tucker) to watch over him. Although Lee and Carter can't stand each other, they choose to work together to solve the case on their own when they figure out they've been ditched by both the FBI and police.",

"rating":{"$numberInt":"89"},

"director":"Brett Ratner",

"poster":"IMAGE_FROM_OMDB_API",

"created_by":"USER"

<p>Reviews</p>

"_id":{"$oid":"UNIQUE_ID"},

"review":"This movie is really funny. I laughed from start to finish.",

"title":"Rush Hour",

"created_by":"USER"

<p>Users</p>

"_id":{"$oid":"UNIQUE_ID"},

"username":"CHOSEN_USERNAME",

"password":"HASHED_PASSWORD"


### Wireframes

<details><summary>Home</summary>
<img src="docs/wireframes/home.png" alt="Home wireframe">
</details>

<details><summary>Products</summary>
<img src="docs/wireframes/products.png" alt="Product wireframe">
</details>

<details><summary>Products Admin (Add and Edit)</summary>
<img src="docs/wireframes/product_admin_add_edit.png" alt="Product Admin wireframe">
</details>

<details><summary>Product Details</summary>
<img src="docs/wireframes/product_details.png" alt="Product Details wireframe">
</details>

<details><summary>Reviews (Add and Update)</summary>
<img src="docs/wireframes/reviews_add_update.png" alt="Reviews wireframe">
</details>

<details><summary>Profile</summary>
<img src="docs/wireframes/profile.png" alt="Profile wireframe">
</details>

<details><summary>Sign In</summary>
<img src="docs/wireframes/sign_in.png" alt="Sign In wireframe">
</details>

<details><summary>Register</summary>
<img src="docs/wireframes/register.png" alt="Register wireframe">
</details>

<details><summary>Bag</summary>
<img src="docs/wireframes/bag.png" alt="Bag wireframe">
</details>

<details><summary>Checkout</summary>
<img src="docs/wireframes/checkout.png" alt="Checkout wireframe">
</details>

<details><summary>Checkout Success</summary>
<img src="docs/wireframes/checkout_success.png" alt="Checkout Success wireframe">
</details>

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Frameworks and Tools

- Django
- AWS
- Bootstrap
- ElephantSQL
- Stripe
- Git
- GitHub
- CodeAnywhere
- Balsamiq
- Figma
- Lucid
- Google Fonts
- Adobe Color
- Font Awesome
- Favicon<span>.</span>io

## Features

### Logo Navigation and Search bar

- Navigation and Logo remains consistent on each page
- Navigation and search bar are fully responsive and collapse when window is resized
- Navigation allows users to easily navigate the site and search bar allows users to search products (User story 10)
- Logo in Navigation takes user back to the main page

<p>Nav on Desktop, tablet and mobile</p>

![Logo Navigation on Desktop](docs/features/feature-navigation-bar.gif)

<p>Search Bar</p>

![Search bar](docs/features/feature-search-bar.gif)

### Home

- Displays shop now button and two products that are special types (Deal and Clearance)  (User story 1)

![Home](docs/features/feature-movie-section.gif)

### Footer

- Displays logo, copyright and links to product pages 

![Footer](docs/features/feature-footer.png)

### Sign In

- Allows users to sign into their own account  (User Story 5, 14, 15)

![Sign In](docs/features/feature-sign-in.gif)

### Register

- Allows users to register with ASHTECHS  (User Story 2, 14)

![Register](docs/features/feature-register.gif)

### Profile

- Allow users to see their own profile (User Story 15)

![Non-admin Profile](docs/features/feature-profile-non-admin.png)

### Add Product

- Allows Site Owner to add procut

![Add Movie](docs/features/feature-add-movie.gif)

### Edit Product

- Allows Site Owner to edit product

![Edit Movie](docs/features/feature-edit-movie.gif)

### Delete Product

- Allows Site Owner to delete products

![Delete Movie](docs/features/feature-delete-movie.gif)

### Add Review

- Allows Site Users to add review

![Add Review](docs/features/feature-see-add-review.gif)

### Edit Review

- Allows Site Users to edit their own review

![Edit Review](docs/features/feature-edit-review.gif)

### Delete Review

- Allows Site Users to delete their own review

![Delete Review](docs/features/feature-delete-review.gif)

### Bag

- Allows Site Users to see their shopping bag contents

![Bag](docs/features/shopping-bag.gif)

### Checkout

- Allows Site Users to checkout

![Checkout](docs/features/checkout.gif)

### Checkout Success

- Allows Site Users to see their successful order details

![Checkout Success](docs/features/checkout-success.gif)

### 404 Page

- Site Users should be presented with a 404 page if they visit an incorrect page

![404](docs/features/feature-404-page.gif)

### 500 Page

- Site Users should be presented with a 500 page if there are any server issues

![500](docs/features/feature-500-page.png)

## Validation

### HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website. 
In order to test some of the HTML validation links you must be logged in.

index.html(Home) [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2F) - No Errors Found

products.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fproducts%2F) - No Errors Found

add_product.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fproducts%2Fadd_product) - No Errors Found

edit_product.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fproducts%2Fedit_product%2F19) - No Errors Found

product_details.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fproducts%2F3%2F) - No Errors Found

add_review.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Freviews%2Fadd_review%2F3) - No Errors Found

update_review.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Freviews%2Fupdate_review%2F45) - No Errors Found

profile.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fprofile%2F) - No Errors Found

login.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Faccounts%2Flogin%2F) - No Errors

signup.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Faccounts%2Fsignup%2F)

bag.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fbag%2F) - No Errors Found

checkout.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fcheckout%2F) - No Errors Found

- To check the test for checkout_success.html please ensure that you use an order number from your own order history and replace the current one in the link

checkout_success.html [result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2Fcheckout%2Fcheckout_success%2FC3E5AFDC463244CBA8BD9F780EA55F1B) - No Errors Found

403.html, 404.html and 500.html mirror index.html and have been tested manually by adding the text input directly with no errors

### CSS Validation

The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.
After testing the whole sites CSS and my own custom CSS all pages passed with no errors, however, there were a number of warnings present that were related to the webkit css extensions used.

whole site [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fash-techs-a3f0a77bec88.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

base.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fash-techs.s3.eu-west-2.amazonaws.com%2Fstatic%2Fcss%2Fbase.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - No Errors Found

checkout.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fash-techs.s3.eu-west-2.amazonaws.com%2Fstatic%2Fcheckout%2Fcss%2Fcheckout.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - No Errors Found

products.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fash-techs.s3.eu-west-2.amazonaws.com%2Fstatic%2Fproducts%2Fcss%2Fproducts.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - No Errors Found

profile.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fash-techs.s3.eu-west-2.amazonaws.com%2Fstatic%2Fprofiles%2Fcss%2Fprofile.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - No Errors Found

reviews.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fash-techs.s3.eu-west-2.amazonaws.com%2Fstatic%2Freviews%2Fcss%2Freviews.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - No Errors Found

### JS Validation

[JS Hint](https://jshint.com/) was used to validate the JavaScript of the website.

<details><summary>footer.js</summary>
<p>No Errors</p>
<img src="docs/validation/js/footer.png" alt="footer.js">
</details>

<details><summary>handle_quantity_script.js</summary>
<p>No Errors</p>
<img src="docs/validation/js/handle_quantity_script.png" alt="handle_quantity_script.js">
</details>

<details><summary>handle_sort_selector.js</summary>
<p>No Errors</p>
<img src="docs/validation/js/handle_sort_selector.png" alt="handle_sort_selector.js">
</details>

<details><summary>handle_update_delete_script.js</summary>
<p>No Errors</p>
<img src="docs/validation/js/handle_update_delete_script.png" alt="handle_update_delete_script.js">
</details>

<details><summary>profile.js</summary>
<p>No Errors</p>
<img src="docs/validation/js/profile.png" alt="profile.js">
</details>

<details><summary>stripe.js</summary>
<p>Two unused variables as a result of Stripe and Jquery usage</p>
<img src="docs/validation/js/stripe.png" alt="stripe.js">
</details>

### Python Validation

[Python Linter](https://pep8ci.herokuapp.com/) was used to test as coding went on.
On completion of the project I used the command `python3 -m flake8` to clear any other issues

### Accessibility

The WAVE WebAIM web accessibility tool was used to ensure the website met accessibility standards.
Some pages cannot be tested due to being behind authentication, so I tested all the pages that were not.

index.html(Home) [results](https://wave.webaim.org/report#/https://ash-techs-a3f0a77bec88.herokuapp.com/) - 1 Contrast Error.

products.html [results](https://wave.webaim.org/report#/https://ash-techs-a3f0a77bec88.herokuapp.com/products) - 1 Contrast Error.

product_details.html [results](https://wave.webaim.org/report#/https://ash-techs-a3f0a77bec88.herokuapp.com/products/5) - 3 Contrast Errors.

login.html [results](https://wave.webaim.org/report#/https://ash-techs-a3f0a77bec88.herokuapp.com/accounts/login/) - 2 Contrast Errors.

signup.html [results](https://wave.webaim.org/report#/https://ash-techs-a3f0a77bec88.herokuapp.com/accounts/signup/) - 1 Contrast Error

### Performance

Google Lighthouse Tool was used to test the performance of the website. 
<details><summary>movies</summary>
<img src="docs/validation/performance/movies.png" alt="lighthouse for movies">
</details>

### Performing tests on various devices

The website was tested on the following devices:

- Apple MacBook Pro M1
- Apple iPhone 11
- Xiaomi Mi 11 Lite

### Browser compatibility

The website was tested on the following browsers:

- Google Chrome
- Safari
- Mozilla Firefox
- Microsoft Edge

### Responsiveness

The website is completely responsive and has been tested on mobile, tablet and desktop:

<details><summary>Mobile, Tablet and Desktop</summary>
<img src="docs/responsiveness/respsonsiveness_of_site.gif" alt="Responsiveness of Site">
</details>

### Testing user stories

01. I want to see all movies on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Movies and Navigation| Click on the home link or logo | show_movies route should be open with all movies display | Works as expected |

![Movie Section](docs/features/feature-movie-section.gif)

02. I want to create an account on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Register | Click on register link and enter new details | Correct details should be accepted and profile page with newly created account should appear. Flash message should confirm this. | Works as expected |

![Register](docs/features/feature-register.gif)

03. I want to add movies on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Add Movie | Click on Add movie and enter detials of movie | Correct details should be accepted and show_movies page should open with newly added film. Flash message should confirm this.  | Works as expected |

![Add Movie](docs/features/feature-add-movie.gif)

4. I want to add reviews on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reviews | Click on see reviews button, click leave review and enter details | Correct details should be accepted and reviews for specific film should be displayed with newly added review. Flash message should confirm this. | Works as expected |

![Add Review](docs/features/feature-see-add-review.gif)

5. I want to log into my MCC account.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navigation, Sign In and Profile| Click on Sign in and enter correct details | Profile should open with logged in user. Flash message should confirm this. | Works as expected |

![Sign In](docs/features/feature-sign-in.gif)

6. I want to edit movies on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Movies and Edit Movie | Click on the edit movie button, enter correct details and click update movie | Edit movie should confirm if user wants to update. Once confirmed it should navigate to the show_movies route displaying updated movie. Flash message should confirm this. | Works as expected |

![Edit Movie](docs/features/feature-edit-movie.gif)

7. I want to edit reviews on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reviews and Edit Review | Click on the see reviews button, locate user review and click on the edit review button. Update review with correct details and click update review | Edit review should confirm if user wants to update. Once confirmed it should navigate to the show_revies route displaying update review. Flash message should confirm this. | Works as expected |

![Edit Review](docs/features/feature-edit-review.gif)

8. I want to delete my movies on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Movies and Delete Movie | Click on the delete movie button | Delete movie should confirm if user wants to delete. Once confirmed it should navigate to the show_movies route with deleted movie no longer present. Flash message should confirm this. | Works as expected |

![Delete Movie](docs/features/feature-delete-movie.gif)


9. I want delete my reviews on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reviews and Delete Review | Click on see reviews button, locate your review and click delete review button | Delete review should confirm if user wants to delete. Once confirmed it should navigate to the show_reviews route with delete review no longer present. Flash message should confirm this. | Works as expected |


![Delete Review](docs/features/feature-delete-review.gif)


10. I want to use the search bar to search movies on MCC.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Search Bar | Type search criteria within the search bar | Should navigate to the search route and display relevant movies that match search criteria. Should also display if no match can be found | Works as expected |


![Search bar](docs/features/feature-search-bar.gif)


11. I want to delete my account if no longer needed.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Profile and Delete user | Click on the delete account button in profile | Delete user should confirm if user wants to delete. Once confirmed it should delete all associated, movies and reviews as well as their account and finally log the user out | Works as expected |


![Delete User](docs/features/feature-delete-user.gif)


12. I want all users to be able to see all movies.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Movies and Navigation| Click on the home link or logo | show_movies route should be open with all movies display | Works as expected |


![Movie Section](docs/features/feature-movie-section.gif)


13. I want all users to be able to see all reviews.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reviews | Click on the see reviews button for specific film | show_reviews route should open with selected film and all reviews displayed. | Works as expected |

![See Reviews](docs/features/feature-see-reviews.gif)


14. I want all users to be able to create an account.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Register | Click on register link and enter new details | Correct details should be accepted and profile page with newly created account should appear. Flash message should confirm this. | Works as expected |


![Register](docs/features/feature-register.gif)


15. I want users who have created accounts to log in and see their profile.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navigation, Sign In and Profile| Click on Sign in and enter correct details | Profile should open with logged in user. Flash message should confirm this. | Works as expected |

![Sign In](docs/features/feature-sign-in.gif)


16. I want account users to add a movie.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Add Movie | Click on Add movie and enter detials of movie | Correct details should be accepted and show_movies page should open with newly added film. Flash message should confirm this.  | Works as expected |

![Add Movie](docs/features/feature-add-movie.gif)

17. I want account users to edit their own movie.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Movies and Edit Movie | Click on the edit movie button, enter correct details and click update movie | Edit movie should confirm if user wants to update. Once confirmed it should navigate to the show_movies route displaying updated movie. Flash message should confirm this. | Works as expected |

![Edit Movie](docs/features/feature-edit-movie.gif)

18. I want account users to delete their own movie.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Movies and Delete Movie | Click on the delete movie button | Delete movie should confirm if user wants to delete. Once confirmed it should navigate to the show_movies route with deleted movie no longer present. Flash message should confirm this. | Works as expected |

![Delete Movie](docs/features/feature-delete-movie.gif)

19. I want account users to add reviews.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reviews | Click on see reviews button, click leave review and enter details | Correct details should be accepted and reviews for specific film should be displayed with newly added review. Flash message should confirm this. | Works as expected |

![Add Review](docs/features/feature-see-add-review.gif)

20. I want account users to edit their own review.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reviews and Edit Review | Click on the see reviews button, locate user review and click on the edit review button. Update review with correct details and click update review | Edit review should confirm if user wants to update. Once confirmed it should navigate to the show_revies route displaying update review. Flash message should confirm this. | Works as expected |

![Edit Review](docs/features/feature-edit-review.gif)

21. I want account users to delete their own review.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Reviews and Delete Review | Click on see reviews button, locate your review and click delete review button | Delete review should confirm if user wants to delete. Once confirmed it should navigate to the show_reviews route with delete review no longer present. Flash message should confirm this. | Works as expected |

![Delete Review](docs/features/feature-delete-review.gif)

22. I want to be able to log in as admin.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Sign In and Profile | Click sign in and log in as admin | Profile should open that displays other users accounts and Manage genre in the navigation. Flash message should confirm this. | Works as expected |

![Admin Login](docs/features/feature-admin-log-in.gif)

23. I want to be able to add a genre.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Manage Genres | Click add genre button, enter the correct details and add genre | show_genres route should appear with newly added genre. Flash message should confirm this. | Works as expected |


![Manage Genres](docs/features/feature-manage-genres.gif)


24. I want to be able to edit a genre.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Manage Genres | Click the edit genre button, enter the correct details, and click update genre | Manage genres should confirm if user wants to update genre. Once confirmed it should navigate to the show_genres route with updated genre displayed. Flash message should confirm this. | Works as expected |

![Manage Genres](docs/features/feature-manage-genres.gif)

25. I want to be able to delete a genre.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Manage Genres | Click the delete genre button and confirm deletion | Manage genres should confirm if user wants to delete genre. Once confirmed it should navigate to the show_genres route with deleted genre no longer present. All it's associated movies should also be deleted. Flash message should confirm this. | Works as expected |

![Manage Genres](docs/features/feature-manage-genres.gif)

26. I want to be able to prompt account users before updating or deleting.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| All Update and Delete functionality | Click on update or delete for specific movie, review or genre (admin) | Modal should appear confirming whether user wishes to update/delte item. User has choice to say yes or no | Works as expected |


![Manage Genres](docs/features/feature-manage-genres.gif)


27. I do not want users to use browser back button if they are looking for a page that does not exist.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| 404 Page | Type in an incorrect route in address bar | 404 template should be rendered with a button navigating to home beneath | Works as expected |

![404](docs/features/feature-404-page.gif)


## Bugs

| **Bug** | **Fix** | 
|-------------|------------|
|Not so much of a bug but the OMDB api was shown in the fetch_movie_poster.js and the add/edit movie page which could present a potential security risk| Moved the api key to the env.py, encoded it in base64 within the app.py file and then decoded it when it reached the html within an internal script tag which could then be called in the fetch_movie_poster.js - source used to help with this are detailed in credits|


## Deployment

You can fork the repository by:
1. Navigating to the GitHub repository
2. Click on "Fork" button in top right hand corner (Please note you must be signed in to Fork a repository)

You can clone the repository by:
1. Navigating to GitHub repository 
2. Locate the "Code" button above the file list and click it 
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to where you wish to clone the directory
6. Type ```git clone``` and paste in the URL from the clipboard e.g ```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)```
7. Press Enter to create your local clone in your chosen folder.

Deployed using Heroku using the following steps:
1. You will need to first create the requirements that Heroku will use to import the dependencies. To do so type the following command in your CLI ```pip3 freeze > requirements.txt```

2. You will then need a Procfile which is needed to specify the commands that are executed by the Heroku app on startup. To do so type the following command in your CLI ```echo web: python app.py > Procfile```

3. Be sure to add, commit and push your changes once you have done the above two tasks
4. Within Heroku follow the steps "New" > "Create New App" > Give app a name and choose the relevant region

![heroku step1](docs/heroku-steps/heroku-1.png)
![heroku step2](docs/heroku-steps/heroku-2.png)

5. The newly created app will open on "Deploy", then follow the steps "Deployment Method" > Select Github and search for the repo-name. Once you have found it, click "Connect" beside the repo-name

![heroku step3](docs/heroku-steps/heroku-3.png)
![heroku step4](docs/heroku-steps/heroku-4.png)

6. Be sure to update the "Config Vars" located in "Settings" > "Config Vars" > "Reveal Config Vars". You will need to set the following variables:
    - IP
    - MONGO_DBNAME
    - MONGO_URI
    - SECRET_KEY
    - OMDB_API_KEY
    - PORT

![heroku step5](docs/heroku-steps/heroku-5a.jpg)

![heroku step5](docs/heroku-steps/heroku-5.png)

![heroku step6](docs/heroku-steps/heroku-6.png)

7. Please also be sure to have set your Heroku API key within the Heroku CLI Toolbelt. The API key can be found in "Account Settings" > "Account" > "API Key"

![heroku step7](docs/heroku-steps/heroku-7.png)

![heroku step8](docs/heroku-steps/heroku-8.png)

![heroku step9](docs/heroku-steps/heroku-9.png)

## Credits

### Media

- Movie Wallpaper background | soure: [Wallpapers.com](https://wallpapers.com/)

- All movie poster images are API generated from [OMDb](https://www.omdbapi.com/)

- Image used on add and edit movie pages taken from [Font Awesome](https://fontawesome.com/icons/image?f=classic&s=solid)

### Code

- Used [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/) to add error routes for 404 and 500

- Used [Code Institute Github Solutions](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js) to assist with validating materializes drop down correctly

- Used [Python Basics](https://pythonbasics.org/flask-redirect-and-errors/), [w3schools](https://www.w3schools.com/python/python_regex.asp), [Stack Overflow](https://stackoverflow.com/questions/33467536/how-to-check-if-a-string-is-made-only-of-letters-and-numbers) and [Pythex](https://pythex.org/) for regex and abort class on `valid_object_id` function in app.py

- Used [Geeks for Geeks](https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/) and [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/atob) to encode/decode the OMDB api so it cannot be seen directly in the JS or HTML file

## Acknowledgements

I would like to take the opportunity to thank:
- Mo Shami for continued mentorship, guidance and support throughout this project. 
- Iris Smok for continued encouragement whilst working on this project.
- and all the Teaching and Non-teaching Personnel at Code Institute.