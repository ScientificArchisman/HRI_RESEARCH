**Project Name:** Database Management GUI with DTALE

**Description:**
This project offers a powerful and user-friendly solution for managing and analyzing your database with ease. We've developed a Graphical User Interface (GUI) that seamlessly connects with your database client, utilizing the DTALE library to filter and structure your data effortlessly. 

**Key Features:**

1. **Effortless Database-to-Dataframe Conversion:** We leverage the power of PyMatGen and ASE to efficiently convert your database into a Pandas Dataframe, making it ready for analysis.

2. **Dynamic Data Filtering:** Our GUI provides intuitive and dynamic data filtering options, allowing you to sift through your data quickly and precisely.

3. **Exploratory Data Analysis (EDA):** Explore your data with various graphing capabilities built into the GUI. Conduct in-depth exploratory data analysis to gain valuable insights.

4. **Machine Learning Integration:** Seamlessly integrate your data with machine learning algorithms, facilitating predictive modeling and data-driven decision-making.

5. **Flexible Data Export and Import:** Export your structured data in multiple formats, including CSV, XML, and more. Likewise, import data in these formats effortlessly.

6. **Docker Container for Easy Deployment:** We've packaged this powerful tool into an executable file using a Docker container, ensuring straightforward deployment across different environments.



## Screenshots
<img src = "screenshots/Screenshot 2023-09-09 at 11.25.03 AM.png">

<img src = "screenshots/Screenshot 2023-09-09 at 11.25.22 AM.png">

<img src = "screenshots/Screenshot 2023-09-09 at 11.25.39 AM.png">

<img src = "screenshots/Screenshot 2023-09-09 at 11.28.39 AM.png">

## Deployment

**Step 1: Dockerfile**

Create a Dockerfile in your project directory. This file defines the environment and instructions for building the Docker image.

```bash
# Use a base image with the desired Python version
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Specify the command to run your GUI application
CMD ["python", "your_app.py"]
```

**Step 2:** Building the Docker Image

Navigate to your project directory in the terminal and build the Docker image using the following command:
```bash
docker build -t app-name .
```

**Step 3:** Running the Docker Container

Once the image is built successfully, you can run a container from it using the following command:

```bash
docker run -p 8080:80 your-app-name
```
