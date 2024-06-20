# Simple summarizer

This is a simple web application for summarizing text. It uses a pre-trained model available on HuggingFaceHub. 
The application uses the langchain Python package for developing applications powered by large language models to handle the required logic. 
To implement the necessary endpoint, I used the popular Python framework FastAPI. Additionally, I wrote a Dockerfile to ensure the application runs without problems.

# Usage

1. First you must have docker installed and have repository cloned.
2. Then do not forget to include your access token to a HuggingFaceHub in the entrypoint.sh - ![Screenshot from 2024-06-20 11-35-37](https://github.com/Andry925/charity_auctions/assets/114020399/7d2caad2-a48c-4b53-84a4-9be9b42f6698)
3. Build container by running - ```bash docker build -t my_app .```.
4. Then run it by - ```bash docker run -p 80:80 my_app```.
5. After this you can access application by clicking this link - ![Screenshot from 2024-06-20 11-45-16](https://github.com/Andry925/charity_auctions/assets/114020399/9a464979-10d3-4b25-8c2a-b5c6ff9ea957)

# Tests

To test the application, I used the popular API testing tool Postman. Here is how the application works:
![Screenshot from 2024-06-20 11-48-39](https://github.com/Andry925/Methodologies_2/assets/114020399/bd016652-bb33-44ed-bf7d-b1cf3238a469)






