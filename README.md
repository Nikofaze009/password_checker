# Password Checker - CI/CD Pipeline

An advanced password strength checker application with a complete CI/CD pipeline using Jenkins and Docker.

## Features

- Checks password strength based on multiple criteria
- Provides feedback and suggestions for improvement
- Detects common passwords
- Scores passwords from 0-11

## Prerequisites

- Git
- Docker
- Jenkins
- Docker registry access (Docker Hub, ACR, ECR, etc.)

## Project Structure

```
Project/
├── password_checker.py      # Main application
├── Dockerfile               # Docker image configuration
├── Jenkinsfile             # Jenkins pipeline configuration
├── k8s-deployment.yaml     # Kubernetes deployment manifest
├── README.md              # This file
```

## Setup Instructions

### 1. Push Code to GitHub

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Password checker with CI/CD pipeline"

# Add remote repository (replace with your repo URL)
git remote add origin https://github.com/yourusername/password-checker.git

# Push to GitHub
git push -u origin main
```

### 2. Configure Jenkins

1. **Install Required Plugins:**
   - Docker Pipeline
   - Kubernetes CLI
   - Git plugin
   - Git plugin
   - Pipeline plugin

2. **Add Credentials:**
   - Docker registry credentials (ID: `docker-hub-credentials`)
     - Go to Jenkins → Manage Jenkins → Credentials
     - Add Username with password for your Docker registry

3. **Create Pipeline Job:**
   - New Item → Pipeline
   - Configure SCM: Git (your repository URL)
   - Script Path: `Jenkinsfile`

4. **Update Jenkinsfile Variables:**
   - Update `DOCKER_REGISTRY` with your registry URL (e.g., `docker.io/yourusername`)
### 3. Build and Push Docker Image

Manual build (optional):
```bash
# Build the image
docker build -t your-registry/password-checker:latest .

# Login to registry
docker login your-registry

# Push the image
docker push your-registry/password-checker:latest
```

### 4. Run the Container

After the pipeline completes, you can run the container on any Docker host:

```bash
# Pull the image
docker pull your-registry/password-checker:latest

# Run the container
docker run -it your-registry/password-checker:latest

# Or run in detached mode
docker run -d --name password-checker your-registry/password-checker:latest

# View logs
docker logs password-checker
```

## CI/CD Pipeline Stages

1. **Checkout**: Clones code from GitHub
2. **Build**: Validates Python environment
3. **Test**: Compiles Python code for syntax errors
4. **Docker Build**: Creates Docker image
5. **Docker Push**: Pushes image to registry
6. **Deploy to Kubernetes**: Deploys application to K8s cluster
 and tags it
5. **Docker Push**: Pushes image to Docker registry
6. **Run Docker Container**: Verifies the container runs correctly
### Local Testing

```bash
python password_checker.py
```

### Access Deployed Application

After Kubernetes deployment:
```bashocker Container

After Jenkins pipeline completes:
```bash
# Pull and run the latest image
docker pull your-registry/password-checker:latest
docker run -it your-registry/password-checker:latest
```

## Configuration

### Docker Image

- **Base Image**: Python 3.9-slim
- **Working Directory**: /app
- **Environment**: PYTHONUNBUFFERED=1

### Customization

1. **Change Python version**: Edit `FROM` line in [Dockerfile](Dockerfile)
2. **Add dependencies**: Update [requirements.txt](requirements.txt)
3. **Modify Docker registry**: Update `DOCKER_REGISTRY` in [Jenkinsfile](Jenkinsfile
```bash
# View logs
kubectl logs -f deployment/password-checker-deployment

# Check pod status
kubectl get pods -l app=password-checker
container logs
docker logs password-checker

# Check running containers
docker ps

# Inspect container
docker inspect password-checker

# View container resource usage
docker stats password-checker
```

## Troubleshooting

### Docker Build Issues
- Ensure Docker daemon is running
- Check Dockerfile syntax
- Verify base image availability: `docker pull python:3.9-slim`

### Docker Push Issues
- Verify Docker registry credentials
- Login manually: `docker login your-registry`
- Check network connectivity to registry

### Jenkins Pipeline Issues
- Verify credentials are configured correctly in Jenkins
- Check Jenkins has Docker installed: `docker --version`
- Review Jenkins console output for detailed errors
- Ensure Jenkins user has Docker permissions

## Deployment Options

Once the image is in the registry, you can deploy it to:

1. **Docker Host**: `docker run -it your-registry/password-checker:latest`
2. **Docker Swarm**: Create a stack/service
3. **Cloud Platforms**: AWS ECS, Azure Container Instances, Google Cloud Run
4. **Any platform supporting Docker containers**

## Cleanup

```bash
# Stop and remove container
docker stop password-checker
docker rm password-checker

# Remove Docker images locally
docker rmi your-registry/password-checker:latest

# Remove from registry (if needed)
# This depends on your registry provider

## Author

Your Name

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
