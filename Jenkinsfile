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
                echo 'Building Docker image...'
                script {
                    bat 'docker build -t password-checker-test .'
                }
            }
        }
        
        stage('Validate') {
            steps {
                echo 'Testing password checker with Docker...'
                script {
                    echo "Checking password: ${params.PASSWORD}"
                    bat "docker run --rm password-checker-test python password_checker_cli.py \"${params.PASSWORD}\""
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            echo 'Password strength check completed. Check the output above!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
        always {
            script {
                bat 'docker rmi password-checker-test || exit 0'
            }
        }
    }
}
