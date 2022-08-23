pipeline {
    agent any
    environment {
        GITHUB_URL = 'https://github.com/euiraekim/flask-model-serving.git'
        GITHUB_CRED_ID = 'github-token'
        GITHUB_BRANCH = 'main'

        DOCKERHUB_REPO = 'harrykur139/flask-ml-server'
        DOCKERHUB_CRED = credentials('dockerhub-token')
        CONTAINER_NAME = 'flask-ml-container'
    }
    stages {
        stage('Clone') {
            steps {
                echo 'Clone start'
                git branch: GITHUB_BRANCH, credentialsId: GITHUB_CRED_ID, url: GITHUB_URL
                sh 'ls'
                echo 'Clone end'
            }
        }
        stage('Test') {
            steps {
                echo 'Test start'
                sh 'docker build -f Dockerfile.test -t test-image .'
                sh 'docker run test-image'
                echo 'Test end'
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
                sh 'echo $DOCKERHUB_CRED_PSW | docker login -u $DOCKERHUB_CRED_USR --password-stdin'
                sh 'docker push $DOCKERHUB_REPO:$BUILD_NUMBER'
                sh 'docker push $DOCKERHUB_REPO:latest'
                echo 'Push end'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy start'
                script{
                    if (BUILD_NUMBER == "1") {
                        sh 'docker run --name $CONTAINER_NAME -d -p 5000:5000 $DOCKERHUB_REPO'
                    }
                    else {
                        sh 'docker stop $CONTAINER_NAME'
                        sh 'docker rm $CONTAINER_NAME'
                        sh 'docker run --name $CONTAINER_NAME -d -p 5000:5000 $DOCKERHUB_REPO'
                    }
                }
                echo 'Deploy end'
            }
        }
    }
}