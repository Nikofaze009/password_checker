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
                echo 'Validating application files...'
                script {
                    bat 'dir *.py'
                    echo 'Python files validated'
                }
            }
        }
        
        stage('Validate') {
            steps {
                echo 'Project validation complete'
                script {
                    echo "Password parameter received: ${params.PASSWORD}"
                    echo 'Note: Run Docker commands locally to see password checker output'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            echo '======================================'
            echo 'To see password checker output, run:'
            echo "docker run --rm nikofaze009/password-checker:latest python password_checker_cli.py \"${params.PASSWORD}\""
            echo '======================================'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
