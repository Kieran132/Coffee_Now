# Coffee Now - Portfolio Project 4 - Full Stack Toolkit

## Live site

https://coffee-now-pp4.herokuapp.com/

## Repository

https://github.com/Kieran132/Coffee_Now

## Contents
- Project Goals
- UXD - User Experience Design
- Existing Features
    - Home Page
    - Order
    - Accessories
    - Contact
    - Wishlist
    - Sign Up
    - Log In
    - Log Out
- Technologies Used
- Testing
- Deployment
- Credits

## Project Goals

Coffee Now is my fourth project as part of the Code Institute Full Stack Web Developer Course.

The idea behind this project was to combine basic CRUD (Create, Read, Update, Delete) with a functioning website that allows different levels of authorised user to be able to do certain tasks within the project. The technolgies used within this project are; HTML, CSS, Javascript, Python and Django. Within this project I wanted to create a modern, sleek designed, interactive platform that allows any user to view the products and be able to find contact information. In addition, allow authenticated users to add items to their wishlist. Going further, allowing admin the ability to create, read, update and delete products without the use of the admin panel.


## UXD - User Experience Design

When designing and creating this project it was important to keep the user experience at the forefront of everything. This was achieved by breaking the project down into 5 planes;

- The Strategy Plane
- The Scope Plane 
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

## Strategy Plane

In this deisgn phase, I defined my initial outcomes in product objectives and also the user needs. From the beginning I knew that the website I create needed to be clean looking, modern, easy to use, clear to use and visually appealing to the user.

<u> Prodject Objectives </u>
 
- Working an operational website
- The use of CRUD functionality
- Clean, modern and sleek design

<u> Users and User Needs </u>

- Coffee enthusiasts looking for new type of coffee/accessory
- People looking to gift a product to another person
- Simple and easy navigation
- Clear direction on how to use the website

## Scope Plane

Within the Scope Place, I defined the features that I think would be best suited to the project and the design.

<u> Features </u>

- Homepage
- Order page showing range of products
- Accessory page showing the range of products
- Contact page showing where we are via google maps and contact form
- Product detail page
- Wishlist page
- Different levels of authorisation accessibility

## Structure Plane

Here at the Structure Plane, this is where I outlined the design colours, fonts and the building blocks of the project

#### Colors

<img src="media/README-Images/Colour-pallet.png">

The contrast between the browns, cream and greys I thought added to the theme of coffee orientated website, but in addition to this added a modern twist. 
Light Grey was used for navbar and footer to give a bold definitive look to top and bottom with the dark brown used as the font color to add contrast and make the font stand out.
The seasalt is used as an off white background color throughout the website.
The dark grey is used as color for the thematic break within the project.
The light brown is used throughout the project for the color of the font as its bright and eye catching but still readable.

<u> Fonts </u>

For all H1 tags I used MuseoModerno font. This gives a fun twist but still formal with more flowing nature of the font

Body of the porject Oxygen font was used. This font is clean and easy to read

<u> Key Models </u>

- User Autehntication

 - Allauth creates user profile and determines the depths of use within the project

- Order

    - Shows coffee products to the user
    - Depending on authentication, the user can add items to the wishlist or if admin they can add, edit and delete products

- Accessories

    - Shows accessory products to the user
    - Depending on authentication, the user can add items to the wishlist or if admin they can add, edit and delete products

- Contact

 - Shows user contact form which submits the form to the terminal

- Wishlist

    - Combines both order and accessories model for the authenticated user to see
    - These products can be deleted from the page by the user


## Skeleton Plane

#### Home Page

I knew how I wanted my home page to look. Welcome text at the top for an inviting feel then blocks of text telling the user what CoffeeNow is about, the ethos and where they get their coffee from. I wanted the layout to be simple and easy for the user and not too much text as to lose the interest of the user.

<img src="media/wireframes/index.html.png">

#### Order Page

The layout of the page I wanted contained into a 3 row formation. This I thought would allow the products to be easily visible and readable. Each card would uniform in shape with the other and the layout would identical also. For a responsiveness design the products will be stacked on top of one another depending on the screen size

<img src="media/wireframes/order.png">

#### Order Detail Page

This page I wanted a more indepth description and summary of the product in question. The image will be larger to the left of the screen with title, descriptions, price and button navigations on the right of the image. For a responsiveness design, the image will appear at the top of the screen with the description and buttons following below

<img src="media/wireframes/order-details.png">

#### Contact Page

For the contact page, I wanted to create a simple form that was easy to understand for the user and one which allowed the user to submit only the neccessary field - name, email address and message. In addition, I wanted to add google maps function so the user could physically see the location of CoffeeNow

<img src="media/wireframes/contact.png">

#### Accessories Page

The accessory page I felt needed to be similar to that of the order page. Firstly because of the uniformity of the website throughout but also the way in which each of the products are easily visible and readable. The responsiveness is also the same as the orde page where they are in one coloum above eachother

<img scr="media/wireframes/accessories.png">

#### Wishlist Page

Whenever the user added a product to their wishlist, I wanted again to stick to the row of 3 look to keep that uniformity. The responsiveness is also the same as the orde page where they are in one coloun above eachother

<img src="media/wireframes/wishlist.png">

## Surface Plane

#### Navigation Bar

- Designed and visible throughout
- Fully responsive on all screen sizes
- Easy and clear navigation

<img src="media/surface-plane-images/navbar-full-screen.png">

#### Footer

- Designed and visible throughout
- Fully responsive on all screens
- Social media icons with links

<img src="media/surface-plane-images/footer.png">

#### Home Page

- Welcoming message
- Clear descriptuive text
- Relevant images corrisponding to the text

<img src="media/surface-plane-images/index.html-main-body.png">

#### Order Page

- Visible images showing what the product is
- Readable text
- Clear navigation button

<img src="media/surface-plane-images/order-page.png">

#### Order Detail Page

- Large image to left side of the page
- More in-depth description of the chosen product
- Clear navigations buttons

<img src="media/surface-plane-images/order-details-page.png">

#### WishList Page

- Visible layout on what the user has added
- The ability to delete individual porducts

<img src="media/surface-plane-images/wishlist.html.png">