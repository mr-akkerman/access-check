# Access Checker API

🤝 A simple and fast way to deploy an API for checking hosting accessibility from a Docker container.

![GitHub last commit](https://img.shields.io/github/last-commit/mr-akkerman/access-check)

## How to Use

1. Install Docker if you haven't already by following the [official Docker documentation](https://docs.docker.com/get-docker/).

2. Run the container using the following command, specifying your desired port (e.g., 8006):

   ```bash
   docker run -d --name api-checker -p 8006:8000 mrakkerman/access-check:latest
   ```

## 📚 Endpoints

#### `GET http://your-ip:8006/docs` - Swagger UI (API documentation)

#### `GET/POST http://your-ip:8006/v1/access-checking/simple-check` - Check if a host is accessible
   
### 🤌 Profit

