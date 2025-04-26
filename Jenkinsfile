pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Payal165/Python_sample_app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv ${VENV}'
                sh './${VENV}/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './${VENV}/bin/pytest'
            }
        }

        stage('Deploy App') {
            steps {
                sh 'nohup ./${VENV}/bin/python app.py &'
            }
        }
    }

    post {
        success {
            echo "✅ App deployed successfully!"
        }
        failure {
            echo "❌ Something went wrong."
        }
    }
}

