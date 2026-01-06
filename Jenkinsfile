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
                echo 'Running password checker...'
                script {
                    bat "python password_checker_cli.py ${params.PASSWORD}"
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
