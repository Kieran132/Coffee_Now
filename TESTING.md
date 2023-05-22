
## Manual Testing

#### Navigation bar

- Navigation bar full responsive across all screen sizes
- Dropdown items on all screen sizes are central and clear
- Sign in/sign out/sign up showing correctly depending which you use. Sign in showing sign out once signed in. Sign up and sign in show when no user has logged in
- Links direct the user to the correct page

#### Footer

- Footer is responsive to screen size
- Social Media icons redirect to relevant pages on a new tab

#### Order Page

- Items are all uniformed with one another
- Clear and easily understood
- Button is visible and directs to relevant page
- Add button visible and only appears for admin users
- All work on responsive screen sizes

#### Order Detail Page

- Clear and readable text
- Indepth description appears
- Wishlist button appears for logged in users
- Add and Delete buttons appear in addition to admin users
- Page reacts correctly to responsive screens

#### Accessories

- Items are all uniformed with one another
- Clear and easily understood
- Button is visible and directs to relevant page
- Add button visible and only appears for admin users
- All work on responsive screen sizes
- Wishlist button appears for logged in users
- Add and Delete buttons appear in addition to admin users

#### Wishlist Page

- Correctly shows added items
- Clear delete button to delete selected item
- Responsiveness works as intended and clear

#### Contact Page

- Email gets sent to external email inbox with correct information
- Screen size responsiveness correctly working
- Google Maps Api works and user can interact with the map

#### Admin

- Only admin have the ability to Add, Edit and Delete items
- Editing items correctly working and updates as it should
- Adding items correctly works and adds the item to the correct page
- Deleting of an item correctly works and deletes intended item from webpage and also database

***
***

## Validation

#### W3C HTML Validation

- 0 Errors
- 0 Warnings

#### W3C CSS Validator

- 0 Errors
- 0 Warnings

## Bugs / Issues and Resolutions

- Fix - Corrected bootstrap class to all dropdown navbar to work
    The initial way I had dropdown menu set up didnt allow for the function to work while viewing on smaller screen sizes. 
    Resolution - Amend the name in the clas by adding 'bs' to data toggle and data target

- FIX - Add if statement for images on wishlist page
    I had a proble viewing the correct product image on wishlist.html as i was using two different models into on html page.
    Resolution - Add an if statement to iterate through each of the models to show the correct image. If not then a default image will be shown

- FIX - Amend spacing between accessory products min 950px screen size
    Viewing the products on a min 950px screen size meant the product cards squeezed up together, not looking very clean or appealing
    Resolution - Added mt-5 class and removed 5rem margin-left

- FIX - changed email to charfield and added information to send_mail function
    As i have used googles smtp server to send details of the contact form to an external email, it meant i had to leave the from email as the email i am sending this to. 
    Resolution - To be able to see the users email address in the email, I changed the email part of the model to Charfield and added that information to the title of the email - "'Contact Form Submission from {}'.format(name + ', ' + email),"

