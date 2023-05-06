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