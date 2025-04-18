pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                git url: 'https://github.com/Arushi9740/sepp02.git', branch: 'main'
            }
        }

        stage('Setup Dependencies') {
            steps {
                echo "Setting up Python virtual environment and installing dependencies"
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }

        stage('Run bill records') {
            steps {
                echo "Executing bill.py"
                bat '''
                call venv\\Scripts\\activate
                python bill.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running test_bill.py"
                bat '''
                call venv\\Scripts\\activate
                pytest test_bill.py
                '''
            }
        }
    }
}
