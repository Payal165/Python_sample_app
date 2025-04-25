pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest'
            }
        }

        stage('Run App') {
            steps {
                sh './venv/bin/python app.py'
            }
        }
    }

    post {
        success {
            echo " Build and test successful!"
        }
        failure {
            echo " Build failed."
        }
    }
}

