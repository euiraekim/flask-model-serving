pipeline {
    agent any
    environment {
        GITHUB_URL = 'https://github.com/euiraekim/flask-model-serving.git'
        GITHUB_CRED_ID = '569c9736-376a-4703-aa98-1aed5c2770e1'
        GITHUB_BRANCH = 'main'

        DOCKERHUB_REPO = "harrykur139/flask-ml-server"
        DOCKERHUB_CRED_ID = "d174b66f-c2eb-44b8-83c9-481726b28bb6"
        DOCKERHUB_CRED = credentials(DOCKERHUB_CRED_ID)
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
                sh 'docker image build -t $DOCKERHUB_REPO:latest .'
                sh 'docker image tag $DOCKERHUB_REPO:latest $DOCKERHUB_REPO:$BUILD_NUMBER'
                echo 'Build end'
            }
        }
        stage('Push') {
            steps {
                echo 'Push start'
                echo 'echo $DOCKERHUB_CRED_PSW | docker login -u $DOCKERHUB_CRED_USR --password-stdin'
                sh 'echo $DOCKERHUB_CRED_PSW | docker login -u $DOCKERHUB_CRED_USR --password-stdin'
                sh 'docker push $DOCKERHUB_REPO:$BUILD_NUMBER'
                sh 'docker push $DOCKERHUB_REPO:latest'
                echo 'Push end'
            }
        }
    }
}