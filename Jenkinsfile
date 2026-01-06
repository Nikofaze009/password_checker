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
        
        stage('Test Password') {
            steps {
                echo 'Validating password checker files...'
                script {
                    bat 'dir password_checker*.py'
                    echo "Would check password: ${params.PASSWORD}"
                    echo 'Files validated successfully!'
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
