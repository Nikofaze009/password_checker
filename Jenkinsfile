pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "password-checker"
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        DOCKER_REGISTRY = "docker.io/nikofaze009"  // Your Docker Hub username
        DOCKER_CREDENTIALS = "docker-hub-credentials"  // Jenkins credential ID
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the application...'
                script {
                    // You can add build steps here if needed
                    bat 'python --version'
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    // Add test commands here
                    bat 'python -m py_compile password_checker.py'
                }
            }
        }
        
        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                script {
                    bat """
                        docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG} .
                        docker tag ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest
                    """
                }
            }
        }
        
        stage('Docker Push') {
            steps {
                echo 'Pushing Docker image to registry...'
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS}", 
                                    usernameVariable: 'DOCKER_USER', 
                                    passwordVariable: 'DOCKER_PASS')]) {
                        bat """
                            echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin ${DOCKER_REGISTRY}
                            docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}
                            docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest
                        """
                    }
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container for verification...'
                script {
                    bat """
                        docker run -d --name password-checker-test ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}
                        timeout /t 5 /nobreak
                        docker logs password-checker-test
                        docker stop password-checker-test
                        docker rm password-checker-test
                    """
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            echo "Docker image pushed: ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}"
            echo "Image is ready to be deployed on any platform supporting Docker containers"
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
        always {
            echo 'Cleaning up...'
            bat 'docker system prune -f'
        }
    }
}
