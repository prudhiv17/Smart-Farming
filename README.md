A Decision Support System for Smart Farming and Sustainable Agricultural Practices
Overview
This project aims to enhance farming efficiency by integrating modern technology and data analytics. The decision support system leverages machine learning models and real-time weather data to provide actionable insights for disease detection, crop management, and sustainable farming. By optimizing resource utilization and providing accurate crop forecasts, the system helps improve overall productivity while minimizing environmental impact.

Key Features
Disease Detection: Utilizes image processing and Convolutional Neural Networks (CNNs) to identify and classify plant diseases.
Crop Management: Provides recommendations based on soil and climate data to ensure optimal crop growth.
Weather-Based Predictions: Integrates real-time weather data to predict disease outbreaks and recommend preventive measures.
Fertilizer Calculator: Suggests the appropriate type and amount of fertilizer based on crop and soil data.
Sustainability Focus: Helps reduce waste, lower operational costs, and promote eco-friendly farming practices.
Project Structure
/models: Pre-trained machine learning models (CNN for disease detection, Random Forest for crop recommendations, etc.)
/api: Backend FastAPI code for serving predictions and recommendations.
/frontend: React-based frontend for user interaction.
/data: Sample datasets for testing and training.
/notebooks: Jupyter notebooks with the model training and evaluation code.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/repo-name.git
cd repo-name
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Start the FastAPI server:

bash
Copy code
uvicorn api.main:app --reload
Navigate to the frontend directory and start the React app:

bash
Copy code
cd frontend
npm install
npm start
Usage
Upload plant images to detect diseases.
Input weather data or fetch it automatically to get crop recommendations.
Use the fertilizer calculator for accurate recommendations based on your crop type.
Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.
