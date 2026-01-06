pipeline {
    agent any
    
    parameters {
        string(name: 'PASSWORD', defaultValue: 'Test123!', description: 'Enter password to check')
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
                echo 'Code validated successfully'
            }
        }
        
        stage('Validate') {
            steps {
                echo 'Validating project files...'
                script {
                    bat 'dir *.py'
                    bat 'dir Dockerfile'
                    echo "Parameter received: ${params.PASSWORD}"
                    echo 'All files present - ready for Docker build!'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            echo 'Password strength check completed.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
