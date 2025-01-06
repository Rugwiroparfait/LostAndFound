
# Lost and Found System

A web application designed to help users submit, search, and claim lost items. This repository contains the backend API, with the frontend under development.

----------
![Lost And Found Logo](Lost_and_found.webp "Lost_And_Found")
----------
![License](https://img.shields.io/badge/license-MIT-green.svg)
## Project Structure

```
lost-and-found/
├── backend/
│   ├── src/
│   │   ├── config/
│   │   │   ├── database.js     # Database configuration
│   │   │   └── config.js       # App configuration
│   │   ├── controllers/
│   │   │   └── itemController.js # Handles item-related API logic
│   │   ├── middleware/
│   │   │   ├── errorHandler.js  # Error handling middleware
│   │   │   └── validation.js    # Input validation middleware
│   │   ├── models/
│   │   │   └── Item.js          # Mongoose schema for lost items
│   │   ├── routes/
│   │   │   └── itemRoutes.js    # API routes for item-related endpoints
│   │   └── app.js               # Express app setup and middlewares
│   ├── .env.example             # Example environment variables file
│   ├── package.json             # Backend dependencies and scripts
│   └── server.js                # Entry point for the backend server
├── frontend/                    # (Coming soon)
│   ├── src/
│   │   ├── components/          # React components (ItemCard, SearchBar, ItemForm)
│   │   ├── services/            # API integration logic
│   │   ├── utils/               # Utility functions
│   │   ├── App.jsx              # Main React app component
│   │   └── main.jsx             # React entry point
│   ├── .env.example             # Example environment variables for frontend
│   └── package.json             # Frontend dependencies and scripts
└── README.md                    # Project documentation

```

----------

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

-   **Node.js** (v14 or higher)
-   **MongoDB** (local or MongoDB Atlas)
-   **npm** or **yarn** for managing dependencies

### Backend Setup

1.  **Clone the repository**:
    
    ```bash
    git clone https://github.com/Rugwiroparfait/LostAndFound.git
    cd LostAndFound/backend
    
    ```
    
2.  **Install dependencies**:
    
    ```bash
    npm install
    
    ```
    
3.  **Create a `.env` file**: Copy the example `.env.example` file and create your own `.env` file:
    
    ```bash
    cp .env.example .env
    
    ```
    
4.  **Configure your environment**: Update the `.env` file with your MongoDB URI and port:
    
    ```env
    MONGODB_URI=mongodb://localhost:27017/lost-and-found  # or use MongoDB Atlas URI
    PORT=5000
    
    ```
    
5.  **Start the server**:
    
    ```bash
    npm run dev
    
    ```
    
    The backend API should now be running at `http://localhost:5000`.
    

### Frontend Setup (Coming Soon)

The frontend part of the application is under development and will be available soon. The components will be designed using React and will integrate with the backend API.

----------

## API Endpoints

### 1. **POST /api/items**

Submit a found item.

**Request Body**:

```json
{
  "ItemType": "Passport",
  "name": "John Doe's Passport",
  "location": "Central Park",
  "dateFound": "2025-01-06T12:00:00Z",
  "description": "Red passport with a US visa.",
  "contact": "123-456-7890",
  "status": "Found"
}

```

**Response**:

```json
{
  "message": "Item submitted successfully"
}

```

### 2. **GET /api/items**

Retrieve all items.

**Response**:

```json
[
  {
    "_id": "12345",
    "ItemType": "Passport",
    "name": "John Doe's Passport",
    "location": "Central Park",
    "dateFound": "2025-01-06T12:00:00Z",
    "description": "Red passport with a US visa.",
    "contact": "123-456-7890",
    "status": "Found"
  }
]

```

### 3. **GET /api/items/search?name=<item_name>**

Search for items by name.

**Query Parameter**:

-   `name` (required): The name or part of the name to search for.

**Response**:

```json
[
  {
    "_id": "12345",
    "ItemType": "Passport",
    "name": "John Doe's Passport",
    "location": "Central Park",
    "dateFound": "2025-01-06T12:00:00Z",
    "description": "Red passport with a US visa.",
    "contact": "123-456-7890",
    "status": "Found"
  }
]

```

### 4. **PUT /api/items/:id/claim**

Claim a found item.

**Response**:

```json
{
  "message": "Item claimed successfully"
}

```

----------

## Project Goals

The primary goal of this project is to create a system that allows users to submit, search for, and claim lost items in an efficient and user-friendly manner. This will be achieved through a clean and scalable backend API.

In the future, a frontend application will be developed to interact with this API, providing a complete web-based interface for users.

----------

## License

This project is licensed under the MIT License - see the [LICENSE] file for details.

----------

## Contributing

We welcome contributions to improve the Lost and Found System. To contribute:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature`).
3.  Make your changes and commit them (`git commit -am 'Add new feature'`).
4.  Push to the branch (`git push origin feature/your-feature`).
5.  Open a pull request.
