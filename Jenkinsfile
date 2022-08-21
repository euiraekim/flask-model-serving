pipeline {
    agent any
    environment {
        GIT_URL = 'https://github.com/euiraekim/flask-model-serving.git'
        GIT_CRED_ID = '569c9736-376a-4703-aa98-1aed5c2770e1'
        GIT_BRANCH = 'main'

        DOCKER_HUB_REPO = "talha1995/test"
        CONTAINER_NAME = "flask-container"
        STUB_VALUE = "200"
    }
    stages {
        stage('Clone') {
            steps {
                echo 'Clone start'
                git branch: GIT_BRANCH, credentialsId: GIT_CRED_ID, url: GIT_URL
                sh 'ls'
                echo 'Clone end!'
            }
         }
        stage('Test') {
            steps {
                echo 'Test start'
                sh 'docker build -f Dockerfile.test -t test-image .'
                sh 'docker run test-image'
                echo 'Test end!!'
            }
         }
    }
}