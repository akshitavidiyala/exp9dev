pipeline {
    agent any

    environment {
        DOCKERHUB_USER = '<your-dockerhub-username>'
        IMAGE_NAME = 'jenkins-docker-demo'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKERHUB_USER/$IMAGE_NAME:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh '''
                docker tag $DOCKERHUB_USER/$IMAGE_NAME:${BUILD_NUMBER} $DOCKERHUB_USER/$IMAGE_NAME:latest
                docker push $DOCKERHUB_USER/$IMAGE_NAME:${BUILD_NUMBER}
                docker push $DOCKERHUB_USER/$IMAGE_NAME:latest
                '''
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f || true'
        }
        success {
            echo "Build and push successful!"
        }
    }
}

