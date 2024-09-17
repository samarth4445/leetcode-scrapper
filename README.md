# LeetCode Contest Problem Filter

## Overview

This project addresses a common challenge faced by LeetCode users: the difficulty in filtering and practicing specific types of contest problems. Our solution is a comprehensive system that allows users to:

1. Access a curated collection of LeetCode contest problems
2. Filter problems by their position in contests (e.g., 3rd and 4th problems)
3. Filter problems by topics
4. Combine filters for more targeted practice sessions

**Website Coming Soon!** We're working hard to bring you an intuitive and powerful tool for LeetCode contest problem practice.

## Features

- **Extensive Problem Database**: A comprehensive collection of LeetCode contest problems.
- **Advanced Filtering**: 
  - Filter by problem rank in contests (1st, 2nd, 3rd, 4th)
  - Filter by problem topics
  - Combine filters for precise problem selection
- **User-Friendly Interface**: Easy-to-use web interface for accessing and filtering problems.
- **Regular Updates**: Keeps the database current with new contest problems.

## Technology Stack

- Backend: Django (Python)
- Frontend: React
- Database: PostgreSQL

## Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)
- PostgreSQL

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/samarth4445/leetcode-scrapper.git
   cd leetcode-scrapper
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:
   - Create a new PostgreSQL database for the project
   - Update the `DATABASES` configuration in `settings.py` with your database details

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

The backend will be available at `http://localhost:8000`.

## Usage

Once the website is launched:

1. Navigate to our website (coming soon!)
2. Use the filters on the left side to select your desired problem types:
   - Contest rank (1st, 2nd, 3rd, 4th)
   - Topics (e.g., Dynamic Programming, Graph Theory)
3. Click "Apply Filters" to see the list of matching problems.
4. Click on a problem to view its details and a link to the original LeetCode page.

## Development

To contribute to the project:

1. Create a new branch for your feature or bugfix:
   ```
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```
   git commit -m "Add some feature"
   ```

3. Push to your branch:
   ```
   git push origin feature/your-feature-name
   ```

4. Create a pull request on GitHub.

## Contributing

We welcome contributions to improve the system, add new features, or fix bugs. Please follow the development process outlined above and ensure your code adheres to the project's coding standards.

## Disclaimer

This project is not affiliated with, endorsed by, or sponsored by LeetCode. It is an independent tool created to help LeetCode users practice more efficiently. Please use responsibly and in accordance with LeetCode's terms of service.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/yourusername/leetcode-contest-filter](https://github.com/yourusername/leetcode-contest-filter)
