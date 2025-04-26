
pipeline {
    agent any
    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Branch to build from')
        choice(name: 'BUILD_VERSION', choices: ['v1.0', 'v1.1', 'v2.0'], description: 'Select the build version')
    }

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: "${params.BRANCH_NAME}", url:"https://github.com/Payal165/Python_sample_app.git"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv ${VENV}'
                sh 'chmod +x ./venv/bin/pip'
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

