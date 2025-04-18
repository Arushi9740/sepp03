pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                git url: 'https://github.com/Arushi9740/sepp03.git', branch: 'main'
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

        stage('Run beneficiary') {
            steps {
                echo "Executing beneficiary.py"
                bat '''
                call venv\\Scripts\\activate
                python beneficiary.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running test_case.py"
                bat '''
                call venv\\Scripts\\activate
                pytest test_case.py
                '''
            }
        }
    }
}
