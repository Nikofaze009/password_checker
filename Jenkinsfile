pipeline {
    agent any
    
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
                    bat 'python --version'
                    echo 'Python environment verified'
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    bat 'python -m py_compile password_checker.py'
                    echo 'Syntax check passed!'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            echo 'Code is ready. You can now build and push Docker image manually.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
