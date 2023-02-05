# `Myflix backend`
This application was created as a netflix clone for my "Dev-ops and microservices" module, the technologies used within its frontend are:
- Flask
- Nginx
- MongoDB
- MySQL
- Docker 
- Github Actions
- Kubernetes

### `Backend description`
This applications backend is made up of several parts. It uses Flask for its rest API that allows the frontend to fetch data from MySQL and MongoDB. MySQL is used to hold user account information for logging in and creating accounts. MongoDB is used to store information about the movies that the frontend showcases. Nginx is used to provide static .m3u8 and .ts HLS format video files as well as the .png image files used for the movie posters/thumbnails.

### `Deployment`
This application is deployed using Github Actions, Docker and Kubernetes. For this I used a kube cluster hosted with Linode that I could manipulate using my kube config as a github secret as well as my docker hub login using an access token. This meant that I could upload the updated docker build straight to dockerhub and update my kubernetes deployment with this new docker image.

### `Module takeaways`
At the time of creating this application all of these technologies were new to me and required a steep learning curve but in the end after this assignment was finished I felt that I had a much greater understanding of all of these technologies involved and really saw the impact that docker can have.

### Frontend: https://github.com/Stuflo19/Myflix-frontend 