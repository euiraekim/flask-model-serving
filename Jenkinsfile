pipeline {
    agent any
    environment {
        GIT_URL = 'https://github.com/euiraekim/flask-model-serving.git'
        GIT_CRED_ID = '569c9736-376a-4703-aa98-1aed5c2770e1'
        GIT_BRANCH = 'main'

        DOCKER_HUB_REPO = "harrykur139/flask-ml-server"
        CONTAINER_NAME = "flask-ml-container"
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
        stage('Build') {
            steps {
                echo 'Build start'
                sh 'docker image build -t $DOCKER_HUB_REPO:latest .'
                sh 'docker image tag $DOCKER_HUB_REPO:latest $DOCKER_HUB_REPO:$BUILD_NUMBER'
                echo 'Build end'
            }
        }
        stage('Push') {
            steps {
                echo 'Push start'
                sh 'docker push $DOCKER_HUB_REPO:$BUILD_NUMBER'
                sh 'docker push $DOCKER_HUB_REPO:latest'
                echo 'Push end'
            }
        }
    }
}