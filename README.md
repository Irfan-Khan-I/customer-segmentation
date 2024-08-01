# customer-segmentation
This Flask-based web app enables customer segmentation using machine learning. Users upload CSV files, and the app preprocesses the data and applies KMeans clustering for demographic and behavioral segmentation. Results are displayed on the web interface in JSON format. Includes data preprocessing and scalable segmentation algorithms.


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/customer-segmentation.git
   cd customer-segmentation
2.Create and Activate a Virtual Environment:

    python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

3.Install Dependencies:
    pip install -r requirements.txt
    
##Running the Application
python3 app.py #On Windows use: python app.py

Access the Web Interface:

Open your web browser and navigate to http://127.0.0.1:5000. You will see a form to upload your CSV files for segmentation.

##Docker Setup
To run the application in a Docker container:

Build the Docker Image:

bash
Copy code
docker build -t customer-segmentation .
Run the Docker Container:

bash
Copy code
docker run -p 5000:5000 customer-segmentation

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.



Replace `Irfan-Khan-I` and `ik914149986@gmail.com` with your actual GitHub username and email address. Adjust the content as necessary based on your specific project details and requirements.



