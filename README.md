# WeByte Online Bookstore Project

Description
   The Online Bookstore Project is a web application developed using Django, PostgreSQL, HTML, CSS, and JavaScript.
   It serves as an online platform for selling books in various formats and includes features such as a shopping cart, checkout system, 
   and integration with Redis for caching purposes.

Features
   Book Catalog: Browse through a diverse collection of books available for purchase.
   Search Functionality: Easily search for books by title, author, genre, or keywords.
   Book Details: View comprehensive information about each book, including description, author, price, and available formats.
   Shopping Cart: Add books to the cart for later purchase and manage items in the cart.
   Checkout Process: Streamlined checkout process with secure payment options.
   Redis Integration: Utilizes Redis for caching frequently accessed data, improving performance and scalability.
   Responsive Design: The application is responsive and optimized for various devices and screen sizes.

Installation
   Clone the repository:
      git clone https://github.com/yourusername/online-bookstore.git
   Navigate to the project directory
      cd online-bookstore
   Install dependencies:
      pip install -r requirements.txt
   Configure the PostgreSQL database:
      Create a PostgreSQL database and update the database settings in settings.py.
   Configure Redis:
      Install and configure Redis according to your system specifications.
      Update the Redis connection details in settings.py.
   Apply migrations
      python manage.py migrate
   Start the Django development server
      python manage.py runserver
   Access the application through your web browser.

Usage
   Browse through the catalog to discover books of interest.
   Utilize the search functionality to find specific books based on various criteria.
   Add desired books to the shopping cart by clicking the "Add to Cart" button.
   Review items in the cart and proceed to checkout when ready.
   Enter shipping and payment details to complete the purchase.
   Take advantage of Redis caching for optimized performance and scalability.


Technologies Used
   Backend Framework: Django
   Database: PostgreSQL
   Frontend: HTML, CSS, JavaScript
   Caching: Redis

Authors
   leburikplc@gmail.com

Contact
   leburikplc@gmail.com
