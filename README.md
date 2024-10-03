**Project Title:**
Student Management System built with Python, Tkinter, and MySQL)

**Project Description**
-This was a boilerplate classroom project but I modified it to suit the needs of my school's newly opened library commons. The project aims to solve student management issues as a result of the large pool of students that troop in everyday to study. 
- The Student Management System is an interactive desktop application designed to help educational institutions or administrators manage student records efficiently.
- Built using Python's Tkinter library for the graphical user interface (GUI) and MySQL as the database backend, this project allows users to seamlessly
perform CRUD (Create, Read, Update, Delete) operations on student data. 
- The system features a login system, secure data handling, and the ability to export data to CSV files. 
- This project aims to simplify student data management with a clean, user-friendly interface while ensuring security and scalability.

**Features:**
*Login Authentication:*
- Secure login system to ensure authorized access.
- Displays an error message for incorrect credentials.

*Student Management:*
- Add new students by inputting their details (ID, Name, Email, Program, etc.).
- Update existing student records.
- Search for students by ID, name, or other criteria.
- Delete student records from the database.
- View all student records in a structured table format.

*Data Export:*
Export student data as a CSV file to store or share externally.

*Real-time Date and Time:*
Displays real-time clock and date to provide a current timestamp for operations.

*Responsive GUI:*
- Built using Tkinter for an interactive and visually appealing user interface.
- Icons and images make the application intuitive and modern.

*Database Integration:*
- Powered by MySQL for efficient data storage and retrieval.
- Supports database creation and table management on first-time setup.

*Technologies Used:*
- Python: Core programming language for logic and GUI.
- Tkinter: For building the graphical user interface.
- MySQL: Database management system for storing student records.
- Pandas: For data export functionality.
- Pillow (PIL): For handling images within the application.
- Git: Version control for managing project development.

*How to Run the Project:*
- Clone the Repository: Clone the project repository from GitHub using the following command:
bash
Copy code
git clone https://github.com/Namelessweirdo/student-management-system.git
- Install Dependencies: Install the required dependencies:
bash
Copy code
pip install tkinter
pip install pymysql
pip install pandas
pip install pillow

- Set Up MySQL:
Install MySQL on your machine.
Create a MySQL user and grant the necessary permissions.
Ensure you update the host, username, and password in the code to match your MySQL credentials.

- Run the Application: Execute the sms.py file to start the Student Management System:
bash
Copy code
python sms.py

*Usage:*
- Login:
Use the login screen to authenticate.
Default credentials can be customized by modifying the login function.

- Add/Update/Delete Students:
Navigate to "Add Student" or "Update Student" to manage student records.
Use "Delete Student" to remove a record from the database.

- Search Students:
Search students by ID, Name, or other attributes using the search feature.

- Export Data:
Save student data as a CSV file by selecting the "Export Data" option.

*Folder Structure:*
- /images/: Contains all image files (login icons, student avatars).
- /database/: Database setup scripts for MySQL.
- sms.py: Main file containing the student management system code.
- README.md: Documentation for the project.

*Future Improvements:*
- Adding role-based authentication (Admin vs. User access).
- Implementing a REST API for web-based access to the student database.

Installation Video:
Provide a YouTube link or local video that demonstrates how to install and use the application.

Demo Link:
[Demo](https://vimeo.com/1015737269?share=copy#t=0)

Contributing:
- Feel free to fork this repository and contribute by submitting a pull request.


